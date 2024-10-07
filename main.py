from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with Python format placeholders
html_template = """                                                                                                                                                        
<!DOCTYPE html>                                                                                                                                                            
<html lang="en">                                                                                                                                                           
<head>                                                                                                                                                                     
    <meta charset="UTF-8">                                                                                                                                                 
    <meta name="viewport" content="width=device-width, initial-scale=1.0">                                                                                                 
    <title>SSTI Demo (Upgraded)</title>                                                                                                                                               
</head>                                                                                                                                                                    
<body style="font-family: Arial, sans-serif; background-color: #f0f8ff; color: #333; padding: 20px; margin: 0;">                                                                                                                                                                          
    <h1 style="text-align: center; color: #4A90E2;">Server-Side Template Injection Demo (Revamped) (Now with CSS!)</h1>                                                                                                                           
    <form method="GET" action="/greet" style="max-width: 400px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; background-color: #fff;">                                                                                                                                            
        <label for="name" style="font-weight: bold; margin-bottom: 10px; display: block;">This time it's a bit harder. Enter your name:</label>                                                                                                                         
        <input type="text" id="name" name="name" required style="width: 100%; padding: 0px; height: 2em; margin-bottom: 10px; border: 1px solid #ccc; border-radius: 4px;">                                                                                                                 
        <button type="submit" style="width: 100%; padding: 10px; border: none; border-radius: 4px; background-color: #4A90E2; color: white; font-size: 16px; cursor: pointer;">Greet</button>                                                                                                                               
    </form>                                                                                                                                                                
    <div style="text-align: center; margin-top: 20px;">{greeting}</div>
    <a href="https://github.com/UMD-CSEC/ssti_demo_revamped">Source</a>
</body>                                                                                                                                                                    
</html>                                                                                                                                                                    
"""

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')

    if not name:
        greeting = "<p>Please enter a name.</p>"
    else:
        greeting = f"<p>Hello, {name}!</p>"  # This is the vulnerable part

    blacklist = ["_", "globals", "builtins", "."]
    for b in blacklist:
        if b in name:
            greeting = f"<code>blacklist: {blacklist}</code>"

    return render_template_string(html_template.format(greeting=greeting))

@app.route('/')
def index():
    return render_template_string(html_template.format(greeting=""))

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
