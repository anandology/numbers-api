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

@app.route("/sort", methods=["POST"])
def _sort():
    d = request.json
    result = sorted(d['numbers'])
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run()