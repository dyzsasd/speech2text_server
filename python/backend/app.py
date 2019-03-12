from flask import Flask, jsonify


api = Flask(__name__)


@api.route('/test')
def test():
    return jsonify({
        "request_id": "test_id",
        "request_user_id": "test_user_id",
        "converted_text": "this is the test response message."
    })


if __name__ == '__main__':
    api.run(debug=True)



