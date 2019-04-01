from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

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
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form action="/" method='post'>
            <label>Rotate by:
            <input type="text" value="0" name="rot" />
            <textarea name="text">{0}</textarea>
            <input type="submit">
            <label>
            <form>
        </body>
    </html>"""

@app.route("/")
def index():
    answer = ''
    answer = form.format("")
    return answer

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    message = request.form['text']
    answer = form.format(rotate_string(message, rot))
    return answer

    


app.run()
