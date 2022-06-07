from __init__ import app
from flask import Flask, render_template, request

from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/password')
def password():
    return render_template("password.html")


@app.route('/findyour/', methods=['GET', 'POST'])
def findyour():
    if request.form:
        input = request.form.get("lname")
        print("works")
        if len("input") != 0:
            return render_template("findyour.html", input=input)
    return render_template("findyour.html")

if __name__ == "__main__":
    app.run(debug=True)