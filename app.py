import os
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/api/key")
def get_key():
    # La API key de Anthropic se guarda como variable de entorno en Render
    # NUNCA la pongas hardcodeada aqui
    return jsonify({"key": os.environ.get("ANTHROPIC_API_KEY", "")})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
