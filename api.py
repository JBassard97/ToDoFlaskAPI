from flask import Flask, request, jsonify

app = Flask(__name__)

data = {"message": "Hello, World!"}


@app.route("/api", methods=["GET"])
def get_data():
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
