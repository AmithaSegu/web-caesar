from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<! DOCTYPE html >
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method='POST'>
            <label for="rot"> Rotate  </label>
            <input type="text" name="rot" value="0"></input>
            <textarea name="text">{0}</textarea>
            <input type="submit"></input> 
        </form>
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rotate_by=int(request.form['rot'])
    text_to=request.form['text']
    encrypted_string=rotate_string(text_to, rotate_by)
    return form.format(encrypted_string)

@app.route("/")
def index():
    return form.format("")

app.run()