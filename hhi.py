from flask import Flask, request

app = Flask(__name__)

# The original view functions
def hhinovuln():
    return "This is hhi no vuln"

def hhivuln():
    headerss = request.headers
    print(f"headers: {headerss}")
    
    try:
        h = headerss["Host"]
    except Exception as e:
        print(f"failed: {e}")
        h = "temo.com"

    if headerss:
        return f"response, <a href='{h}'>", 200
    else:
        return {"msg": "failed"}, 400

# Function to dynamically generate the vulnerability functions
def create_dynamic_functions1(num_replicas=1000, g=None):
    global_vars = g
    
    for i in range(1, num_replicas + 1):
        # Create dynamically named hhinovuln functions
        func_name_hhinovuln = f"hhinovuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhinovuln] = hhinovuln

        # Create dynamically named hhivuln functions
        func_name_hhivuln = f"hhivuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhivuln] = hhivuln

