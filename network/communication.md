# 통신 방식

## 네트워크란?
컴퓨터와 컴퓨터가 통신하기 위한 것들

## Media
컴퓨터끼리 통신할때 정보 전달을 해주는 매체
    - 인간으로 치면 소리를 전달해주는 공기정도

총 3종류의 미디어가 있다.
1. Copper(구리선)
    - 전기 신호로 통신
        - 1은 +2.5v, 0은 -2.5v
2. fiber optical(광섬유)
    - 빛으로 통신
3. Radio Wave(전파)
    - 전파로 통신

위 3가지를 통신에 쓰이는 것을 **전자기파**라고 부름

빛은 크게 3개로 나뉠 수 있다.

1. 자외선
    - 가시광선보다 파장이 짧은 류를 얘기한다.
    - 3가지의 빛 중 가장 에너지가 크다.
    - 흔히 무지개에서 보라색 바깥 부분이라 하여서 자외선이라 한다.

2. 가시광선
    - 우리 눈에 보이는 빛이다.

3. 적외선
    - 가시광선보다 파장이 길다.
    - 3가지의 빛 중 가장 에너지가 적다.
    - 흔히 무지개에서 적색 바깥 부분이라 하여서 적외선이라 한다.

## 네트워크 범위에 따른 분류

1. BAN(Body Area Netwrok, 인체 통신망)
    - 사람의 몸과 가까운 곳에 있는 기기들 사이의 네트워크이다.
    - 몸 자체를 전파 전송 주요 환경으로 사용한다.

2. PAN(Personal Area Network, 개인 통신망)
    - 한 명의 사람 범위(최대 10m)내에서 디지털 기기들 사이의 통신을 위한 네트워크
    - 유선으로는 `USB`, `IEEE1394`
    - 무선으로는 `IrDA`, `Bluetooth`, `UWB(Ultra WideBand)`, `ZigBee`등을 이용한다.
    - `Blueooth PAN`은 `Poconet`이라고도 불리며 최대 8개의 활성 장치를 연결한다.

3. HAN(Home Area Network, 가정 통신망)
    - 가정 내 다양한 정보기기들의 상호간 네트워크이다.
    - 가정 내부는 기기들 사이에 유무선 네트워크로 통신하며, 외부는 인터넷을 통해 상호 접속 가능한 환경을 구축한다.

4. LAN(Local Area Network, 근거리 통신망)
    - 하나의 사무실 건물, 캠퍼스와 같이 건물 한채정도의 크기에 대한 최적화된 네트워크다.
    - `LAN`은 중간 노드의 교환이 필요 없는 `점 대 점`(Point to point) 공유물리적 매체를 이용하여 통신한다.
    - 전송 속도는 다른 네트워크에 비해 빠른편이다.(4Mbps ~ 10 Gbps)
    - 구성요소 : 네트워크 운영체제 + LAN 카드 + 전송 매체
    - 프로토콜 : `Ethenet`, `Token Ring` 등

5. MAN(Metropolitan Area Network, 도시권 통신망)
    - `MAN`은 `LAN`의 확장된 개념이며, `LAN`보다는 넓은 지역에 분포하고 있는 연관성이 있는 `LAN` 상호간을 접속해 놓은 네트워크이며, 몇개의 건물로부터 도시 전체에 이르는 `LAN`보다 더 큰 공간에 대한 네트워크이다.
    - 근거리 망에서처럼 `MAN`은 높은 데이터 전송율의 통신채널에 근거하다.
    - `LAN`보다는 속도 면에서 떨어지나, `WAN`에 비해서는 비교적 고속으로 처리되는 구조이다.(34 ~ 155 Mbps, IEEE 802.6에 근거한 `DQDB 사용시이며 반경 30km 이내에 해당한다.)
    - 여러개의 `LAN`들을 고용량 `Backbone` 회선을 통해 연결하는 것을 의미하기도 한다.
    - 프로토콜 : `ATM`, `FDDI`, `SDMS`, `Metro Ethernet`, 등

6. WAN(Wide Area Network, 광역 통신망)
    - `WAN`은 건물, 기업, 도시 및 국가간 등 넓은 지역을 공중망(기간망)을 통해 연결하는 네트워크다.
    - `WAN`은 광역 통신망으로, 넓은 지역에 분산 배치되어 있는 단말기들을 묶어주는 통신망이다.
    - `LAN`이나 `MAN`에 비해 저속이다(1200 bps ~ 24Mbps, `ATM`이며 임대 라인의 경우 156Mbps 이상 가능하다.)
    - 전송시간 지연이 크기에 주로 `점 대 점`(Point to Point) 연결 방식을 이용한다.
    - 프로토콜 : `PPP`, `HDLC`, `SDLC`, `HNAS`, `ISDN`, `X.25`, `Frame Relay`, `ATM` 등
### 특수 네트워크
1. VAN(Value Added Network)
    - `VAN`은 부가가치 통신망으로 `WAN`, `MAN`에 부가적인 통신 기능이나 응용 소프트웨어들을 부가한 통신망이다.