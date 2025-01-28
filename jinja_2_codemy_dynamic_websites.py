from flask import Flask, render_template, redirect, request, url_for

app: Flask = Flask(__name__)

@app.route('/')
def index() -> str:
    title: str = 'John Doe\'s Portfolio'
    names: list[str] = []
    return render_template('jinja_2_codemy_dynamic_websites.html', title = title, names = names)

""" NOTE:
    1> Always bloody make route unique & different - route corresponds to a unique page - page names cannot be same'

    2> if render_template(.html) is kept common across, then check whatever variables wriiten inside the .html file,
        are also present in the route() fn getting called to avoid getting nasty exceptions / ugly errors

"""

@app.route('/about')
def about() -> str:
    names: list[str] = ['John', 'Stan', 'Ben', 'Hanah']
    return render_template('jinja_2_codemy_dynamic_websites.html', names = names)


@app.route('/user/<name>')
def user(name: str) -> str:
    some_stuff: str = 'This is <strong>Bold</strong> text'
    fav_pizza: list[str | int] = ['Pepperoni', 'Cheese', 'Mushroom', 41]
    return render_template('jinja_2_codemy_username.html',
                           name = name,
                           some_stuff = some_stuff,
                           fav_pizza = fav_pizza)



""" Filters:
    --------------
    are separated from the variable by a pipe symbol (|) and may have optional arguments in parentheses. 
    Multiple filters can be chained. The output of one filter is applied to the next.
    ex: {{name | striptags | title }} will remove all HTML Tags from variable name and title-case the output (title(striptags (name))).
    ------------------------------------------
    safe            --> makes a text display in bold when enclosed with <strong></strong tags [The <strong> tag in HTML is used to define text with strong importance. The content inside the <strong> tag is typically displayed in bold by browsers]

    capitalize    
    lower    
    upper    
    title   
    trim    
    striptags       --> rips off html tags to make a text display in plain text

"""


if __name__ == '__main__':
    app.run(debug = True, port = 8081)
