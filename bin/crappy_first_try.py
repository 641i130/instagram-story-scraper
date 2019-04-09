### Hecc

from bs4 import BeautifulSoup
import json, random, re, requests, urllib.request
import urllib2

USERNAME = 'fantasaicproductions'
PASSWD = 'Fluteislife$333&1'
account_purging = 'splendiferachie'

BASE_URL = 'https://www.instagram.com/accounts/login/'
LOGIN_URL = BASE_URL + 'ajax/'

headers_list = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.6.01001)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.7.01001)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.5.01003)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8",
    "Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko/20100101 Firefox/11.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.0.3705)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
    "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.01",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0.1) Gecko/20100101 Firefox/5.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.02",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.02 Bork-edition [en]"
    ]

USER_AGENT = headers_list[random.randrange(0,(len(headers_list)+1))]

session = requests.Session()
session.headers = {'user-agent': USER_AGENT}
session.headers.update({'Referer': BASE_URL})
req = session.get(BASE_URL)
soup = BeautifulSoup(req.content, 'html.parser')
body = soup.find('body')

pattern = re.compile('window._sharedData')
script = body.find("script", text=pattern)

script = script.get_text().replace('window._sharedData = ', '')[:-1]
data = json.loads(script)

csrf = data['config'].get('csrf_token')
login_data = {'username': USERNAME, 'password': PASSWD}
session.headers.update({'X-CSRFToken': csrf})
login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)

story_page = "https://www.instagram.com/stories" + "/" + account_purging

# stories url is:
request_headers_story = {
    "Accept:" : "video/webm,video/ogg,video/*;q…q=0.7,audio/*;q=0.6,*/*;q=0.5",
    "Accept-Language" : "en-US,en;q=0.5",
    "Connection" : "keep-alive",
    "DNT" : "1",
    "Host" : "scontent-ort2-1.cdninstagram.com",
    "Range" : "bytes=0-",
    "Referer" : story_page,
    "TE" : "Trailers",
    "User-Agent" : USER_AGENT
}

soup = session.post(story_page, data=request_headers_story, allow_redirects=True)
print(BeautifulSoup(soup.content, 'html.parser'))




















#.
