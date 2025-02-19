# server.py
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_keys():
    with open("public/keys.json", "r") as f:
        return json.load(f)

def save_keys(data):
    with open("public/keys.json", "w") as f:
        json.dump(data, f, indent=4)

@app.route("/verify", methods=["POST"])
def verify():
    data = load_keys()
    key = request.json.get("key")

    if key in data["unused_keys"]:
        data["unused_keys"].remove(key)
        data["used_keys"].append(key)
        save_keys(data)
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "invalid"}), 403

if __name__ == "__main__":
    app.run(debug=True)
