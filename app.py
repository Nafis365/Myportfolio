from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
import smtplib



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
Bootstrap(app)
subscribers = []




class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])



@app.route('/', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@app.route('/cong')
def e():
    return render_template("cong.html")

@app.route('/signup', methods=['GET','POST'])
def f():

    form = RegisterForm()
    if form.validate_on_submit():
        #new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        #db.session.add(new_user)
        #db.commit()
        return'<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template("signup.html", form=form)

@app.route('/hobbies')
def g():
    return render_template("hobbies.html")

@app.route('/forget')
def h():
    return render_template("forget.html")


@app.route('/base')
def index():
    return render_template("base.html")


@app.route('/home')
def a():
    return render_template("Mainpage.html")


@app.route('/contactme')
def b():
    return render_template("Contact.html")


@app.route('/whoami')
def c():
    return render_template("WHOAMI.html")


@app.route('/mywork')
def d():
    return render_template('gallery.html')


@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")


@app.route('/thanks', methods=["POST"])
def thanks():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    if not first_name or not last_name or not email:
        error_statement = "All Form Fields Required..."
        return render_template("subrcribe.html",
                               error_statement = error_statement,
                               first_name=first_name,
                               last_name=last_name,email=email)


    subscribers.append(f" {first_name} {last_name} || {email}")

    message = "You have been suscribe to my email newsLetter"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("soen287class@gmail.com", "@1234abc")
    server.sendmail("soen287class@gmail.com", email, message)
    title = "Thank You!"

    return render_template("thanks.html", subscribers=subscribers)






if __name__=='__main__':
    app.run(debug=True)