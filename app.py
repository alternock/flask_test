from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)   
cors = CORS(app)

@app.route("/persona", methods=["GET"])
def personas():
    persona = {
        "email":"foo@foo.com",
        "name":"fookziman",
        "alias":"foo"
    }
    return jsonify(persona)
    
if __name__ == "__main__":
    app.run(debug=True,port=5000)
