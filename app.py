from flask import Flask, jsonify

app = Flask(__name__)

def paridad(n: int) -> str:
    return "par" if n % 2 == 0 else "impar"

def factorial(n: int) -> int:
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

@app.get("/<int:n>")
def compute(n: int):

    result = {
        "number": n,
        "factorial": factorial(n),
        "paridad": paridad(n)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)