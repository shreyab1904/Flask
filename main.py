from flask import Flask

app =  Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my website"

@app.route("/contact")
def Contact_page():
    return "Contact Page"

if __name__ == "__main__":
    app.run()