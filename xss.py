
def novuln():
    return "This is just a simple response"

from flask import Flask, request
def xssvuln():
    username = request.form.get("username", "noprovided")

    if username:
        return {"msg": f"Hello, {username}"}, 200
    else:
        return {"msg": f"Error"}, 400

# Function to dynamically generate the vulnerability functions
def create_dynamic_functions6(num_replicas=1000, g=None):
    global_vars = g
    
    for i in range(1, num_replicas + 1):
        # Create dynamically named hhinovuln functions
        func_name_hhinovuln = f"novuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhinovuln] = novuln

        # Create dynamically named hhivuln functions
        func_name_hhivuln = f"xssvuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhivuln] = xssvuln
