from flask import *
from models import db, User
from app import app
from .forms import LoginForm, SignupForm

user = {'name': 'guest'} #fake user
posts = [  # fake array of posts
    {
        'author': {'nickname': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'nickname': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
]



@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html',
                         title='Home',
                         user=user,
                         posts=posts)

@app.route('/signup', methods=['GET','POST'])
def signup():
  form=SignupForm(request.form)

  if request.method == 'POST' and form.validate():
      new_user = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
      db.session.add(new_user)
      db.session.commit()
      session['email'] = new_user.email
      return redirect(url_for('index'))
  return render_template('signup.html',
                          title='Sign Up',
                          form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()

  if request.method == 'POST':
    email = form.email.data
    password = form.password.data
    user = User.query.filter_by(email=email).first()
    if user is not None and user.check_password(password):
      session['email'] = form.email.data
      return redirect(url_for('index'))
    else:
      return "Invalid Login"


  return render_template('login.html',
                          title='Sign In',
                          form=form)


@app.route('/api')
def api():
  return jsonify({'posts': posts})


# render_template function invokes the Jinja2 templating engine that is part of the Flask framework. Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments. The Jinja2 templates also support control statements, given inside {%...%} blocks.