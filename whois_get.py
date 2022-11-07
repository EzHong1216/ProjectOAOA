import whois


def whois_get(url):

   try:
      domain_info = whois.whois(url)
      print(type(domain_info))
      print(domain_info)
   except whois.parser.PywhoisError :
      print("domain lookup fail")


whois_get("https://www.ssjoy.org/dho/")

#메인에서 실행 - 텍스트 파일로 정리
# 저장폴더 열기
