# 도메인 , 서브도메인 추출
import tldextract as tld

def top_name_get(url):
    get_data = tld.extract(url).domain ,tld.extract(url).suffix
    get_name = ".".join(get_data)
    return get_name

def sub_name_get(url):
    get_data = tld.extract(url).subdomain,tld.extract(url).domain, tld.extract(url).suffix
    get_name = ".".join(get_data)
    return get_name

# GUI 제작시 메인 화면에서 도메인 추출 버튼 눌러서 새 창에서 도메인 , 서브도메인 선택할 수 있게 체크박스 해도 되고 새창으로 해도 되고