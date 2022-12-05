import whois


def get_whois(url):

   try:
      domain_info = whois.whois(url)
      #print(type(domain_info))
      return(str(domain_info))
   except whois.parser.PywhoisError :
      return("domain lookup fail")


#메인에서 실행 - 텍스트 파일로 정리
# 저장폴더 열기
