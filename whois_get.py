import whois


def whois_get(url):

   try:
      domain_info = whois.whois(url)
      print(type(domain_info))
      print(domain_info)
   except whois.parser.PywhoisError :
      print("domain lookup fail")

