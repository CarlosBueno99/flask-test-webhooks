from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)


@app.route('/')
def index():
    dt = datetime.now()
    ticket_id = request.args.get('test')

    print(f'this ran at {dt} and from this ticket {ticket_id}')
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
