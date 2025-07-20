import getopt
import json
import re
import sys
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

useage = 'python index.py -u <url>'


# 获取命令行参数
def getArgs(argv):
    if len(argv) == 0:
        print(useage)
        sys.exit(2)
    url = ''
    try:
        opts, args = getopt.getopt(argv, "hu:", ["url="])
    except getopt.GetoptError:
        print(useage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(useage)
            sys.exit()
        elif opt in ("-u", "--url"):
            url = arg
    return {
        'url': url,
    }


def extract_play_url_info(text):
    pattern = r'"playUrlInfo"\s*:\s*\[\s*{.*?}\s*\]'
    match = re.search(pattern, text, re.DOTALL)

    if match:
        json_str = "{" + match.group(0) + "}"
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            corrected = re.sub(r"\\u002F", "/", json_str)
            return json.loads(corrected)
    return None


# 获取真实地址
def getRealUrl(url):
    parse = urlparse(url)
    host = parse.netloc
    if 'bilibili.com' not in host:
        print('url host wrong, ' + url)
    path = parse.path
    scheme = parse.scheme
    headers = {
        'authority': host,
        'method': 'GET',
        'path': path,
        'scheme': scheme,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36',
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }
    res = requests.get(url=url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    scripts = soup.find_all('script')
    for script in scripts:
        # print(script.prettify())
        if 'playUrlInfo' in script.prettify():
            # print(script.prettify())
            return extract_play_url_info(script.prettify())['playUrlInfo'][0]['url']


def main(argv):
    args = getArgs(argv)
    url = args['url']
    realUrl = getRealUrl(url)
    print(realUrl)


if __name__ == "__main__":
    main(sys.argv[1:])
