import requests
def spider(key):
    url = 'https://fanyi.baidu.com/sug'
    header = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edg/108.0.1462.54'
    }
    data = {
        'kw':key
    }
    ret = requests.post(url = url,headers = header,data = data).json()['data']
    for i in ret:
        print(i['k'],i['v'])
        
while 1:
    spider(input('翻译：'))