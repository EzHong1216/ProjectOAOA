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