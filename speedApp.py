from flask import Flask, jsonify
from flask_cors import CORS
from speed import get_result

app = Flask(__name__)
CORS(app)


@app.route("/test")
def test():
    result = get_result()
    return jsonify(result)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
