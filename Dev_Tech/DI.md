# DI
DI는 Dependency Injection이라고 불리는데, 의존성 주입이라고 한다.

이는 이제 스프링에서는 IOC라고 불리기도하지만 DI라고 불리기도 한다.
> IOC와 DI는 엄밀히 따지면 다르지만, 이는 어떻게 해석하느냐의 차이이기도 하다.
> IOC : 역전 컨테이너, DI : 의존성 제어

몇가지 예시 코드를 살펴보자
```java
public class SubHello {
    public SubHello() {
        System.out.println("sub Hello");
    }
}

public class Hello {
    public Hello() {
        SubHello subHello = new SubHello();
        System.out.println("hello?");
    }
}

public class Client {
    public static void main(String[] args) {
        Hello hello = new Hello();
    }
}
```
이 코드를 보면 `Hello`가 시작이 되어야 `SubHello`가 시작이 된다.
이런 경우 `SubHello`가 `Hello`에 의존적이다라고 할 수 있다.

이의 경우 `Hello`로 `SubHello` 조작이 힘드니 좋다고  할 수는 없다.
이를 의도한 경우면 모를까

다음 코드를 보자
```java
public class Hello {
    public Hello() {
        System.out.println("hello?");
    }
}

public class SubHello {
    public SubHello() {
        System.out.println("sub Hello");
    }
}

public class Client {
    public static void main(String[] args) {
        Hello hello = new Hello();
        SubHello subHello = new SubHello();
    }
}
```
다음 코드는 전 문제의 해결점을 해결은 하였지만
`Hello`와 `SubHello`가 따로 놀기에 `Hello`로 `SubHello`를 조작하기는 매우 힘들다. 이런 경우 결합도가 낮다고 한다. 두 `Hello`와 `SubHello`는 관계가 없기 때문이다.

그럼 원하는건 두가지가 된다.
1. 코드의 의존도는 낮춘다.
2. 코드의 결합도를 높인다.

그러기에 다음과 같은 코드가 생겨난다.
```java
public class SubHello {
    public SubHello() {
        System.out.println("sub Hello");
    }
}

public class Hello {

    private SubHello subHello;

    public Hello(SubHello subHello) {
        this.subHello = subHello;
        System.out.println("hello?");
    }
}

public class Client {
    public static void main(String[] args) {
        SubHello subHello = new SubHello();
        Hello hello = new Hello(subHello);
    }
}
```
이 경우 `SubHello`를 `Hello`에 넣음으로써
두가지의 문제를 해결하였다.

`Hello`로 `SubHello`를 조작이 가능하며, `SubHello`가 단독으로 실행이 된다.
> `Hello` <- `SubHello`

스프링에서 IOC라는 기술로 DI를 제공한다.

이제 스프링의 경우는 저는 안하기에, 언젠가 배울 쯤에 다시 언급하지않을까 싶다.
> 코드 출처 : [https://b-programmer.tistory.com/255](https://b-programmer.tistory.com/255)