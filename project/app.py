import os
from flask import Flask, redirect, url_for, render_template, request, send_from_directory

app = Flask("__name__")

pic = os.path.join('static', 'pictures')

app.config['UPLOAD_FOLDER'] = pic

#pages
@app.route("/")
@app.route("/home")
def home():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'huis1.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'huis2.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], 'huis3.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], 'huis4.jpg')
    pic5 = os.path.join(app.config['UPLOAD_FOLDER'], 'huis5.jpg')
    pic6 = os.path.join(app.config['UPLOAD_FOLDER'], 'huis6.jpg')
    return render_template("home.html", huis1=pic1, huis2=pic2, huis3=pic3, huis4=pic4, huis5=pic5, huis6=pic6)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)