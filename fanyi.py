import requests,json

def fanyi(enter):
    kw = enter[6:]
    url = 'https://fanyi.baidu.com/sug'
    header = {
        'kw':kw
    }
    res = requests.post(url,data=header)
    json_res = json.loads(res.text)
    print(json_res['data'][0]['v'])
