from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/test')
def test():
    return jsonify({
        "request_id": "test_id",
        "request_user_id": "test_user_id",
        "converted_text": "this is the test response message."
    })


if __name__ == '__main__':
    app.run(debug=True)



