import logging
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(TO, FROM, MSG, SUBJECT, MAILER_SMTP, MAIL_SECRET_KEY, MAILER_PORT=587):
    msg = MIMEMultipart()
    msg['From'] = FROM
    msg['To'] = TO
    msg['Subject'] = SUBJECT
    body = MSG
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()



    try:
        with smtplib.SMTP(MAILER_SMTP, MAILER_PORT) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            # https://myaccount.google.com/apppasswords
            s.login(FROM, MAIL_SECRET_KEY)
            s.sendmail(FROM, TO, text)
            s.close()
        logging.info("Email sent!")
    except:
        logging.warning("Unable to send the email. Error: ", sys.exc_info()[0])
        raise
