import re

#print(re.search(r'\d\d\d','I love 123FishC.com'))
#匹配ip地址：\d\d\d
#print(re.search(r'[1-9]{2,5}','I love 12344FishC.com'))
#print(re.search(r'^Fish(C|D)','I love 12344FishC'))
#print(re.search(r'\.','FishCFishCFishCFishC.com'))
#print(re.findall(r'[a-z]','FishCFishCFishCFishC.com'))

import urllib.request
import urllib.error

req=urllib.request.Request("http://www.test-sby.com")
try:
    urllib.request.urlopen(req)

except urllib.error.HTTPError as s:
    print(s.code)
    print(s.read())
except urllib.error.URLError as e:
    print(e.reason)
