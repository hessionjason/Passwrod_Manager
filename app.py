from flask import Flask, render_template, request, redirect, url_for, flash
import hashlib

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # For session-based flash messages

# In-memory storage for accounts
password_manager = {}

@app.route("/")
def home():
    """Homepage."""
    return render_template("home.html")

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    """Handle account creation."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in password_manager:
            flash("Username already exists!", "error")
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            password_manager[username] = hashed_password
            flash("Account created successfully!", "success")
        return redirect(url_for("home"))
    return render_template("create_account.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in password_manager and password_manager[username] == hashed_password:
            flash("Login successful!", "success")
        else:
            flash("Incorrect username or password!", "error")
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/view_accounts")
def view_accounts():
    """Display all accounts."""
    return render_template("view_accounts.html", accounts=password_manager.keys())

if __name__ == "__main__":
    app.run(debug=True)
