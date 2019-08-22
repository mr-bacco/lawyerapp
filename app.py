from flask import Flask, render_template, url_for, request, session, redirect
from data import Items
import pymongo

Items = Items()

app = Flask(__name__) # creating an instalnce of the Flask class

############## db SETUP START ##############
'''using mongo db cloud version'''
# checking the connection to cloud ongodb and printing in the console the list of collections under the database
myclient = pymongo.MongoClient("mongodb://mrbacco:mongodb001@cluster0-shard-00-00-goutv.mongodb.net:27017,cluster0-shard-00-01-goutv.mongodb.net:27017,cluster0-shard-00-02-goutv.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = myclient["database001"]
print(mydb.list_collection_names())

############## db SETUP ENDS ##############



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



####################################################################################################
# running this app in debug mode so that I can update the app.py without the need of manual restart
if __name__ == "__main__":
    app.run(debug=True)
    