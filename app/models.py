from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
db = SQLAlchemy()
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)

  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

  def is_active(self):
        """True, as all users are active."""
        return True

  def get_id(self):
      """Return the email address to satisfy Flask-Login's requirements."""
      return self.email


  def is_anonymous(self):
      """False, as anonymous users aren't supported."""
      return False