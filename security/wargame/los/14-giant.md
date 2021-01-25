# Giant

소스코드는 다음과 같다.

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(strlen($_GET[shit])>1) exit("No Hack ~_~"); 
  if(preg_match('/ |\n|\r|\t/i', $_GET[shit])) exit("HeHe"); 
  $query = "select 1234 from{$_GET[shit]}prob_giant where 1"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result[1234]) solve("giant"); 
  highlight_file(__FILE__); 
?>
```

`from`과 `prob_giant`가 붙어있어 `query`가 작동을 안한다. 따라서 공백을 넣어줘야하는데, `WhiteSpace`와 `\n`, `\r`, `\t`가 막혀서 ```과`` \`값을 넣어 공백을 대체해줄 예정이다.

이렇게 Clear!

