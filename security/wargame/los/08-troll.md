# Troll

소스코드는 다음과 같다.

```php
<?php  
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
  if(preg_match("/admin/", $_GET[id])) exit("HeHe");
  $query = "select id from prob_troll where id='{$_GET[id]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id'] == 'admin') solve("troll");
  highlight_file(__FILE__);
?>
```

`admin`을 우회해 Where문에 넣어야한다. `php` 에서는 `Admin`이랑 `admin`은 다르다. 하지만 MySQL에서는 같으니 `Admin`을 넣어서 우회하면 된다.

