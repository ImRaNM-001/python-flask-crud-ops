from flask import Flask, Blueprint, render_template, redirect, url_for
from werkzeug import Response

main_bp: Blueprint = Blueprint('main', __name__)

@main_bp.route('/')
def welcome() -> str:
    return """<html>
                <H1>Welcome to flask course - function overriden</H1>
            </html>"""                             # this is bad practice

@main_bp.route('/index')
def index() -> str:
    return render_template('index.html')

@main_bp.route('/about')
def about() -> str:
    return render_template('about.html')

main: Flask = Flask(__name__)
main.register_blueprint(main_bp, url_prefix='/main')

# add a app redirect route
@main.route('/')
def root() -> Response:
    return redirect(url_for('main.welcome'))

if __name__ == '__main__':
    main.run(debug = True, port = 3000)

