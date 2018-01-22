import urllib.request
import urllib.parse
import re

url='https://www.baidu.com/s'
wd = '名字'
url += '?wd='+urllib.parse.quote(wd)
#print(url)

req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

result = re.search(r"百度为您找到相关结 果约(.)+个",html)

#print(html)
result = re.search(r"(\d)+",result.group().replace(',',''))
print(result.group())