# TCP/IP

통상적으로 TCP/IP의 경우
OSI7계층을 베이스로 1~2계층을 하나로, 5~7계층을 하나로 만들기 때문에 4층의 모습을 띄게된다.

따라서 다음과 같이 각 계층이 불린다.

1. [네트워크 인터페이스 계층](#Network-Interface-Layer)
2. [인터넷 계층](#Internet-Layer)
3. [트랜스포트 계층](#Transfort-Layer)
4. [애플리케이션 계층](#Application-Layer)

## Network Interface Layer
TCP/IP 패킷을 네트워크 매체로 전달하는 것과 네트워크 매체에서 TCP/IP 패킷을 받아들이는 과정을 담당한다.

## Internet Layer
어드레싱, 패키징, 라우팅 등의 기능을 제공하며,
여기서 핵심 프로토콜은 `IP`, `ARP`, `ICMP`, `IGMP`등 이다.

## Transfort-Layer
애플리케이션 계층에 세션과 데이터 그램 통신 서비스를 제공한다.
핵심 프로토콜은 `UDP`, `TCP`이다.

## Application-Layer
다른 계층의 서비스에 접근할 수 있게 하는 앱을 제공하며, 앱들이 데이터를 교환하기 위해 사용하는 프로토콜을 정의한다.
프로토콜로는 `HTTP`, `FTP`, `SMTP`, `Telnet` 등이 있다.