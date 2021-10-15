from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)



@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "E:\\Resume-Rahima-Khan.pdf"
    return send_file(path, as_attachment=True)

@app.route("/")
def index():
    return render_template('index.html')


# @app.route("/projects")
# def projects():
#     return render_template('projects.html')


# @app.route("/blogs")
# def blogs():
#     return render_template('blogs.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0')
