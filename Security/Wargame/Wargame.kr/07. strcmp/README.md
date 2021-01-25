# Leverage vulnerabilities in strcmp
1. check the view source
2. strcmp($POST['password'], $password) should be made into a strcmp (array, string) format
3. "password" replace "password[]=" in html code
4. Clear!!
    + strcmp(array, string) == 0 in strcmp

1. 소스코드를 확인한다.
2. strcmp를 사용해 비교하는것을 체크한다.
3. strcmp는 php에서 스트링과 비교할시에 0으로 체크된다.
4. 따라서 개발자관리모드에서 strcmp를 strcmp(array, string)으로 들어가도록
"password"부분을 "password[]="으로 교체해준다.
5. 그 다음 아무값이나 보내면 flag값을 얻을 수 있다.
