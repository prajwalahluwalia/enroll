from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User

class LoginForm(FlaskForm):
   email=StringField("Email", validators=[DataRequired(), Email()])
   password=PasswordField("Password", validators=[DataRequired(),Length(min=6,max=18)])
   rememberMe=BooleanField("Remember Me")
   submit=SubmitField("Login")
   
class RegisterForm(FlaskForm):
   email =StringField("Email", validators=[DataRequired(),Email()])
   password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=18)])
   password_confirm=PasswordField("Re-type Password", validators=[DataRequired(), Length(min=6,max=18), EqualTo('password')])
   first_name=StringField("First Name", validators=[DataRequired(),Length(min=2,max=50)])
   last_name=StringField("Last Name", validators=[DataRequired(),Length(min=2,max=50)])
   submit=SubmitField("Register")
   
   def validate_email(self,email):
      user=User.objects(email=email.data).first()
      if user:
         raise ValidationError("Email already exists")
  