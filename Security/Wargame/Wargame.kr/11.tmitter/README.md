# Tmitter sqli or html modification

## 첫번째 HTML코드 수정
1. 사이트 sign up 페이지에 접속한다.
2. admin 계정으로 로그인을 하기 위해서 admin 계정을 새로 만들 예정이다.
고로 id에 admin을 넣어야만 한다.
3. html코드를 수정하여서 최대 입력 제한을 없앤다.
4. admin + (27칸의 공백) + 아무거나 를 입력해주고, 비밀번호는 원하는걸로 적어준다.
5. 가입 완료!
6. 아이디에 admin을 넣고 아까 넣은 비밀번호를 넣어준다.


1. join the site at sign up
2. you should input id : admin but admin is overlapping account
3. html modification at id input windows
4. maxlenght : 32 -> anything
5. you should sign up that id is admin(27 blank) + anything
6. Wow you succese the sign up that overlapping admin account

## second sqli
1. if id in ', show \'
-> server use addslashes or mysql_real_escape_string or something
2. if id in %1a, show \Z
-> mysql_real_escape_string or something
3. input id that admin%bf' and 0
