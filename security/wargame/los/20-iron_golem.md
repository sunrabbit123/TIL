# iron\_golem

소스코드는 다음과 같다.

```php
<?php
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/sleep|benchmark/i', $_GET[pw])) exit("HeHe");
  $query = "select id from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(mysqli_error($db)) exit(mysqli_error($db));
  echo "<hr>query : <strong>{$query}</strong><hr><br>";

  $_GET[pw] = addslashes($_GET[pw]);
  $query = "select pw from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("iron_golem");
  highlight_file(__FILE__);
?>
```

`sleep`가 막혀있는걸보니 `Time based sqli`가 아닌 `error based sqli`인 것 같다.

`subquery`에 출력이 `2 column`이상이면 에러가 나는 것을 이용하여 `sqli`를 진행하였다.

코드는 [여기](https://github.com/sunrabbit123/TIL/tree/f35c1dcd3c295d492c3895fd89eff46c83899885/Security/Wargame/LOS/20-iron_golem/exploit.py)에 있습니다.

이렇게 해서 `pw`을 얻어내고 Clear!

