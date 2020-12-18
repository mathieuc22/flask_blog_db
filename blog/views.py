from flask import Flask, render_template

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

from .models import User

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

if __name__ == "__main__":
    app.run()