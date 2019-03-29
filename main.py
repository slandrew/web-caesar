from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form action="/" method='post'>
            <label>Rotate by:
            <input type="text" value="0" name="rot" />
            <input type="textarea" name="text" />
            <input type="submit">
            <label>
            <form>
        </body>
    </html>"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    message = request.form['text']
    encrypted = rotate_string(message, rot)
    content = "<h1>" + encrypted + "</h1>"
    return content

    


app.run()
