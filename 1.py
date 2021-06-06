import json
import urllib.request
import urllib.parse

import requests


def getToken():  # 获取token函数
    url = "http://61.157.243.110:4980/login.php"
    data = {'UserName': '20305064', 'Password': '123'}
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data=data)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print(target)


getToken()
