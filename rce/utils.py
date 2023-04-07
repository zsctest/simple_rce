import re
import subprocess
import os

class StringFilter:
    def __init__(self, filter_func):
        self.filter_func = filter_func

    def filter(self, string):
        return self.filter_func(string)


def filter_spaces(string):
    #过滤空格
    # filtered_string = re.sub(r'\s', '', string)
    return string.replace(" ", "")

def double_quotation(string):
    #用双引号包含输入
    return "\"%s\""%string

def single_quotation(string):
    #用单引号包含输入
    return "\'%s\'"%string

def filter_quotation(string):
    #过滤双引号和单引号，同时用双引号包裹输入
    string = string.replace("\"","").replace("\'","")
    return "\"%s\""%string


def ping2(request,rule):
    ip_address = request.form['inputip']
    new_address = StringFilter(rule).filter(ip_address)
    command = 'ping -c 3 %s'%new_address
    print("输入：",command)
    return subprocess.getstatusoutput(command)

def ping3(request,rule):
    ip_address = request.form['inputip']
    new_address = StringFilter(rule).filter(ip_address)
    command = 'ping -c 3 %s'%new_address
    print("输入：",command)
    return subprocess.getstatusoutput(command)

def curl(request,rule):
    target = request.form['inputip']
    filtered_target = StringFilter(rule).filter(target)
    command = 'curl %s'%filtered_target
    print("输入：",command)
    return subprocess.getstatusoutput(command)

def is_valid_hostname(hostname):
    #主机名是否合法
    try:
        socket.gethostbyname(hostname)
    except socket.error:
        return False
    return True

# def validHostname(request,rule):
#     ip_address = request.form['inputip']
#     if not is_valid_hostname(ip_address):
#         return render_template('/views/error.html', error='Invalid hostname')

# filter = StringFilter(filter_spaces)
# filtered_string = filter.filter("hello world")
# print(filtered_string)
