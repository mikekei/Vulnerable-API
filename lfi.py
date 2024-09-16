def fetchfile(name):
    try:
        file = open(name).read()
    except:
        file = ""
    return file

def lfinovuln():
    return f"This is just a simple response {fetchfile('req.txt')}"


def lfivuln(lfi):
    filename = lfi.get("filename", "readme.txt")

    if filename:
        return {"msg": f"response, {fetchfile(filename)}" }, 200
    else:
        return {"msg": f"Error"} , 400

# Function to dynamically generate the vulnerability functions
def create_dynamic_functions(num_replicas=1000):
    global_vars = globals()
    
    for i in range(1, num_replicas + 1):
        # Create dynamically named hhinovuln functions
        func_name_hhinovuln = f"lfinovuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhinovuln] = lfinovuln

        # Create dynamically named hhivuln functions
        func_name_hhivuln = f"lfivuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhivuln] = lfivuln

# Call the function to generate 1000 dynamic functions
create_dynamic_functions(num_replicas=1000)
