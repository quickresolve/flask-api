from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField, validators

class SignupForm(Form):
  first_name = StringField('First name', [validators.DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', [validators.DataRequired("Please enter your last name.")])
  email = StringField('Email', [validators.DataRequired("Please enter your email address."), validators.Email("Please enter a valid email address.")])
  password = PasswordField('New Password', [
        validators.DataRequired("Please enter a password."),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=6, message="Passwords must be 6 characters or more.")
    ])
  confirm = PasswordField('Repeat Password')
  submit = SubmitField('Sign up')


class LoginForm(Form):
  email = StringField('Email', [validators.DataRequired("Please enter your email address."), validators.Email("Please enter a valid email address.")])
  password = PasswordField('Password', [
        validators.DataRequired("Please enter your password.")])
  remember_me = BooleanField('remember_me', default=False)
  submit = SubmitField('Sign in')

