# ARP 프로토콜

`Address Resolution Protocol`, 즉 `주소 결정 프로토콜`은 줄여서 `ARP`라고 한다.
네트워크 상에서 `IP`주소를 물리적 주소인 `MAC`주소와 대응시키기 위해 사용되는 프로토콜이다.

## ARP Header

- Hardware Type(`HTYPE`) : 네트워크 유형을 정의하며, `Ethernet`의 경우 `0x0001`으로 세팅한다.
- Protocol Type(`PTYPE`) : 프로토콜을 정의하며, `IPv4`의 경우 `0x0800`으로 세팅한다.
- Hardware Length(`HLEN`) : `MAC`주소를 정의하며, `Ethernet`의 경우 `6byte`으로 세팅한다.
- Protocol Length(`PLEN`) : 프로토콜의 길이를 정의하며, `IPv4`의 경우 `4byte`으로 세팅한다.

- Operation(`OPER`) : 패킷의 유형이며, `ARP`요청(`ARP Request`)의 경우는 `1`, `ARP`응답(`ARP Reply`)의 경우 `2`

- Sender Hardware Address (`SHA`) : 발신자의 `MAC` 주소 세팅
- Sender Protocol Address (`SPA`) : 발신자 `IP` 주소 세팅

- Target Hardware Address (`THA`) : 목적지 `MAC` 주소이며 `OPER`이 `일 경우 알 수 없다.
- Target Protocol Address (`TPA`) : 목적지 `IP` 주소 세팅

## ARP 특징

동일한 세그먼트 내에서 통신을 하는 경우에 `MAC`을 이용한 통신을 하기 때문에 `ARP` 스푸핑을 주의해야 한다.
