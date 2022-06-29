def domain_name(url):
    domain = url

    if url[:8] == 'https://':
        domain = domain[8:]
    elif url[:7] == 'http://':
        domain = domain[7:]

    if domain[:4] == 'www.':
        domain = domain[4:]

    return domain.split('.')[0]


print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
