"""
    ****** Learnings from this topic  ******:

        1> Building URL dynamically --> in below, I've build URL dynamically / directly in browse ex: http://127.0.0.1:4000/result/100, which returns Passed in table 


        2> Variable rules --> the "score" is handled to accept integers only even though URL would later interpret it as string

        3> Jinja 2 template engine            
                        {{      }}      --> expressions to print output ex: variables in html
            for ex:     {%      %}       --> if conditions ; for loops  NOTE: before or after %, there should be NO spaces
                        {#      #}       --> this is for comments
"""

# refer below logic to handle -ve intgers (signed integers) in URL's - totally unnecessary::
"""
from werkzeug.routing import IntegerConverter, Map
class SignedIntConverter(IntegerConverter):
    regex = r'-?\d+'

# Register the custom converter
jinja_2_app.url_map.converters['signed_int'] = SignedIntConverter

"""
from flask import Flask, render_template

jinja_2_app: Flask = Flask(__name__)

@jinja_2_app.route('/result/<int:score>')
def student_result(score: int) -> str:
    return render_template('result.html', score = score)


if __name__ == '__main__':
    jinja_2_app.run(debug = True)
