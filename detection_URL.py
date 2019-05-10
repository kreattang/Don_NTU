import urllib.request
import time

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]

# print('开始检查：')
# tempUrl = 'https://github.com/ethz-asl/1212'
def is404(tempUrl):
    try:
        opener.open(tempUrl)
        return  False
    except urllib.error.HTTPError:
        return True
        time.sleep(3)
    except urllib.error.URLError:
        return True
        time.sleep(2)

# print(is404(tempUrl))