from flask import Flask, request, make_response, jsonify
import numb

app = Flask(__name__)

def get_int_param(name, default=None):
    value = request.args.get(name)
    if value:
        try:
            return int(value)
        except ValueError:
            pass
    return default

def text_response(value):
    if isinstance(value, str):
        text = value
    elif hasattr(value, "__iter__"):
        text = "\n".join(str(v) for v in value)
    else:
        text = str(value)

    if not text.endswith("\n"):
        text += "\n"

    response = make_response(text, 200)
    response.mimetype = "text/plain"
    return response

HOME = """
<!doctype html>
<html>
<head>
  <title>Numbers API</title>
  <style type="text/css">

  </style>
</head>
<body>
    <h1>Numbers API</h1>
    <p>
    Simple API to work with numbers.
    </p>

    <h2>Add</h2>
    <p>API to add two numbers.<p>

    <p>Example:</p>
    <a href="/add?a=3&b=4">/add?a=3&b=4</a>

    <h2>Fibs</h2>

    <p>Generates fibonacci numbers.</p>

    <a href="/fibs?a=3&b=4&n=10">/fibs?a=3&b=4&n=10</a>

    <h2>Documentation</h2>
    <p>
    See <a href="https://github.com/anandology/numbers-api">Github repo</a> to know more details about the API.
    </p>
</body>
</html>
"""

@app.route("/")
def home():
    return HOME

@app.route("/add")
def add():
    """Adds two numbers.
    """
    a = get_int_param("a", 0)
    b = get_int_param("b", 0)
    result = a + b
    return text_response(result)

@app.route("/fibs")
def fibs():
    """Returns a sequence of fibonacci numbers.
    """
    a = get_int_param("a", 1)
    b = get_int_param("b", 1)
    n = get_int_param("n", 10)
    numbers = numb.fibs(a, b, n)
    return text_response(numbers)

@app.route("/product", methods=["POST"])
def product():
    d = request.json
    result = numb.product(d['numbers'])
    return jsonify({"result": result})

@app.route("/range", methods=["POST"])
def _range():
    d = request.json
    start = d.get("start", 0)
    stop = d.get("stop", 0)
    step = d.get("step", 1)

    result = list(range(start, stop, step))
    return jsonify({"result": result})

@app.route("/sort", methods=["POST"])
def _sort():
    d = request.json
    result = sorted(d['numbers'])
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run()