# 주어진 url 로 호스트 ip , 포트 알아내기
from urllib.parse import urlparse
import socket

def get_ip(url):
    #https://가 생략되었을 경우
    if not url.startswith('https://') and not url.startswith('http://'):
        url = 'https://' + url
    o = urlparse(url)

    hostname = o.hostname
    port = o.port or (443 if o.scheme == 'https' else 80)
    ip_addr = socket.getaddrinfo(hostname, port)[0][4][0]
    return ip_addr

def main():
    print(get_ip("http://blkimmo.ch/"))

if __name__ == "__main__":
    main()

# 메인화면에 있는 입력창에 URL 입력하여 바로 출력 가능하게 기능하면 될거 같습니다 .