# Golem

소스코드는 다음과 같다.

```php
?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and|substr\(|=/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_golem where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_golem where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem"); 
  highlight_file(__FILE__); 
?>
```

`or`, `and`, `substr`, `=`들이 금지되었다.
`or`의 경우 `||`로, `=`의 경우 `like`로 대체가 가능하다.

> ?pw=1%27||id%20like%27admin

이렇게 하면 `Hello admin`이 출력이 되면서, 우회가 성공했음을 알 수 있다.

그러면 `pw`를 알아내는 exploit 코드를 작성해보자

```python

```

이렇게 clear!
