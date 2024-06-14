import random

user_agents = [
    # Windows Chrome
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"),
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"),
    # Windows Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    # Windows Edge
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Edge/92.0.902.73 Safari/537.36"),
    # iPhone Safari
    ("Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 "
     "(KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"),
    # Android Chrome
    ("Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"),
    # Mac Safari
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"),
    # Mac Firefox
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
    # iPad Safari
    ("Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 "
     "(KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"),
    # Linux Firefox
    "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    # Samsung Galaxy Chrome
    ("Mozilla/5.0 (Linux; Android 11; SM-A715F) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"),
    # Windows Opera
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.277"),
    # Mac Opera
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 OPR/77.0.4054.277"),
    # iPhone Facebook App
    ("Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 "
     "(KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]"),
    # iPad Chrome
    ("Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 "
     "(KHTML, like Gecko) CriOS/91.0.4472.114 Mobile/15E148 Safari/604.1"),
    # Linux Chrome
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"),
    # Windows IE 11
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    # Android Firefox
    "Mozilla/5.0 (Android 10; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0",
    # Mac Edge
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/92.0.902.73"),
]

def gen_useragent():
    random_user_agent = random.choice(user_agents)
    return random_user_agent
