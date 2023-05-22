from flask import Flask, render_template, request, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from passlib.hash import bcrypt_sha256
import sqlite3

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Set a secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Create the database table
with sqlite3.connect('users.db') as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        password = bcrypt_sha256.hash(form.password.data)

        with sqlite3.connect('users.db') as conn:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))

        return redirect('/login')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        with sqlite3.connect('users.db') as conn:
            cursor = conn.execute('SELECT password FROM users WHERE username = ?', (username,))
            row = cursor.fetchone()

            if row and bcrypt_sha256.verify(password, row[0]):
                session['username'] = username
                return redirect('/profile')

        return render_template('login.html', form=form, error='Invalid username or password')

    return render_template('login.html', form=form)

@app.route('/profile')
def profile():
    if 'username' in session:
        return f'<h1>Welcome, {session["username"]}!</h1>'
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
