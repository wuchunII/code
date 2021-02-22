import re
import requests
def filter_u_code(string):
	u_codes = re.findall(r'(\\u\w{4})',string)
	print(u_codes)
	for u_code in u_codes:
		print(u_code.encode('utf-8').decode('unicode_escape'))
		string = string.replace(u_code,u_code.encode("utf-8").decode("unicode_escape"))
	return string
def get_verifyCode(mobile,username,pwd,loginurl,smsSendurl):
    s = requests.session()
    r = s.post(loginurl,
               data={"username": username, "password": pwd}, verify=False)
    print(r.text)
    print('aaa===============')
    if r'超过90天未登录的用户' in r.text:
        return r'系统登录不上，请联系后台'
    r = s.post(smsSendurl,data={"startTime": "", "endTime": "", "mobile": mobile}, verify=False)
    print(r'==============')
    print(r.text)
    p = r'您的验证码为：(\d+)'
    pat=re.compile(p)
    print(pat)
    m=re.search(pat,r.text)
    if not  m:
        p = r'您的验证码为:(\d+)'
        pat = re.compile(p)
        m = re.search(pat, r.text)
    print(m)
    if m:
        num=m.group(1)
    else:
        return "没收到消息，请确认有发送"
    p = r'\d{4}-\d{2}-\d{2}'
    pat = re.compile(p)
    date=re.findall(pat,r.text)[0]+" "
    p=r'\d{2}:\d{2}:\d{2}'
    pat = re.compile(p)
    print(re.findall(pat,r.text))
    return date+re.findall(pat,r.text)[0]+"  "+num

def get_yunzhijiaT6(mobile):

    he={'Referer':"http://op.kdweibo.cn/sms/",
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'X - Requested - With': 'XMLHttpRequest'
        }

    f=requests.get(r'http://op.kdweibo.cn/sms/search/get/?arg='+str(mobile)+'&env=prod',headers=he)
    print(f.json())
    p = r'您的验证码为：(\d+)'
    pat = re.compile(p)
    m = re.search(pat, f.json()['result'])
    if not  m:
        p = r'您的验证码为:(\d+)'
        pat = re.compile(p)
        m = re.search(pat, f.json()['result'])
    if m:
        num=m.group(1)
    else:
        return "没收到消息，请确认有发送"
    p = r'\d{4}-\d{2}-\d{2}'
    pat = re.compile(p)
    date = re.findall(pat, f.text)[0] + " "
    p = r'\d{2}:\d{2}:\d{2}'
    pat = re.compile(p)
    return date+re.findall(pat, f.text)[0] + "  " + num
def get_kd(mobile):

    he={'Referer':"http://op.kdweibo.cn/sms/","User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'X - Requested - With': 'XMLHttpRequest'
        }
    f=requests.get(r'http://op.kdweibo.cn/sms/search/get/?arg='+str(mobile)+'&env=test',headers=he)
    print(f.content.decode('utf-8'))

    result=filter_u_code(f.json()['result'])
    print(result)
    p = r'您的验证码为:(\d+)，'
    pat = re.compile(p)
    m = re.search(pat, result)
    if not  m:
        p = r'您的验证码为：(\d+)'
        pat = re.compile(p)
        m = re.search(pat, result)
    if m:
        num=m.group(1)
    else:
        return "没收到消息，请确认有发送"
    p = r'\d{4}-\d{2}-\d{2}'

    pat = re.compile(p)
    date = re.findall(pat, f.text)[0] + " "
    p = r'\d{2}:\d{2}:\d{2}'
    pat = re.compile(p)
    return date+re.findall(pat, f.text)[0] + "  " + num

# print(get_yunzhijiaT6(17258240120))
# print(get_kd(17258240120))
# print(get_verifyCode(17258240120,13751015923,"123456",r'https://dev.kdweibo.cn/innermanage/login',r'https://dev.kdweibo.cn/innermanage/sms/smsSendDetail?_menu_=smsSendDetail'))  dev
# print(get_verifyCode(17258240120,19924538057,"Kingdee@1024",r'https://drillb6.kdweibo.cn/innermanage/login',r'https://drillb6.kdweibo.cn/innermanage/sms/smsSendDetail?_menu_=smsSendDetail')) T6
# print(get_verifyCode(17258240120,15920594742,"a123456@",r'https://devtest.kdweibo.cn/innermanage/login',r'https://devtest.kdweibo.cn/innermanage/sms/smsSendDetail?_menu_=smsSendDetail'))  devtest
# print(get_verifyCode(17258240120,17223232323,"aaa@1234",r'https://private.kdweibo.cn/innermanage/login',r'https://private.kdweibo.cn/innermanage/sms/smsSendDetail?_menu_=smsSendDetail')) private