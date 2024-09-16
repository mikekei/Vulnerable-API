import sqlite3

conn = sqlite3.connect("vulns.db", check_same_thread=False)

def sqlinovuln():
    return "This is just a simple response"


def sqlivuln(sqli):
    username = sqli.get("username", "noprovided")
    password = sqli.get("password", "noprovided")

    if username and password:
        cur = conn.cursor()
        try:
            cur.execute(f"SELECT * FROM USERS WHERE USERNAME='{username}'")
            users = cur.fetchall()
        except Exception as e:
            return {"msg": f"{e}"}, 200
        return {"msg": f"Hello, {users}"}, 200
    else:
        return {"msg": f"Error"}, 400
    
# Function to dynamically generate the vulnerability functions
def create_dynamic_functions(num_replicas=1000):
    global_vars = globals()
    
    for i in range(1, num_replicas + 1):
        # Create dynamically named hhinovuln functions
        func_name_hhinovuln = f"sqlinovuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhinovuln] = sqlinovuln

        # Create dynamically named hhivuln functions
        func_name_hhivuln = f"sqlivuln_{i}"

        # Add the dynamically created function to the global scope
        global_vars[func_name_hhivuln] = sqlivuln

# Call the function to generate 1000 dynamic functions
create_dynamic_functions(num_replicas=1000)