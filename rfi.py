import requests

def fetchimage(name):
    try:
        file = requests.get(url=name, timeout=2, verify=False).text
    except:
        file = ""
    return file

def rfinovuln():
    return f"This is just a simple image"
from flask import Flask, request
def rfivuln():
    filename = request.form.get("imagelink", "http://google.com")

    if filename:
        return {"msg": f"response, {fetchimage(filename)}"}, 200
    else:
        return {"msg": f"Error"}, 400


# Function to dynamically generate the vulnerability functions
def create_dynamic_functions3(num_replicas=1000, g=None):
    global_vars = g
    
    for i in range(1, num_replicas + 1):
        # Create dynamically named hhinovuln functions
        func_name_hhinovuln = f"rfinovuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhinovuln] = rfinovuln

        # Create dynamically named hhivuln functions
        func_name_hhivuln = f"rfivuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhivuln] = rfivuln
