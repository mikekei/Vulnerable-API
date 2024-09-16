from flask import Flask, request, jsonify

from hhi import create_dynamic_functions1
from ssti import create_dynamic_functions5
from xss import create_dynamic_functions6
from sqli import create_dynamic_functions4
from rfi import create_dynamic_functions3
from lfi import create_dynamic_functions2

# Dynamically creating functions for each vulnerability replica

create_dynamic_functions5(num_replicas=500, g=globals())
create_dynamic_functions1(num_replicas=500, g=globals())
create_dynamic_functions2(num_replicas=500, g=globals())
create_dynamic_functions3(num_replicas=500, g=globals())
create_dynamic_functions4(num_replicas=500, g=globals())
create_dynamic_functions6(num_replicas=500, g=globals())
app = Flask(__name__)

# Define the parameters and vulnerability names
vulnerabilities_info = {
    'xss': 'username',
    'lfi': 'filename',
    'rfi': 'imagelink',
    'hhi': 'email',
    'ssti': 'mathexp',
    'sqli': 'username'
}

# Register routes for each vulnerability replica
for vuln, param in vulnerabilities_info.items():
    for i in range(1, 501):
        func_name = f"{vuln}vuln_{i}"
        func = globals().get(func_name, None)
        
        if func:
            methods = ['GET'] if 'novuln' in func_name else ['POST']
            app.add_url_rule(f'/api/{vuln}vuln_{i}', view_func=func, methods=methods)
        else:
            print(f"Function {func_name} not found in globals")

# Main index route listing all vulnerability types
@app.route('/index.html', methods=['GET'])
def index():
    links = []
    for vuln in vulnerabilities_info.keys():
        links.append(f"""
        <h2>{vuln.upper()} Vulnerability</h2>
        <a href="/api/{vuln}vuln">Go to {vuln.upper()} Forms</a><br>
        """)
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Vulnerable Flask Application Index</title>
    </head>
    <body>
        <h1>Vulnerable Flask Application</h1>
        {''.join(links)}
    </body>
    </html>
    """, 200

# Vulnerability-specific page showing 500 dynamic forms
@app.route('/api/<vuln>vuln', methods=['GET'])
def list_vuln_forms(vuln):
    if vuln not in vulnerabilities_info:
        return "Invalid vulnerability type", 400

    param = vulnerabilities_info[vuln]
    forms = []
    
    for i in range(1, 501):
        form_action = f"/api/{vuln}vuln_{i}"
        forms.append(f"""
        <form action="{form_action}" method="POST">
            <label for="{param}_{i}">Enter {param} (Replica {i}):</label>
            <input type="text" id="{param}_{i}" name="{param}">
            <button type="submit">Submit Replica {i}</button>
        </form><br>
        """)

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{vuln.upper()} Vulnerability Forms</title>
    </head>
    <body>
        <h1>{vuln.upper()} Vulnerability - 500 Forms</h1>
        {''.join(forms)}
        <br><br>
        <a href="/index.html">Back to Index</a>
    </body>
    </html>
    """, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, threaded=True)
