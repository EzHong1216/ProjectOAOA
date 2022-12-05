import requests

def dirscan_spec(url):
    r = requests.get(url)
    if r.status_code == 200:
        return(" 연결 성공 : " + url)
    else:
        return(" 연결 실패 : " + url)
    
def dirscan(url):
    result = []
    result.append("디렉토리 리스트 대조 진행")

    f = open("./dir_scan_list.txt", 'r')
    while True:
        data = f.readline()
        dirscan_spec(url+data)
        if not data: break

    f.close()
    return result
