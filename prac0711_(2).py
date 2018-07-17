# Requests를 이용한 HTML 얻어오기
# requests 설치연습
# url 확인
# post / get 확인

import requests
from bs4 import BeautifulSoup
import re #정규표현식 쓰려면
import csv #저장형식
import json


session = requests.Session()
url = "http://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=101&date=20180711"
response = session.get(url)
#print(response.text)

#파일 입출력

#파일 객체
csvfile = open('news title.csv','w')
jsonfile = open('news title.json','w')

#csv 패키지 writer (패키지가 제공하는 무언가?)
spamWriter = csv.writer(csvfile)

soup = BeautifulSoup(response.text, "html.parser") #response.text가 html이고 이걸 구조화를 원해!
#print(soup)

result = soup.findAll("div",{"class":"ranking_headline"}) #tag이름, {속성이름, 속성값}
#print(result)

#print(result[00].contents[1].contents[0])  #기사제목 추출
#for i in range(30):
#    print(result[i].contents[1].contents[0]) #기사제목 다 추출하기

soupResult = soup.findAll("div",{"class":"ranking_headline"})
for i in range(30):
    # (?<=title=").*(?=\s)
    # 전방탐색 (?=~) / ~까지 포함하지않고 그 앞까지
    # 후방탐색 (?<=~) / ~포함하지 않고 그 뒤부분

    #print(str(soupResult[i]))
    exp = r"(?<=title=(\"|\')).*(?=(\"|\')>)"

    #print(str(soupResult[i]))
    rex = re.search(exp,str(soupResult[i]))

    if(rex is not None):

        #print(rex.group(0))
        #csv 파일
        spamWriter.writerow([str(rex.group(0))])

        #json 파일
        data = {"title":str(rex.group(0))}
        json.dump("\n", jsonfile)
        json_t = json.dumps(data, ensure_ascii=False)
        jsonfile.write(json_t)



# 정규표현식 : 문자열 검색할 때 사용
# abc+ >> abc, abcc, abccc ...
# c의 개수 제한
#   abc{10} : c가 10개 / abc{10,} : c가 10개 이상 / abc{10,20} : c가 10이상 20이하
# abc? >> ab 뒤에 c가 있거나 없거나 >> abc, ab
# . : 어떠한 임의의 한 문자 표현
# .* : 어떠한 문자 표현 >> abc. : abc 뒤에 어떤게 와도 상관없음
# \. : 점 자체를 표현
# [abc] = a|b|c

# 퀴즈
# 0xFFFF 와 같은 16진수 : ^(0x)[a-fA-F0-9]{4}
# 문자열 앞의 공백 : ^\s*[^S]
# abc로 시작하고 efg로 끝나는 문자열 : ^abc.*efg$
# 핸드폰 번호 : \d{3}\-\d{4}\-\d{4}
# 주민등록번호 : \d{6}\-\d{7}
# i like apples and bananas > ^.*?s > i like apples
