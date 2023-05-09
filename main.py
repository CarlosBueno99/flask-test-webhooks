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
    internal_zendesk_endpoint_api = f'https://[you-subdomain].zendesk.com/api/v2/webhooks/{webhook_id}/invocations/{webhook_invocation_id}/attempts'
    invocation_ui_URL = f'https://[you-subdomain].zendesk.com/admin/apps-integrations/webhooks/webhooks/{webhook_id}/activity/{webhook_invocation_id}'
    body = request.json

    print('=-=-=-=-=-=-=-=-=-=-=-= New request =-=-=-=-=-=-=-=-=-=-=-=')
    print(f'datetime_from_flask_server: {date_time}\nticket_id: {ticket_id}\naccount_id: {account_id}\nwebhook_id: {webhook_id}\nwebhook_invocation_id : {webhook_invocation_id}\nuser_agent: {user_agent}\nui_endpoint: {invocation_ui_URL}\napi_endpoint: {internal_zendesk_endpoint_api}\n request_body: {body}')

    


    return jsonify({
        "datetime_from_flask_server": date_time,
        "ticket_id": ticket_id,
        "account_id": account_id,
        "webhook_id": webhook_id,
        "webhook_invocation_id" : webhook_invocation_id,
        "user_agent": user_agent,
        "ui_endpoint": invocation_ui_URL,
        "api_endpoint": internal_zendesk_endpoint_api,
        "request_body": body
    })



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
