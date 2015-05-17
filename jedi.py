"""
Try making a new view called /jedi. In this view, you should work out what a person's Jedi name is, and return it to them as HTML. Your Jedi name is the first three letters of your last name, followed by the first two letters of your first name. So visiting /jedi/beyonce/knowles should tell you that your Jedi name is "knobe".
"""

from flask import Flask

app = Flask(__name__)

@app.route("/jedi/<firstname>/<lastname>")
def hello_person(firstname, lastname):
    html = """
        <h1>
            Hello {}!
        </h1>
    """
    return html.format(lastname[0:3].title() + firstname[0:2])

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)