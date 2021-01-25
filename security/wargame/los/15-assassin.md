# Assassin

소스코드는 다음과 같다.

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_assassin where pw like '{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("assassin"); 
  highlight_file(__FILE__); 
?>
```

`like`의 정규표현식을 이용하여 푸는 문제인것 같다. 흔히 사용하는 와일드카드인 `*`의 역할을 `like`에서는 `%`가 대신한다. 이를 이용하여 `brute force attack`이 가능하다.

이렇게 `admin`의 `pw`를 얻어내면 `Clear!`

Hint : `admin`의 `pw`와 `guest`의 `pw`는 앞자리 2~3개가 같다.

