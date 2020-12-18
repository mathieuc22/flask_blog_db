from flask import Flask, render_template, request, redirect, url_for
from . import app
from .models import User, db

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = str(request.form.get("username")) or None
        email = str(request.form.get("email")) or None
        u = User(username=username, email=email)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('users'))
    else:
        return render_template("register.html")

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route("/users/<int:user_id>")
def user(user_id):
    # Make sure user exists.
    user = User.query.get(user_id)
    if user is None:
        return render_template("error.html", message="No such user.")
    return render_template("user.html", user=user)

if __name__ == "__main__":
    app.run()