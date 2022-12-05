# 타겟 ip or 도메인에 대해 오픈된 포트 스캔
import socket
import ipaddress
from PyQt5.QtWidgets import QMessageBox
import re
from PyQt5.QtTest import QTest

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

#특정 아이피의 특정 포트가 열려 있는가?
def is_Valid_Port(ip_addr: str, port: int = 80) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_addr, port))
            return True
    except:
        print(bcolors.WARNING +bcolors.BOLD+"port", port, "not open"+ bcolors.ENDC)
        return False

#특정 아이피의 포트들을 스캔
def scan_port(url_input: str, port_min: int=80, port_max: int=90) -> list:
    valid_ports = []

    for port in range(port_min, port_max + 1):
        if is_Valid_Port(url_input, port):
            print(bcolors.OKGREEN + bcolors.BOLD + '연결된 포트 : ' +str(port)+ bcolors.ENDC)
            valid_ports.append(port)
    
    return valid_ports

#주요 포트 빠른스캔
def Fastscan(url):
    result = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        s.connect((url, 80))
        ipscan = s.getsockname()[0]

    port = [80, 20, 21, 22, 23, 25, 53, 5357, 110, 123, 161, 443, 1433, 3306, 1521, 8080, 135, 139, 137, 138, 445, 514, 8443, 3389, 8090, 42, 70, 79, 88, 118, 156, 220]
    host = url

    result.append("IP and Port 스캐닝...")
    result.append('IP 스캔 → '+ipscan)
    QTest.qWait(1)
    
    target_ip = socket.gethostbyname(host)
    opened_ports = []
    for p in port:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            results = sock.connect_ex((target_ip, p))

        if results == 0:
            opened_ports.append(str(p))

    for i in opened_ports:
        result.append('연결된 포트 :'+ i)

    return result


# 해야 할것 , 소켓 데이터 출력
# 메인으로 리턴값 만들것
# 출력값 가독성