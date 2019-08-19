from flask import Flask, render_template
from data import Articles

Articles = Articles()

app = Flask(__name__) # creating an instalnce of the Flask class

####### defining the routes for the different web pages START #######
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    return render_template("articles.html", articles = Articles)

@app.route('/list_article/<string:id>/')
def article(id):
    return render_template('list_article.html', id = id)



####################################################################################################
# running this app in debug mode so that I can update the app.py without the need of manual restart
if __name__ == "__main__":
    app.run(debug=True)