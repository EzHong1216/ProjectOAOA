import requests

def dirscan_spec(url):
    r = requests.get(url)
    if r.status_code == 200:
        return("[◈] Connect → " + url)
    else:
        return("[X] Connect Failed: " + url)
    
def dirscan(url):
    result = []
    result.append("Directory Scanning...")

    f = open("./dir_scan_list.txt", 'r')
    while True:
        data = f.readline()
        dirscan_spec(url+data)
        if not data: break

    f.close()
    return result

def main():
    print(dirscan("http://bellsoft.net"))
    
if __name__ == "__main__":
    main()