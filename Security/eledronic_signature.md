# 전자서명

## 전자서명의 형식
암호방식에 따라 크게 두가지로 구별된다.
1. 공개키 암호방식의 공개키 서명방식
2. 관용 암호방식의 중재서명방식

### 과정
1. 송신자는 서명 알고리즘을 통해 메시지에 서명을 한다.
2. 메시지와 서명은 수신자에게 전송된다.
3. 수신자는 메시지와 서명을 받고 이들에게 검증 알고리즘을 적용한다.
4. 만약 그 결과가 참이면 메시지는 올바른 것으로 받아들여지지만, 그렇지 않으면 그 문서는 거절된다.

#### 키의 필요성
전자서명에서 서명자는 자신의 개인키를 이용하여 문서에 서명을 하게 된다.
이때 서명 알고리즘을 사용한다.

검증하는 사람은 역으로 서명자의 공개키를 이용하여 문서를 검증한다.
이때 검증 알고리즘을 사용한다.

### 전자서명 서비스

#### 메시지 인증
안전한 전통적인 서명처럼 안전한 전자서명구조는 메시지 인증을 보장한다.
Bob는 받은 메시지가 Alice로부터 왔다는 것을 확신할 수 있게 된다.

#### 메시지 무결성
메시지 무결성은 전체 메시지에 서명을 할 경우에도 보장이 된다.
왜냐하면 메시지가 변경되면 서명도 같이 달라지기 때문이다.

#### 부인방지
만약 나중에 Alice가 그 메시지를 보낸 사실을 부인한다면
센터는 저장하고 있는 메시지를 제시할 수 있다.

만약 bob의 메시지가 센터가 보관하고 있는 메시지의 복사본과 같다면
Alice는 법정에서 패하게 될 것이다.

#### 기밀성
전자서명을 한다고 해서 기밀성이 보장되는 통신을 할 수는 없다.
만약 기밀성이 필요하다면 메시지와 서명에 비밀키를 이용하거나 공개키를 이용해서 암호화를 해야만 한다.

### 전자서명의 주요 기능
1. 위조 불가(Unforgeable):
    합법적인 서명자만이 전자서명을 생성할 수 있어야 한다.

2. 서명자 인증(User authentication):
    전자서명의 서명자를 누구든지 검증할 수 있어야 한다.

3. 부인방지(NOn-requdiation):
    서명자는 서명행위 이후에 서명한 사실을 부인할 수 없어야 한다.

4. 변경 불가(Unalterable):
    서명한 문서의 내용을 변경할 수 없어야 한다.

5. 재사용 불가(Not reusable): 
    전자문서의 서명을 다른 전자문서의 서명으로 사용할 수 없어야 한다.

## 전자서명 구조
### RSA 전자서명 구조(RSA digital signature scheme)
RSA 아이디어를 이용하면 메시지에 서명을 하고 검증을 할 수 있다.
이것을 RSA 전자서명 구조라고 한다.

RSA 암호 방식을 이용한 전자 서명의 안전도는 RSA 암호 방식의 안전도와 일치한다.

전자서명 구조에서는 개인키와 공개키의 역할이 바뀐다.
암호화의 경우에서처럼 수신자의 키를 사용하는 것이 아닌, 송신자의 개인키와 공개키를 사용한다.
(송신자의 개인키로 암호화를 진행하여, 누구나 열어 볼 수 있도록 하는 것이다)

### ElGamal 전자서명 구조
ElGamal 전자서명은 ElGamal 암호시스템과 동일한 키를 사용하지만 알고리즘은 다르다.
이는 이산대수 문제를 이용한 최초의 서명방식이기 때문이다.

암호화 연산과 전자서명 연산이 거의 동일한 RSA와 달리 ElGamal 전자서명은 암호화 스키마와 꽤 다르다.

이 알고리즘은 실제로 거의 사용되지않으며, 대신 DSA라 알려진 그 변형이 더욱 더 많이 사용된다.


### Schnorr 전자서명 구조
ElGamal 전자서명 구조의 문제인 이산대수 문제로부터 안전해지기 위해 만들어졌다.

해당 서명의 크기를 줄이기 위해서 Schnorr은 ElGamal에 기반을 두고 있지만 서명의 크기는 작은 새로운 구조를 제안하였따.

### 전자서명 표준(DSS, Digital Signature Standard)
전자서명 표준, 이하 `DSS`는 미국의 전자서명 표준으로 `ElGamal` 전자서명을 개량한 방식이다.
전자서명 표준은 `ElGamal` 전자서명 방식과 유사하지만 서명과 검증에 소요되는 계산량을 획기적으로 줄인 방식이다.

`DSS`는 이산대수 문제를 기반으로 하며, 오직 전자서명 기능만을 제공하도록 설계된 알고리즘을 사용한다.

`RSA`와 달리, 이것은 암호화나 키 교환에 사용되지 않지만 공개키 기술이다.

DSA(Digital Signature Standard)는 전자서명에 대한 미 연방 표준 `DSS`이고 `NIST`가 제안하였다.
`ElGamal` 서명 스키마보다 서명 길이가 320비트로 짧고, ElGamal에 대한 공격 중 일부가 적용되지 않는다는 것이다.
|알고리즘|암호/복호|전자서명|키 교환|
|:-:|:-:|:-:|:-:|
|RSA|Yes|Yes|Yes|
|Diffie-Hellman|No|No|Yes|
|DSS|No|Yes|No|
|타원 곡선|Yes|Yes|Yes|
> 공개키 암호시스템의 응용
  
### 타원곡선 전자서명 구조
타원곡선 전자서명 구조(ellptic curve digital scheme)는 타원곡선에 기반을 둔 **DSA**이다.
그렇기에 이 구조는 **ECDSA**라고 부른다.

ECC는 보다 짧은 비트 길이로 인해 짧은 처리 시간에 짧은 서명 생성이 가능하다.
이런 이유로 1998년 **ANSI**(American National standards Institue)가 **ECDSA**를 미국에서 표준화하였다.

## 전자서명 방식

### 메시지 복원형 전자서명
1. 서명자가 자신의 개인키를 이용하여 메시지를 암호화하여 전송하면
2. 검증자가 서명자의 공개키를 이용하여 서명된 암호문을 복호화한다.
3. 그 결과가 일정한 규칙을 만족하는 의미 있는 메시지가 되는지 확인함으로써 서명을 검증한다.
- 장점
    기존의 공개키 암호 방식을 이용하므로 별도의 전자서명 프로토콜이 필요하지 않는다는 장점이 있다.
- 단점
    그러나 메시지를 일정한 블럭으로 나누어 그 각각의 블럭에 서명을 해야 하므로 많은 시간이 소요되어 실제로는 사용되지 않는다.

![메시지 복원형 전자서명](Image/전자서명1.png)
> 앨리스는 미리 공개키와 개인키의 키쌍을 만들어둔다, 또한 밥이 서명을 검증하기 위해 앨리스의 공개키를 입수해야한다.

### 부가형 전자서명
임의의 길이로 주어진 메시지를 해시 알고리즘을 이용해 일정한 길이로 압축하고, 해시한 결과에 서명자의 개인키를 이용하여 전자서명한 후 메시지에 덧붙여 전송한다.

전자서명의 검증은 수신된 메시지를 해시한 결과와 공개키를 이용하여 전자서명을 복호화한 값과 비교함으로써 이루어진다.

부가형 전자서명은 메시지 이외에 전자서명을 따로 전송해야 하므로 전송량이 약간 늘어나는 반면, 메시지가 아무리 길어도 한 번의 서명생성 과정만이 필요하므로 효율적이다.
그러기에 많이 사용되는 편이다.

![부가형 전자서명](Image/전자서명2.png)
1. 메시지 전체를 암호화하는 대신에 일방향 해시함수를 사용해서 메시지의 해시값을 구하고, 그 해시값을 암호화(해시값에 서명)하도록 한다.
2. 메시지가 아무리 길어도 해시값을 짧기에 암호화가 수월해진다.

## 특수 전자서명
공개키 방식을 이용한 전자 서명은 검증키를 공개하고 있어 누구나 서명의 진위를 검증할 수 있으나
전자 서명을 제한적으로 사용하려고 하는 경우 제한하기가 곤란하다.
이는 개인의 이익 침해나 사생활 노출로 이어질 수 있다.

따라서 서명자의 동의가 있어야 검증이 가능하거나 서명문의 내용을 알지 못하게 하고 서명해야 하는 경우 등 다양한 형태에 맞는 전자서명이 필요하다.

### 부인방지 전자서명
일반적인 전자 서명 방식의 서명 검증은 검증자가 임의로 할 수 있으며, 누구든지 검증이 가능한
**자체 인증 기능 특성**을 가지고 있다.
그러나 `D.Chaum`이 제안한 부인 방지 서명(undeniable signature)은 자체 인증 방식을 배제시켜 서명을 검증할 때 반드시 서명자의 도움이 있어야 검증이 가능한 전자 서명 방식이다.

### 의뢰 부인방지 서명
부인 방지 서명 방식은 자신의 서명문을 부인하지 못하게 하는 부인과정 때문에 일종의 **거짓말 탐지기 기능**을 제공해준다.

위의 기능은 결국 검증을 원하는 검증자가 부인 과정을 수행할 수 있다는 데서 기인된다.

따라서 부인 방지 서명의 **거짓말 탐지 기능** 문제를 해결하기 위해서는
임의의 검증자가 부인 과정을 수행하지 못하고 특정한 자, 즉 일종의 해결자 또는 재판관만이 부인 과정을 수행할 수 있어야 한다.

### 수신자 지정 서명
서명의 검증 시 특정 검증자만이 서명을 확인할 수 있도록 하되,  
만일 그 서명이 문제가 되는 경우라도 검증자의 비밀서명 생성정보를 노출시키지않고  
제 3자에게 서명의 출처를 증명함으로써 분쟁 해결 기능을 제공하는 서명 방식을 뜻한다.  

즉 지정된 수신자만이 서명을 확인할 수 있고 필요시
제 3자에게 그 서명이 서명자에 의해 자신에게 발행된 서명임을 증명할 수 있게 함으로써
서명의 남용을 서명자가 아닌 검증자가 통제할 수 있는 서명 방식을 말한다.

### 은닉 서명(Blind digital Signature)
은닉 서명 방식은 D.Chaum에 의해서 제안된 서명 방식이다.

서명 용지 위에 묵지를 놓은 채로 봉투에 넣어 서명자가 서명문 내용을 알지 못하는 상태에서 서명하도록 한 방식을 나타낸 것이 은닉 서명이다.  
즉, 서명문의 내용의 내용을 숨기는 서명 방식으로 제공자(서명을 받는 사람 : provider)의 신원과 서명문을 연결시킬 수 없는 익명성을 유지할 수 있다.

예시를 들면 다음과 같다.
    
    은행(서명자)가 만원에 해당하는 화폐에 서명을 한다고 하면, 화폐는 불추적성이 보장되어야 하므로, 화폐 소유자의 익명성이 보장되어야 한다.
    고객(제공자)는 묵지가 내장된 봉투에 서명받을 용지(만원권)을 넣어 은행에 보내면 은행은 그 고객의 계좌에서 만원을 인출하고 고객이 보낸 봉투 위에다 서명을 한다.
    그러면 내장된 묵지로 인해 봉투안에 있는 서명 용지에도 똑같이 서명이 된다.
    은행은 서명된 봉투를 고객에게 보내고, 고객은 그 봉투를 제거하고 그 안에 있는 용지 위의 서명을 확인한다.

### 위임 서명(proxy digital signature)

M. Mambo와 E. Okamoto는 본인이 부재 중 자신을 대리해서 서명을 할 수 있는 위임 서명을 제안하였다.
이 위임 서명 방식은 위임 서명자(proxy signer)로 하여금 서명자(original signer)를 대신해서 대리로 서명할 수 있도록 구성한 서명 방식을 말한다.

### 다중 서명(multisignatures)

지금까지 개발되어 온 대부분의 전자서명은 문서에 한 사람이 서명하는 단순 서명(single signature) 방식에 중점을 두고 개발되어 왔다.

탄원을 위한 서명서 등에 단순 서명을 밥녹해서 적용하면 서명의 길이가 늘어나고,
서명을 검증하려면 서명자의 수만큼 검증과정을 거쳐야 하기 때문에 서명자가 많은 경우 검증 시간이 오래 걸리는 단점이 있다.

이런 단순 서명방식의 문제를 해결하기 위해 나온 개념이 다중 서명방식으로,
다중서명은 동일한 전자문서에 여러 사람이 서명하는 것이다.

## 전자서명의 응용

### 전자 투표

전자 투표 시스템은 선거인 명부를 DB로 구축한 중앙 시스템과 직접 연결한 단말에 자신이 정당한 투표자임을 증명하면
어디서나 쉽게 컴퓨터망을 통하여 무기명 투표를 할 수 있는 방식이다.

유권자의 투표 기회 증가에 따른 투표율 향상과 투표 결과를 신속히 알 수 있는 등의 장점이 있지만,
유권자 개인의 인증과 투표 내용의 기밀성 유지 등의 문제점이 있기 때문에 현실적으로 실현하기에는 어려움이 많다.

#### 전자 투표 시스템 구현을 위한 요구사항

1. 완전성 : 모든 투표가 정확하게 집계되어야 한다.
2. 익명성 : 투표결과로부터 투표자를 구별할 수 없어야 한다.
3. 건전성 : 부정한 투표자에 의해 선거가 방해되는 일이 없어야 한다.
4. 이중투표방지 : 정당한 투표자가 두 번 이상 투표할 수 없다.
5. 정당성 : 투표에 영향을 미치는 것이 없어야 한다.
6. 적임성(투표자격제한 선거권): 투표권한을 가진 자만이 투표 할 수 있다.
7. 검증 가능 : 선거 결과를 변경 할 수 없도록 누구라도 투표 결과를 확인하여 검증해 볼 수 있어야 한다.

#### 전자 투표 방식

전자투표는 크게 두가지로 나뉜다.

1. 투표소 전자투표(Poll Site E-Voting)
2. 원격 인터넷 투표(Remote Internet e-Voting)

|구분|투표방식|투표장치|선거관리 정도|기술적 쟁점 정도|
|:-:|:-:|:-:|:-:|:-:|
|PSEV방식|투표소 전자투표|전자투표기|상|하|
|키오스크 방식|투표소 전자투표|전자투표기|중|중
|REV방식|모바일, 디지털TV, PC|원격 인터넷 투표|하|상|

PSEV는 터치스크린 기표기를 이용한 것이 대표적이며, 유궈낮는 기존 방식대로 투표소에 나와 마치 ATM과 같은 투표 기기의 터치스크린 화면을 보면서 지지하는 후보의 버튼을 누르면 된다.

REV는 투표소에 가지 않아도 투표할 수 있다.
형태는 다양할 수 있지만, 문자 메세지를 이용한 모바일 SMS 투표, 디지털 TV를 이용한 투표, PC 등 인터넷을 이용한 투표 등이 있다.

### 전자입찰 시스템

입찰 공고에서 다수의 공급자가 응찰하여 오면 이 중에서 가장 싼 가격을 제시한 응찰자와 계약을 맺는 입찰방식을 인터넷을 통하여 구현한 것이다.

#### 요구사항

1. 독립성 : 전자입찰 시스템의 각 구성요소는 자신들의 독자적인 자율성을 보장받아야 한다.
2. 비밀성 : 네트워크 상에서 개별 정보는 각 구성요소 간에 누구에게도 노출되어서는 안 된다.
3. 무결성 : 입찰 시 입찰자 자신의 정보를 확인 가능하게 함으로써 누락 및 변조 여부를 확인할 수 있어야 한다.
4. 공평성 : 입찰이 수행될 때 모든 정보는 공개되어야 하낟.
5. 안전성 : 각 입찰 참여자 간의 공모는 방지되어야 하고 입찰 공고자와 서버의 독단이 발생해서는 안된다.


### 전자서명으로 해결할 수 없는 문제

전자서명이 바르게 이용되기 위해서는 큰 전제 조건이 있다.
그것은 `서명 검증을 할 때 이용하는 공개키가 진짜 송신자의 공개키일 것`이다.
