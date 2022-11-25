import whois


def whois_get(url):

   try:
      domain_info = whois.whois(url)
      #print(type(domain_info))
      return(str(domain_info))
   except whois.parser.PywhoisError :
      return("domain lookup fail")

def main():
   print(whois_get("https://www.ssjoy.org/dho/"))

if __name__ == "__main__":
   main()

#메인에서 실행 - 텍스트 파일로 정리
# 저장폴더 열기
