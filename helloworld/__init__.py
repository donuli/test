import os
from flask import Flask, render_template, request, redirect, send_file,url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/root/test/helloworld/data'
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename) :
    return '.' in filename and \
            filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Non-Labelled")
def NonLabelled():
    return render_template("NonLabelled.html")

@app.route("/NLupload")
def NLupload():
    return render_template("NLupload.html")

@app.route('/NLsuccess', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['attach']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return render_template("NLsuccess.html")

@app.route("/Labelled")
def Labelled():
    return render_template("Labelled.html")

@app.route("/Verified")
def Verified():
    return render_template("Verified.html")