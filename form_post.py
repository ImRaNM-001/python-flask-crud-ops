from flask import Flask, Blueprint, redirect, render_template, request, url_for
from werkzeug import Response

form_post_bp: Blueprint = Blueprint('form_post', __name__)

# application endpoints:
# 1- This is the landing page / route
@form_post_bp.route('/')
def welcome() -> str:
    return render_template('welcome.html')

# @form_post_bp.route('/index', methods = ['GET'])
# def index() -> str:
#     return render_template('index.html')

# 2- This is a form for name submission
@form_post_bp.route('/form', methods = ['GET','POST'])    # writing both https methods are compulsory to avoid getting "Method Not Allowed" error
def form() -> str:
    if request.method == 'POST':                          # below if block is called when clicked on "Submit" button in the UI
        name: str = request.form['name']
        return f'Hello there {name}'
    return render_template('form.html')


# 3- This is a page for name display post submission - based on the action attribute specified in "form.html", appropriate route gets called
@form_post_bp.route('/submit', methods = ['GET','POST'])   
def submit() -> str:
    if request.method == 'POST':
        name: str = request.form['name']
        return f'You just made a POST call for name: {name}'
    return render_template('form.html')


form_post: Flask = Flask(__name__)
form_post.register_blueprint(form_post_bp, url_prefix = '/home')

# auto-redirect to this route
@form_post.route('/')
def root() -> Response:
    return redirect(url_for('form_post.welcome'))


if __name__ == '__main__':
    form_post.run(debug = True, port = 8080)