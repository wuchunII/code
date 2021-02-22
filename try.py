from flask import Flask
from flask import request
from getCode import *
from data import d
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    env=request.args.get("env")
    phone=request.args.get("phone")
    print(type(env))
    print(type(phone))
    if env in ['dev', 'devtest', 'private']:

        code = get_verifyCode(phone, d[env][0], d[env][1], d[env][2], d[env][3])
    elif env == 'kdtest':
        print('kd')
        code = get_kd(phone)
    else:
        code = get_yunzhijiaT6(phone)
    print(code)
    return code
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')