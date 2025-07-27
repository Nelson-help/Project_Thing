from flask import Flask, request # type: ignore

app = Flask(__file__) # Create a Flask application from the current file

# For example
# https://      www.youtube.com     /watch      ?v=Cr0nwCYDJNE              &
#     ^ secure  ^ domain             ^ route    ^ parameters (at the end)   ^ more params

@app.route("/")  # Decorator
def Home(): # route handler
    print(request.args.get("v", None)) # Print the query parameters from the request
    return "Hello, World!"
    
@app.route("/watch")  # Decorator
def watch(): # route handler
    return {"data": 123}

app.run(debug=True)  # Run the Flask application with debug mode enabled