from flask import Flask, Blueprint, redirect, url_for
from werkzeug import Response

app_bp: Blueprint = Blueprint('app', __name__)

# not used normal "route" decorator i.e, @app.route('/')
@app_bp.route('/')
def welcome() -> str:
    return 'Welcome to Flask learning project.....'

@app_bp.route('/index')
def index() -> str:
    return 'Welcome to the index page'


""" Initialize the Flask app next,
    which will create an instance of the Flask class > which will be your WSGI (Web Server Gateway Interface) application.
"""

app: Flask = Flask(__name__)
app.register_blueprint(app_bp, url_prefix='/app')

# add a app redirect route
@app.route('/')
def root() -> Response:
    return redirect(url_for('app.welcome'))

if __name__ == '__main__':
    app.run(debug = True)
