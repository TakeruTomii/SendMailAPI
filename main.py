import setting
from service import sg
from flask import Flask, jsonify, request, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from flask_httpauth import HTTPAuth, HTTPBasicAuth


app = Flask(__name__)
app.secret_key = setting.FLASK_SECRET_KEY

limiter = Limiter(app, key_func=get_remote_address, default_limits=["10 per minute"])
CORS(app, origins=setting.ALLOW_COR_ORIGINS)
auth = HTTPBasicAuth()
users = setting.USERS
app.config['CORS_HEADERS'] = 'Content-Type'

# SendGrid
@app.route("/sendmail", methods=['POST'])
@limiter.limit("10 per minute")
@auth.login_required()
def sendmail():
  service = sg.mailUtil()
  res = service.send_inquiry(request)

  return jsonify(res['message']), res['statusCode']

# Basic Authentication
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
