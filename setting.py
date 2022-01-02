import os
FLASK_SECRET_KEY = os.environ['FLASK_SECRET_KEY']

ALLOW_COR_ORIGINS = os.environ['ALLOW_COR_ORIGINS']

USERS = {os.environ['MAIL_USER_1']:os.environ['MAIL_PASS_1']}

SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']