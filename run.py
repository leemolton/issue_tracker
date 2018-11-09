import os
import json
from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return render_template("index.html")
    

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
       flash("Thanks {}, you have added to the forum!".format(
            request.form["name"]))
    return render_template("add.html", page_title="Add to forum")

   
@app.route('/view')
def view():
    return render_template("datesdiary.html", page_title="Dates for your diary")
    

@app.route('/pay')
def pay():
    return render_template("checkout.html", page_title="Pay for Predictions Comp.")
    
    
@app.route('/post')
def post():
    return render_template("blog.html", page_title="Post")
    
    
@app.route('/predict')
def predict():
    return render_template("predict.html", page_title="Predictions")
 
 
@app.route('/get_posts')
def get_posts():
    return render_template("blogposts.html", {'posts': posts})
    

@app.route('/new_post')
def new_post():
    return render_template("blogpostform.html", page_title="form")
    
    
@app.route('/login')
def login():
    return render_template("login.html", page_title="Pay for Predictions")
    

@app.route('/henry')
def henry():
    return render_template("henry.html", page_title="A step up for Henry")


@app.route('/jose')
def jose():
    return render_template("jose.html", page_title="Is time up for Jose?")


    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)