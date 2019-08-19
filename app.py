from flask import Flask, render_template

app = Flask(__name__) # creating an instalnce of the Flask class

@app.route("/")                             #defining the route for the index page
def index():                                #creating the function to return the index page
    return render_template("home.html")    #using a template and rendering the template


# running this app in debug mode so that I can update the app.py without the need of manual restart
if __name__ == "__main__":
    app.run(debug=True)