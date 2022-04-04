from flask import Flask, render_template

app =  Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>WELCOME</h1>"

@app.route("/contact")
def Contact_page():
    return render_template("contact.html")

@app.route("/home")
def HomePage():
    return "Home Page"

@app.route("/gallery")
def gallery():
    return "Insert your pictures"


if __name__ == "__main__":
    app.run()