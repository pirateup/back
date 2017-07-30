from flask import Flask, request, make_response
from back.pirateup.users.models import User

# random_string
import string
from random import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_cookie = request.cookies.get('user_cookie')
    if user_cookie == None:
        resp = make_response('Hello, World! You now have cookie!')
        # TODO(wojtek): Check if unique=True is good enaugh
        user = User(random_string())
        resp.set_cookie('user_cookie',user.cookie)

        return resp
    else:
        return 'Hello, World! You had cookie ' + user_cookie

def random_string():
    min_char = 8
    max_char = 12
    allchar = string.ascii_letters + string.punctuation + string.digits
    random_string = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return random_string

if __name__ == '__main__':
    app.run()