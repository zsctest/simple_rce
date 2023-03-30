from flask import Flask,request
from flask import render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/first",methods=['GET'])
def first():
    return render_template("first.html")

@app.route('/first',methods=['POST'])
def ping():
    ip_address = request.form['inputip']
    command = 'ping -c 3 %s'%ip_address
    status,output = subprocess.getstatusoutput(command)
    return render_template('first.html', output=output)

@app.route("/second")
def second():
    return render_template("second.html")

@app.route("/third")
def third():
    return render_template("third.html")




if __name__  == "__main__":
    app.run(debug=True)