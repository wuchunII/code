import requests
import re
import PySimpleGUI as ps
import PySimpleGUI as sg
from data import d
from getCode import *
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import *
import threading
import os
import webbrowser
class window():
    def __init__(self):
        envs=['正式','kdtest','dev','devtest','private',"T6"]

        self.t=Tk()
        self.t.geometry('480x400')
        self.t.title('测试小工具,有问题请联系质量部吴椿')
        self.fun1Label = Label(text="获取验证码功能------------------")
        self.mobileLabel=Label(self.t,text="请输入电话号码： ")
        self.mobile=Entry(self.t)
        self.getCodeButton=Button(self.t,text='获取验证码',command=self.getCode)
        self.variable = StringVar(self.t)
        self.variable.set("dev")  # default value
        self.envsChooseLabel=Label(text="请选择环境： ")
        self.envsChoose= OptionMenu(self.t, self.variable, *envs)

        # self.fun2Label=Label(text="注册用户功能-------------")
        # self.registMobileLable=Label(text='要注册的用户电话')
        # self.pwdLable =Label(text='要注册的用户密码')
        # self.registMobile = Entry()
        # self.pwd=Entry()
        # self.registenvsChooseLabel = Label(text="请选择环境： ")
        # self.registvariable = StringVar(self.t)
        # self.registvariable.set("dev")  # default value
        # self.registenvsChoose = OptionMenu(self.t, self.registvariable, *envs)
        # self.registButton=Button(text="注册",command=self.regist)

        self.fun2Label = Label(text="下载最新客户端功能-------------")
        self.winButton=Button(text="下载最新的公有云测试win包",command=self.winDown)
        self.macButton = Button(text="下载最新的公有云测试mac包",command=self.macDown)
        self.privateButton = Button(text="下载private客户端",command=self.privateOpen)
        self.t6Button = Button(text="下载T6客户端",command=self.t6Open)

        self.fun3Label = Label(text="注册用户功能--------------------")
        self.managerMobileLable = Label(text='请输入管理员电话')
        self.managerMobile = Entry()
        self.managerEidLable = Label(text='请输入管理员所在圈子eid')
        self.managerEid = Entry()
        self.registenvsChooseLabel = Label(text="请选择环境： ")
        self.registvariable = StringVar(self.t)
        self.registvariable.set("dev")  # default value
        self.registenvsChoose = OptionMenu(self.t, self.registvariable, *envs)
        self.memberEidLable = Label(text='请注册成员的电话')
        self.memberMobile = Entry()
        self.registButton = Button(text="确认", command=self.regist)

        self.fun3Label=Label(text='管理和运行jmeter自动化脚本---')
        self.t6scriptButton=Button(text="管理t6脚本", command=self.t6sciprt)
        self.kdscriptButton = Button(text="管理kd脚本", command=self.kdscript)
        self.jenkinsButton=Button(text="jenkins运行脚本", command=self.jenkins)


        self.fun1Label.grid(row=0,column=0)
        self.mobileLabel.grid(row=1,column=0)
        self.mobile.grid(row=1,column=1)
        self.envsChooseLabel.grid(row=2,column=0)
        self.envsChoose.grid(row=2,column=1)
        self.getCodeButton.grid(row=3,column=0)


        self.fun2Label.grid(row=4, column=0)
        self.winButton.grid(row=5, column=0)
        self.macButton.grid(row=5, column=1)
        self.privateButton.grid(row=6, column=0)
        self.t6Button.grid(row=6, column=1)

        self.fun3Label.grid(row=7, column=0)
        self.t6scriptButton.grid(row=8, column=0)
        self.kdscriptButton.grid(row=8, column=1)
        self.jenkinsButton.grid(row=9, column=0)


        # self.fun3Label.grid(row=7, column=0)
        # self.managerMobileLable.grid(row=8, column=0)
        # self.managerMobile.grid(row=8, column=1)
        # self.managerEidLable.grid(row=9, column=0)
        # self.managerEid.grid(row=9, column=1)
        # self.registenvsChooseLabel.grid(row=10, column=0)
        # self.registenvsChoose.grid(row=10, column=1)
        # self.memberEidLable.grid(row=11, column=0)
        # self.memberMobile.grid(row=11, column=1)
        # self.registButton.grid(row=12, column=0)
        self.t.mainloop()
    def t6sciprt(self):
        webbrowser.open('http://172.20.200.203:5002')
    def kdscript(self):
        pass
    def jenkins(self):
        webbrowser.open('http://172.20.200.203:8080')
    def regist(self):
        manage=self.managerMobile.get()
        eid=self.managerEid.get()
        env=self.registvariable.get()
        member=self.memberMobile.get()
        print(manage)
        print(env)
        if env in ['dev','devtest','private']:

            code=get_verifyCode(manage,d[env][0],d[env][1],d[env][2],d[env][3])
        elif env=='kdtest':
            print('kd')
            code=get_kd(manage)
        else:
            code=get_yunzhijiaT6(manage)
        code=code[-4:]
        r=requests.session()
        r.get(r'https://kdtest.kdweibo.cn/space/c/rest/user/loginByVerifyCode HTTP/1.1')


    def privateOpen(self):
        webbrowser.open(r'https://yunzhijia.com/home/saas/private/beta/')
    def t6Open(self):
        webbrowser.open(r'https://yunzhijia.com/home/saas/drillb6/beta/')
    # def getPrivateDownUrl(self,type): #获取302链接
    #     if type=='win':
    #         url=r'https://yunzhijia.com/public/download?type=sop&platform=mac&id=private&tag=beta'
    #     else:
    #         url=r'https://yunzhijia.com/public/download?type=sop&platform=win&id=private&tag=beta'
    #     f=requests.get(url)
    #     print(f.headers['Location'])
    def getCode(self):
        env=self.variable.get()
        mobile=self.mobile.get()
        if not mobile:
            tkinter.messagebox.showinfo("请输入电话号码","请输入电话号码")
            return
        if env in ['dev','devtest','private']:
            code=get_verifyCode(mobile,d[env][0],d[env][1],d[env][2],d[env][3])
        elif env=='kdtest':
            code=get_kd(mobile)
        else:
            code=get_yunzhijiaT6(mobile)
        tkinter.messagebox.showinfo("验证码",code)
    # def regist(self):
    #     default_dir = r"文件路径"
    #
    #     file_path = askdirectory(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
    #     print(file_path)
    #     mobile=self.registMobile.get()
    #     pwd=self.pwd.get()
    #     registenv=self.registvariable.get()
        # tkinter.messagebox.showinfo('',mobile+pwd+registenv)
    def winDown(self):

        file_path = askdirectory (title=u'下载最新的公有云win包到')
        version=self.getMaxVersion()

        dirUrl=r'http://desktop.yzjop.com/res/CloudHub/feature/'+version+'/win/'
        packageName=self.getWinDownUrl(dirUrl)
        print('package',packageName)
        url=dirUrl+packageName
        self.download(url,file_path,packageName)
    def macDown(self):
        file_path = askdirectory(title=u'下载最新的公有云mac包到')
        version = self.getMaxVersion()
        print('version ',version)
        dirUrl = r'http://desktop.yzjop.com/res/CloudHub/feature/'+version+'/mac/'
        print('dirurl',dirUrl)
        packageName = self.getMacDownUrl(dirUrl)
        print('package',packageName)
        url = dirUrl + packageName
        self.download(url, file_path,packageName)
    def getMaxVersion(self):
        p = r'>(\d+\.\d\.\d+)/</a>'
        pat = re.compile(p)
        f = requests.get(r'http://desktop.yzjop.com/res/CloudHub/feature/')
        html = f.content.decode('utf-8')
        print(html)
        l = re.findall(pat, html)
        return max(l, key=self.compare1)
    def compare1(self,v1):
        return list(map(lambda x:int(x),v1.split('.')))
    def getWinDownUrl(self,Dirurl):
        p = r'>(CloudHubXSetup.+)</a>'
        pat = re.compile(p)
        f = requests.get(Dirurl)
        html = f.content.decode('utf-8')
        return re.findall(p, html)[-1]
    def getMacDownUrl(self,Dirurl):
        p = r'>(CloudHub.+)</a>'
        pat = re.compile(p)
        f = requests.get(Dirurl)
        html = f.content.decode('utf-8')
        print('=========')
        return re.findall(p, html)[-1]

    def download(self,url, filePath,packageName):
        l=os.listdir(filePath)
        if packageName in l:
            os.remove(os.path.join(filePath, packageName))
        path = os.path.join(filePath, packageName )
        print(path)

        r = requests.get(url)
        with open(path, 'wb') as f:
            for i in r.iter_content(100):  #100kb是缓冲区，如果是大文件，要设置缓冲区
                f.write(i)


w=window()

# Create some widgets
# text = sg.Text("请输入电话号码：")
# text_entry = sg.InputText()
# envselect=sg.Text("哪个环境： ")
# mutil=sg.InputCombo(['dev','devtest','kdtest',"正式",'private','T6'],auto_size_text=True)
# button=sg.OK('确认',auto_size_button=True)
# warningText = sg.Text("注意：只会获取第一条验证码，T6和正式一样，如需账号，请查看http://192.168.0.22/cms/pages/viewpage.action?pageId=22152001")
# layout = [[text, text_entry],
#           [envselect,mutil],[button,warningText]]
#
# # Create the Window
# window = sg.Window('获取验证码小工具', layout)
#
# # Create the event loop
# while True:
#     event, values = window.read()
#     if event in (None, 'Cancel'):
#         # User closed the Window or hit the Cancel button
#         break
#     mobile=text_entry.Get().strip('')
#     env=mutil.Get()
#     if env in ['devtest','dev','private']:
#         num=get_verifyCode(mobile,d[env][0],d[env][1],d[env][2],d[env][3])
#     elif env == "kdtest":
#         num=get_kd(mobile)
#     else:
#         num=get_yunzhijiaT6(mobile)
#     print(num)
#     print(env)
#     print(type(mobile))
#
#
#     sg.popup(num)
#
#
#
# window.close()




