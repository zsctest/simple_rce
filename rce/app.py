from flask import Flask,request
from flask import render_template
from utils import *

import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/first",methods=['GET'])
def first():
    return render_template("/views/first.html")

@app.route('/first',methods=['POST'])
def ping():
    ip_address = request.form['inputip']
    command = 'ping -c 3 %s'%ip_address
    status,output = subprocess.getstatusoutput(command)
    return render_template('/views/first.html', output=output)

@app.route("/second",methods=['GET'])
def second():
    return render_template("/views/second.html")

@app.route("/second",methods=['POST'])
def second2():
    status,output = ping2(request,filter_spaces)
    return render_template("/views/second.html",output=output,detail="空格")

@app.route("/third",methods=['GET'])
def third():
    return render_template("/views/third.html")


@app.route("/third",methods=['POST'])
def third2():
    status,output = ping2(request,double_quotation)
    return render_template("/views/third.html",output=output,detail="双引号")


@app.route("/fourth",methods=['GET'])
def fourth():
    return render_template('/views/fourth.html')

@app.route("/fourth",methods=['POST'])
def fourth2():
    status,output = ping2(request,single_quotation)
    return render_template("/views/fourth.html",output=output,detail="单引号")


@app.route("/fifth",methods=['GET'])
def fifth():
    return render_template('/views/fifth.html')

@app.route("/fifth",methods=['POST'])
def fifth2():
    status,output = curl(request,filter_quotation)
    return render_template("/views/fifth.html",output=output,detail="过滤引号")



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




if __name__  == "__main__":
    app.run(debug=True)