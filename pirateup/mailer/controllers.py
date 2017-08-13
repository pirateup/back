from back.pirateup.mailer.models import send_mail
from back.config import Config

MAILER_SMTP = Config.MAILER_SMTP
MAIL_SECRET_KEY = Config.MAIL_SECRET_KEY
MAILER_PORT = Config.MAILER_PORT

# example
# send_mail(TO, FROM, MSG, SUBJECT, MAILER_SMTP, MAIL_SECRET_KEY, MAILER_PORT=MAILER_PORT)