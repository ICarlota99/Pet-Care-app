from datetime import datetime
from flask import Flask, redirect, render_template, request, session, make_response

from helpers import error_message, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies?)

@app.route('/')
def home():
    # Verify if it is a new user
    if request.cookies.get("new_user") is None:
        # New user: show welcome message
        return render_template("home.html", is_new_user=True)
    else:
        # Redirect to homepage
        return render_template("index.html", year=datetime.now().year)

@app.route("/set-cookie")
def set_cookie():
    # Configurar la cookie para marcar que el usuario no es nuevo
    response = make_response(redirect(url_for("index")))
    response.set_cookie("new_user", "no", max_age=60*60*24*365)  # Cookie válida por 1 año
    return response


@app.route('/register', methods=["GET", "POST"])
def register():
    """Register a new user"""
    return render_template(".html")


@app.route('/login', methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST
    if request.method == "POST":
        # Ensure username and password were submited
        if not request.form.get("username"):
            return apology("must provide username", 403)
        
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        
        # Query database for username

        # Ensure username exists and password is correct

        # Remember which user has logged in

        # Redirect user to home page
        return redirect("/")
    
    # User reached route via GET
    else:
        return render_template("login.html")
    

@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user id
    session.clear()

    # Redirect user to login form
    return redirect("/")
