import urllib.request
import urllib.parse
import http.cookiejar
import requests
import base64
import re
import sys
import io



# encoding:utf-8


def uN():
    user = open("username.ini")
    username = user.readlines()
    user.close()
    # return username[0:len(username)]
    return username


def PM(i):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    name = uN()
    data = {'UserName': name[i], 'Password': '123', 'yzm': Bdjk(), 'Submit': '登 录', 'action': 'login'}
    post_data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    log_url = "http://61.157.243.110:4980/index.php"
    req = urllib.request.Request(log_url, headers=headers, data=post_data)
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    resp = opener.open(req)
    url = 'http://61.157.243.110:4980/main.php'
    req = urllib.request.Request(url, headers=headers)
    resp = opener.open(req)
    print(resp.read().decode('utf-8'))
    urltoken = 'http://61.157.243.110:4980/CreditSearch.php'
    req = urllib.request.Request(urltoken, headers=headers)
    resp = opener.open(req)
    print(resp.read())


def Bdjk():
    tp = urllib.request.urlopen('http://61.157.243.110:4980/yzm.php')
    tp_img = tp.read()
    with open('yzm.png', 'wb') as f:
        f.write(tp_img)
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    f = open('yzm.png', 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = jk()
    print(access_token)
    request_url = request_url + "?access_token= " + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        a = str(response.json()['words_result'])
        b = str(re.findall(r"\d+\d", a))[2:6]
        return b


def jk():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lt3XxuaeuZChNeQOjE9MGo03&client_secret=IE4MVrNQ5yxdlBIN5PZ03EykcwWlwmh4'
    response = requests.get(host)
    if response:
        return response.json()['access_token']


PM(1)
