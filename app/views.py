from flask import *
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for OpenID="%s", remember_me=%s' %
          (form.openid.data, str(form.remember_me.data)))
    return redirect('/index')
  return render_template('login.html',
                          title='Sign In',
                          form=form)


@app.route('/api')
def api():
  return jsonify({'posts': posts})


# render_template function invokes the Jinja2 templating engine that is part of the Flask framework. Jinja2 substitutes {{...}} blocks with the corresponding values provided as template arguments. The Jinja2 templates also support control statements, given inside {%...%} blocks.