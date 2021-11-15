#!/bin/python3
from selenium import webdriver
from sys import argv
from re import search

flags = [f for f in argv if len(f)>0 and f[0]=='-']
args = [a for a in argv[1:] if a not in flags]
url = args[0]
re_search = '.' if len(args) <2 else args[1]


browser = webdriver.Firefox()
browser.get(url)
curl=browser.current_url
cookies = []
while 1:
    try:
        cookies=browser.get_cookies()
        if curl != browser.current_url:
            browser.quit()
            break;
    except:
        break
cookies = {x['name']:x['value'] for x in cookies if x['domain'] in url and search(re_search,x['name'])}
if '-b' in flags:
    print('; '.join([f"{k}='{v}'" for k,v in cookies.items()]))
else:
    print(cookies)
