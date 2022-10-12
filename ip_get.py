# 주어진 url 로 호스트 ip , 포트 알아내기
from urllib.parse import urlparse
import socket
def get_ip(url):
    o = urlparse(url)

    hostname = o.hostname
    port = o.port or (443 if o.scheme == 'https' else 80)
    ip_addr = socket.getaddrinfo(hostname, port)[0][4][0]
    return ip_addr
