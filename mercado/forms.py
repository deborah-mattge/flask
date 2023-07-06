from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from mercado.models import User


class CadastroForm(FlaskForm):
    def validate_username(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuário já existe! Cadastre outro usuário.")

    def validate_email(self, check_email):
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("E-mail já existe! Cadastre outro e-mail.")

    usuario = StringField(label='Usuário: ', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email: ', validators=[Email(), DataRequired()])
    senha1 = PasswordField(label='Senha: ', validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField(label='Confirmação de Senha: ', validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Cadastrar')