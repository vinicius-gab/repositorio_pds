from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class CadastroForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('senha', validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField('Entrar')
    
    def validate_username(self, field):
        if field.data.lower() == 'admin':
            raise ValidationError('O nome "admin" está reservado. Escolha outro.')