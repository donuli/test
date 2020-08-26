from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Non-Labelled")
def NonLabelled():
    return render_template("NonLabelled.html")

@app.route("/Labelled")
def Labelled():
    return render_template("Labelled.html")

@app.route("/Verified")
def Verified():
    return render_template("Verified.html")
