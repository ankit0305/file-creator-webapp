from flask import Flask, render_template
app = Flask(__name__)

info=[
    {
        'name':'Ankit',
        'DOB':'02-Aug-1994',
        'city':'Bangalore'
    },
    {
        'name':'Ankur',
        'DOB':'02-Dec-1998',
        'city':'Jalandhar'
    }
]

@app.route("/")
def home():
    return render_template("home.html",values=info)

@app.route("/index")
def index():
    return "Hi I am index"

if __name__ == "__main__":
    app.run(debug=True)