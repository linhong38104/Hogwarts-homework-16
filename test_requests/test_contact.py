import requests


def get_token():
    r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwcb19e4e24a59c34a&corpsecret=lZ4i0RPO3ieJullUPRTD0nc5s5yivNTsWJBrwbStQo8')
    token = r.json()['access_token']
    return token

def test_defect_member():
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=TEST02USER'
    r = requests.get(get_member_url)
    print(r.json())
    assert 'TEST02' == r.json()['name']

def test_update_member():
    update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    data = {
        "userid":"TEST02USER",
        "name":"TEST03"
    }
    r = requests.post(url=update_member_url,json = data)
    print(r.json())

def test_create_member():
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "zhangsan",
        "name": "张三",
        "alias": "jackzhang",
        "mobile": "+86 13800000000",
        "department": [1],
        "order": [10, 40],
        "position": "产品经理"
    }
    r = requests.post(url=create_member_url,json = data)
    print(r.json())

def test_delete_member():
    delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=zhangsan'
    r = requests.get(delete_member_url)
    print(r.json())