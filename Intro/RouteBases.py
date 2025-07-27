from flask import Flask, request # type: ignore

app = Flask(__file__)

@app.route("/")
def Home():
    return "Welcome to the Home Page! Use /calculate with 's' and 'n' parameters."

def convert_base(s, n):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" # Max Base 62
    value = 0

    if n < 2 or n > len(digits):
        return f"Please provide a base between 2 and {len(digits)}"
    
    for char in s:
        cur_digit = digits.index(char) # Which place char is in digits
        if cur_digit >= n: # If out of range of base n
            return f"String has character {char} out of base {n}"
        value = value*n + cur_digit
        
    return value

@app.route("/calculate")
def calculate():
    s = request.args.get("s", None)
    n = request.args.get("n", None)
    if s is None or n is None:
        return "Missing 's' or 'n' parameters"
    # Cheat method
    # else:
    #    return str(int(s, int(n)))
    else: return str(convert_base(s, int(n)))
    
app.run(debug=True)