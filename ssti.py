from flask import request
from jinja2 import Template

def sstinovuln():
    return f"This is ssti no vuln, 49"

from flask import Flask, request
def sstivuln():
    exp = request.form.get("mathexp", "test")
    test = Template("my temp: " + exp)
    if exp:
        return f"{test.render()}", 200
    else:
        return {"msg": f"Error"}, 400

# Function to dynamically generate the vulnerability functions
def create_dynamic_functions5(num_replicas=1000, g=None):
    global_vars = g
    
    for i in range(1, num_replicas + 1):
        # Create dynamically named hhinovuln functions
        func_name_hhinovuln = f"sstinovuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhinovuln] = sstinovuln

        # Create dynamically named hhivuln functions
        func_name_hhivuln = f"sstivuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhivuln] = sstivuln
