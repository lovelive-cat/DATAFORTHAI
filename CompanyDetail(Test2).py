# Import
import pandas as pd
import requests
from bs4 import BeautifulSoup

# LOGIN_INFO = {
#     'username': 'dev@myjobgate.com',
#     'password': 'dev@!12345'
# }

# with requests.Session() as s:
#     req = s.get('https://www.dataforthai.com/login')
#     html = req.text# HTML 소스 가져오기
#     soup = BeautifulSoup(html, 'html.parser')
#     header = req.headers# HTTP Header 가져오기
#     status = req.status_code# HTTP Status 가져오기 (200: 정상)
#     is_ok = req.ok# HTTP가 정상적으로 되었는지 (True/False)
#     login_req = s.post('https://www.dataforthai.com/login', data=LOGIN_INFO)

##접속 테스트
# print(is_ok)
# print(status)
# print(header)

# print(login_req.status_code) 로그인 테스트, 실패시 "Failed Login"
# if login_req.status_code != 200:
#     raise Exception('Failed Login')


# 스크래핑 시작

jar = []  # 리스트 jar 생성
url = ("https://www.dataforthai.com/company/0205560017882/52%20TRAVEL%20COMPANY%20LIMITED/printview",
       )  # 튜플 url 생성
# "https://www.dataforthai.com/business/search/0205560017882"
# https://www.dataforthai.com/company/0205560017882
# view-source:https://www.dataforthai.com/company/0205560017882/

for i in url:
    req = requests.get(i)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    ComNameTH = soup.select('h2', {'class': 'noelect'})

    # ComNameEN = soup.select('//*[@id="main"]/div[3]/h2')
    # TaxID = soup.select('//*[@id="main"]/div[3]/table[1]/tbody/tr/td/table[1]/tbody/tr/td[2]')
    # BigCatBiz = soup.select('//*[@id="main"]/div[3]/table[1]/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/text()[1]')
    # SmallCatBiz = soup.select('//*[@id="main"]/div[3]/table[1]/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/text()[2]')
    # RegDate = soup.select('//*[@id="main"]/div[3]/table[1]/tbody/tr/td/table[4]/tbody/tr/td[2]')
    # Capital = soup.select('//*[@id="main"]/div[3]/h1')
    # GMapLocation = soup.select('//*[@id="main"]/div[3]/table[1]/tbody/tr/td/table[5]/tbody/tr/td[2]')

    serial_no = url.index(i)  # 연번 생성(연번 규칙: 튜플 url의 인덱스 값)
    i = [ComNameTH]
    # i = [i, ComNameTH, ComNameEN, TaxID, BigCatBiz, SmallCatBiz, RegDate, Capital, GMapLocation]
    jar.append(i)  # jar 리스트

print(jar)

# df = pd.DataFrame(jar)  # Extract Dataframe 리스트 데이터 프레임화
# df.to_excel(r'D:\export_dataframe.xlsx', index=True, header=True)  # Save Excel File 엑셀파일 저장

# print(is_ok)

# req = requests.get('https://www.dataforthai.com/business/objective/20231')  # HTTP GET Request
#   log = {
#     "mode" : "login",
#     "member_type" : "2",
#     "username" : "dev@myjobgate.com",
#     "password" : "dev@!12345",
#     "rc" : "e544a85da2329df1e7b36bc23480c881"
# }
#
# header = {
#     "Referer": "https://www.dataforthai.com/login",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
# }
#
# with requests.Session() as s:
#     login = s.post(req, headers=header, data=log)
#     print(login.text.find('logout')) #로그인이 정상적으로 되었는지 확인용도
#
# # html = req.text  # HTML 소스 가져오기
# # soup = BeautifulSoup(html, 'html.parser')  # 뷰티플 소스 라이브러리 가져오기 정의 (파싱 타입 : HTML 문서)
# # comname = soup.select('tr', {'class': 'clickable-row'})  # ComName 회사이름 웹링크
# # print(comname)