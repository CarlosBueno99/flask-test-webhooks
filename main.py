from flask import Flask, request, jsonify
from datetime import datetime
import os
import json

app = Flask(__name__)


@app.route('/')
def index():
    dt = datetime.now()
    date_time = dt.strftime("%m/%d/%Y, %H:%M:%S")
    ticket_id = request.args.get('test')
    account_id = request.headers.get('X-Zendesk-Account-Id')
    webhook_id = request.headers.get('X-Zendesk-Webhook-Id')
    webhook_invocation_id = request.headers.get('X-Zendesk-Webhook-Invocation-Id')
    user_agent = request.headers.get('User-Agent')


    print(f'datetime_from_flask_server: {date_time}\nticket_id: {ticket_id}\naccount_id: {account_id}\nwebhook_id: {webhook_id}\nwebhook_invocation_id : {webhook_invocation_id}\nuser_agent: {user_agent}')

    


    return jsonify({
        "datetime_from_flask_server": date_time,
        "ticket_id": ticket_id,
        "account_id": account_id,
        "webhook_id": webhook_id,
        "webhook_invocation_id" : webhook_invocation_id,
        "user_agent": user_agent
    })



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
