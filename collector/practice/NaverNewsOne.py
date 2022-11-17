import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/001/0013493416?sid=102'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, liek Gecko) Chrome/92.0.4515.131 Safari/537.36'}
result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, 'html.parser')
title = doc.select('h2.media_end_head_headline')[0].get_text()

# get_text() : 태그를 제거하고 text만 추출
# strip() : 앞 뒤 공백을 제거
# - 회원가입(공백을 가지고 입력하는 경우 공백을 지워줌)
content = doc.select('div#dic_area')[0].get_text().strip()
print(f'뉴스제목 : {title}')  # fstring 출력법
print('본문 : {}'.format(content))  #format 출력법