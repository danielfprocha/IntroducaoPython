from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "API funcionando"})

@app.route("/sensores/clima")
def clima():
    return jsonify({"leituras": [], "total_registros": 0})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)