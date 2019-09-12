############################################################
# Project: web application for data science / web scraping #
# Author: bac [and_bac]                                    #
# Date: 2019                                               #
############################################################

from flask import Flask, render_template, url_for, session, request, redirect, logging, flash  # modules from flask
from data import Items
import pymongo # driver for mongdb connectivity
import pandas as pd
import scrapy as scrapy
from bs4 import BeautifulSoup # used for web scraping
import requests # the request HTTP library allows managing HTTP request/responses to/from websites
from wtforms import Form, StringField, TextAreaField, PasswordField, validators #FOR THE WEBFORMS
from passlib.hash import sha512_crypt #passowrd hashing

Items = Items() # defining the items as per model created in data.py

app = Flask(__name__) # creating an instalnce of the Flask class for thsi app as web server

############## db SETUP START ##############
# using mongo db cloud version
# checking the connection to cloud ongodb and printing in the console the list of collections under the database

try:
    myclient = pymongo.MongoClient("mongodb://mrbacco:mongodb001@cluster0-shard-00-00-goutv.mongodb.net:27017,cluster0-shard-00-01-goutv.mongodb.net:27017,cluster0-shard-00-02-goutv.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    mydb = myclient["database001"]
    mycol = mydb["python001"]
    print ("if connected to db, then these are the collections in mydb: ", mydb.list_collection_names()) #used to check if db is connected
except:
    print("Could not connect to MongoDB")

############## db SETUP END ##############


############## Web scraping example START ##############
'''
this is a block of code for web scraping 

# example as following 
with open("./templates/home.html") as file:
    soup = BeautifulSoup(file)

soup = BeautifulSoup("<html>data</html>")
print(soup.prettify)

'''

############## Web scraping example END ##############




############## defining the routes for the different web pages START ##############
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    return render_template("articles.html", items = Items)

@app.route('/list_item/<string:id>/')
def article(id):
    return render_template('list_item.html', id = id)

class Reg(Form): #definition of a class for the registration form
    name = StringField('Name', [validators.Length(min = 1, max = 50)])
    username = StringField('Username', [validators.Length(min = 5, max = 50)])
    email = StringField('Email', [validators.Length(min = 6, max = 50)])
    password = PasswordField('Password', [validators.DataRequired()])

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = Reg(request.form)
    if request.method == 'GET': # make sure the method used is define above
        return render_template('register.html', form = form), print("you are under the register page now using GET, well done bacco ")
    elif request.method == 'POST' and form.validate():
        name = form.name.data                           # the following are the data from the registration form
        username = form.username.data
        email = form.email.data
        password = sha512_crypt.hash(str(form.password.data)) # passsword is encrypted

        # defining a new variable taking as input the values from the registration form
        myuser=[{ 
                "name": name, 
                "username": username, 
                "email" : email, 
                "password" : password
                }]
        # insert the list into the mongo db
        x = mycol.insert_many(myuser), print("inserting this user: ", myuser, "in the database called ", mycol)
        
        return render_template('register.html', form = form), print("you are under the register page now using POST, data are sent to database")
    else: 
        print("this is the error")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None    #declaration for this variable
    if request.method == 'POST':
        if request.form.get('username') == " " or request.form.get('password') == '':
            error = 'Credentials cannot be empty, please try again.'
        else:
            username = request.form.get('username')
            newuser = mycol.find_one({'username': username })
            print ("inserted username is: ", newuser )
            
            

    return render_template('login.html', error=error)
        





'''
    if request.method == "GET":
        return render_template('login.html', error=error)
    elif request.method == 'POST':
        if request.form.get('username') == " " or request.form.get('password') == " ":
            error = 'Credentials cannot be empty, please try again.' 
            return redirect(url_for('login'))
            
        else:
           def user():
                username = request.form.get('username')
                password = request.form.get('password')
                newuser = mycol.find_one_or_404({'username': username})
                print ("inserted username and password are: ", username, password )
'''



############## defining the routes for the different web pages END ##############




####################################################################################################
# running app in debug mode so that I can update the app.py without the need of manual restart
if __name__ == "__main__":
    app.run(debug=True) 