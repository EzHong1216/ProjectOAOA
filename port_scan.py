# 타겟 ip or 도메인에 대해 오픈된 포트 스캔
import socket
import ipaddress
import re

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

def port_scan():
    port_regex = re.compile("([0-9]+){1,5}-([0-9]+){1,5}")
    ip_regex1 = re.compile("^\d")
    ip_regex2 = re.compile("^www\.")
    while True:
        ip_addr_input = input("IP 주소 또는 도메인 주소를 입력(ex: 127.0.0.1 or www.naver.com) :")
        try:
            ip_regex1_valid = ip_regex1.search(ip_addr_input.replace(" ", ""))
            ip_regex2_valid = ip_regex2.search(ip_addr_input.replace(" ", ""))
            if ip_regex1_valid:
                ip_addr = ipaddress.ip_address(ip_addr_input)
                break
            elif ip_regex2_valid:
                ip_addr = ip_addr_input
                break
        except:
            print("잘못된 주소 형식입니다.")

    while True:
        try:
            loop_num = int(input("접속 시도 횟수 지정 : "))
            break
        except:
            print(" 숫자만 입력 가능합니다.")

    while True:
        port_min = 0
        port_max = 65535
        print('경고! 정보통신망법은 ‘정당한 접근권한 없이 또는 허용된 접근권한을 초과해 정보통신망에 침입’하는 행위를 금지하고 있습니다.')
        print('\n본 프로그램을 이용한 사전 협의 없는 포트 스캔을 금지합니다!')
        port_range = input("스캔 할 포트 범위 지정(ex:0-65535) :")
        port_range_valid = port_regex.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break
    i = 0
    open_ports = []
    while i < loop_num:
        valid_ports = []

        print(f"{i+1}회차")
        for port in range(port_min, port_max + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    s.connect((ip_addr, port))
                    valid_ports.append(port)
            except:
                print("port", port, "not open")
                pass
        for port in valid_ports:
                print(f"연결된 포트 : {port}")

                open_ports.append(port)

        i = i + 1

    total_ports = {}
    for value in open_ports:
        try:
            total_ports[value] += 1
        except:
            total_ports[value] = 1
    print(f'\n접속 주소 {ip_addr_input}')
    print(f'총 {loop_num} 번 접속 시도 하였습니다.')
    for key, value in total_ports.items():
        print(f'연결된 포트 번호 : {key} / 연결 횟수 : {value}')
    return total_ports

print(port_scan())

# 해야 할것 , 소켓 데이터 출력
# 메인으로 리턴값 만들것
# 출력값 가독성