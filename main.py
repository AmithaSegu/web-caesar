from flask import Flask , request
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
        <form actions='/encrypt' methods='POST' >
            <label for="rot"> Rotate  </label>
            <input id="rot" type="text" name="rot" value='0'/>  <br>
            
            <label for="text">Text</label>
            <textarea name="text">{0}</textarea>
            
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rotate_by=int(request.form['rot'])
    text_encrypt=request.form['text']
    encrypted_string=rotate_string(text_encrypt,rotate_by)
    #content = 
    return form.format(encrypted_string)

@app.route("/")
def index():
    return form.format("")

app.run()