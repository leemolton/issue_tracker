import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return render_template("base.html")
    

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
       flash("Thanks {}, you have added to the forum!".format(
            request.form["name"]))
    return render_template("add.html", page_title="Add to forum")

   
@app.route('/view')
def view():
    return render_template("view.html", page_title="View forum")
    

@app.route('/pay')
def pay():
    return render_template("pay.html", page_title="Pay for Predictions Comp.")
    
    
@app.route('/blog')
def blog():
    return render_template("blog.html", page_title="Blog")
    
    
@app.route('/predict')
def predict():
    return render_template("predict.html", page_title="Predictions")
    
    
@app.route('/login')
def login():
    return render_template("login.html", page_title="Pay for Predictions")
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)