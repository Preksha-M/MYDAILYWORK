from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        a = float(request.form["num1"])
        b = float(request.form["num2"])
        op = request.form["op"]

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b

    return render_template("index.html", result=result)

app.run(debug=True)
