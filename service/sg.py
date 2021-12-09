from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import re

import setting


class mailUtil():
    def send_inquiry(self, req):
        # content of mail
        content = mailContent()

        content.mail_from = req.json['mail_from']
        content.mail_to = req.json['mail_to']
        content.title = req.json['title']
        content.msg = req.json['message']

        # Validate mail content
        isValid = self.isValidMailContent(content)
        if not isValid :
            return {
                'statusCode': 400,
                'message':"Invalid Request"
            }

        # Compose mail content
        message = Mail(
            from_email=content.mail_from,
            to_emails=content.mail_to,
            subject=content.title,
            html_content=content.msg)

        # Call SendGrid API
        sg = SendGridAPIClient(setting.SENDGRID_API_KEY)
        try:
            response = sg.send(message)
            if response.status_code == 202:
                return {
                    'statusCode': 200,
                    'message': 'Sent mail successfully'
                }
            else:
                return {
                    'statusCode': response.status_code,
                    'message': response.body
                }
        except Exception as e:
            return {
                    'statusCode': 500,
                    'message': e.message
                }

    # validate mail content
    def isValidMailContent(self, content):
        pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        # mail_from must be email address format
        if re.match(pattern, content.mail_from) is None:
            return False

        # mail_to must be email address format
        if re.match(pattern, content.mail_to) is None:
            return False

        # title must be string
        if type(content.title) is not str:
            return False

        # msg must be string
        if type(content.msg) is not str:
            return False

        return True


class mailContent:
    pass

