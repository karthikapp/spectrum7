from flask import Flask, render_template
from flask import render_template
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
mail = Mail(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/datascience")
def datascience():
    return render_template('datascience.html')

@app.route("/oracle")
def oracle():
    return render_template('oracle.html')

@app.route("/it_infra")
def it_infra():
    return render_template('it_infra.html')

@app.route("/iot")
def iot():
    return render_template('iot.html')

if __name__ == "__main__":
    app.run()