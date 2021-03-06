"""
Flask Tutorial
Nicholas Johnston
December 20, 2020
"""
from flask import Flask, render_template, abort, redirect, session, url_for
from forms import LoginForm, SignUpForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
database = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

"""Information regarding the Pets in the System."""
pets = [
    {"id": 1, "name": "Nelly", "age": "5 weeks",
     "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
    {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
    {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
    {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
]
"""User information"""
users = [
    {"id": 1, "full_name": "Pet Rescue Team", "email": "team@pawsrescue.co", "password": "adminpass"}
]


@app.route("/")
def home():
    """
    View function for Home page.
    :return:
    """
    return render_template("home.html", pets=pets)


@app.route("/about")
def about():
    """
    Greet the user by name.
    """
    return render_template("about.html")


@app.route("/details/<int:pet_id>")
def details(pet_id):
    """View function for Showing Details of Each Pet."""
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet is None:
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet=pet)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Login to the website
    """
    form = LoginForm()

    if form.validate_on_submit():
        user = next(
            (user for user in users if user["email"] == form.email.data and user["password"] == form.password.data),
            None)
        if user is None:
            return render_template('login.html', form=form, message="Wrong credentials. Please try again.")
        elif form.errors:
            print(form.errors.items())
        else:
            session['user'] = user
            return render_template('login.html', form=form, message='Successfully Logged In!')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    """
    Logout of an account
    """
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('homepage', _scheme='https', _external=True))


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """
    Signup for an account
    """
    form = SignUpForm()

    if form.validate_on_submit():
        new_user = {"id": len(users) + 1,
                    "full_name": form.full_name.data,
                    "email": form.email.data,
                    "password": form.password.data}
        users.append(new_user)
        return render_template('signup.html', message="Successful signup")
    return render_template('signup.html', form=form)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
