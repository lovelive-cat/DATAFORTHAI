# Import
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


jar = [] # 리스트 jar 생성
TgtUrl = (
     )  # 튜플 url 생성

LoginUrl = 'https://www.dataforthai.com/login' #dataforthai 로그인 창 path 설정
chrome_options = webdriver.ChromeOptions()  # webdriver의 크롬 옵션 객체 생성
chrome_options .add_argument("--incognito") # 크롬 옵션 시크릿 모드 추가
chrome_options.add_argument("--start-maximized") # 크롬 옵션  전체창 모드 추가


driver = webdriver.Chrome('chromedriver.exe', options=chrome_options) # driver 객체 -> 크롬창 / 크롬 옵션 시크릿 모드
driver.get(LoginUrl) # webdriver에 URL 연결
driver.implicitly_wait(10) # 웹 페이지 로딩 대기 (초)

import pyperclip
from selenium.webdriver.common.keys import Keys
my_id = "sejin@gmail.com" # my_id 변수값(텍스트) 지정
pyperclip.copy(my_id) # my_id 변수 copy
find1 = driver.find_element_by_xpath('//*[@id="login-username"]').send_keys(Keys.CONTROL,'v') # ID 입력창 선택 & 입력 & Xpath에 paste
driver.implicitly_wait(10)

my_pw = "crackcloud" # my_pw 변수값(텍스트) 지정
pyperclip.copy(my_pw) # my_pw 변수 copy
find2 = driver.find_element_by_xpath('//*[@id="login-password"]').send_keys(Keys.CONTROL,'v') # PW 입력창 선택 & 입력 & Xpath에 paste
driver.implicitly_wait(10)

search = driver.find_element_by_xpath('//*[@id="btn-login"]') # 로그인 버튼 element xpath
search.click() # 로그인 버튼 element 실행
driver.implicitly_wait(10) # 웹 페이지 로딩 대기 (초)

search = driver.find_element_by_xpath('//*[@id="UpdateBtn"]') # 업데이트 버튼 element xpath
search.click() # 업데이트 버튼 element 실행
driver.implicitly_wait(10) # 웹 페이지 로딩 대기 (초)

search = driver.find_element_by_xpath('//*[@id="txt_search"]') # TAXID Search 필드 인풋  xpath
search.click() # TAXID Search 필드 인풋 버튼 element 실행
driver.implicitly_wait(10) # 웹 페이지 로딩 대기 (초)

###########################
    #TAXIDInput을 for문에 넣는 과정 필요
###########################

TAXIDInput = "0205560017882" # TAXIDInput 변수값(Number) 지정
pyperclip.copy(TAXIDInput) # TAXIDInput 변수값(Number) copy
find3 = driver.find_element_by_xpath('//*[@id="txt_search"]').send_keys(Keys.CONTROL,'v') # TAXIDInput 선택 & 입력 & Xpath에 paste
find4 = driver.find_element_by_xpath('//*[@id="txt_search"]').send_keys(Keys.ENTER) # TAXIDInput 선택 & 조회(Enter)
driver.implicitly_wait(10) # 웹 페이지 로딩 대기 (초)



for i in TgtUrl:  # for i in 튜플 url
    driver.get(i)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    ComNameTH = soup.select('#main_data > h2') # 회사명 (태국어) / CSS Selector
    ComNameEN = soup.select('#main_data > h3') # 회사명 (영어) / CSS Selector
    TaxID = soup.select('#main_data > table:nth-child(3) > tbody > tr > td:nth-child(1) > table:nth-child(1) > tbody > tr') # 세무등록번호 (영어) / CSS Selector
    BigCatBiz = soup.select('#main_data > table:nth-child(3) > tbody > tr > td:nth-child(1) > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2)')
    RegDate = soup.select('#main_data > table:nth-child(3) > tbody > tr > td:nth-child(1) > table:nth-child(4) > tbody > tr')
    Capital = soup.select('#main_data > table:nth-child(3) > tbody > tr > td:nth-child(1) > table:nth-child(5) > tbody > tr')
    GMapLocation = soup.select('#main_data > table:nth-child(3) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr > td:nth-child(2) > a')

    TelNo = soup.select("#main > div.visible-xs.hidden-sm.hidden-md.hidden-lg.notprint > table:nth-child(3) > tbody > tr > td > table:nth-child(7) > tbody > tr > td:nth-child(2)")

    Email = soup.select("#main > div.visible-xs.hidden-sm.hidden-md.hidden-lg.notprint > table:nth-child(3) > tbody > tr > td > table:nth-child(8) > tbody > tr > td:nth-child(2)")

    # print(TelNo, Email)
#
    serial_no = TgtUrl.index(i)  # 연번 생성(연번 규칙: 튜플 url의 인덱스 값)
    i = [i, ComNameTH, ComNameEN, TaxID, BigCatBiz, RegDate, Capital, GMapLocation, TelNo, Email]
    jar.append(i)  # jar 리스트에 추가

df = pd.DataFrame(jar)  # Extract Dataframe 리스트 데이터 프레임화
# df_trans = df.transpose()
# df_trans.to_excel(r'C:\Users\spect\Desktop\export_dataframe.xlsx', index=True,  header=True)    # Save Excel File 엑셀파일 저장
df.to_excel(r'D:\export_dataframe.xlsx', index=True, header=False)  # Save Excel File 엑셀파일 저장
# print(jar)

driver.quit() # 웹드라이버 종료



# search = driver.find_element_by_xpath('//*[@id="main"]/div[4]/div[2]/div[2]/a[1]/div') # 업종별 조회 element xpath
# search.click() # 업종별 버튼 element 실행
# driver.implicitly_wait(10) # 웹 페이지 로딩 대기 시간


# URLBizCat1 = 'https://www.dataforthai.com/business/objective/47411'
# driver.get(URLBizCat1)
# driver.implicitly_wait(10) # 웹 페이지 로딩 대기 시간
#
# search = driver.find_elements_by_xpath('//*[@id="datatable"]/tbody/tr[1]') # 업종별 조회 element xpath
# search.click() # 업종별 버튼 element 실행
# driver.implicitly_wait(10) # 웹 페이지 로딩 대기 시간




# req = requests.get('https://www.dataforthai.com/business/objective/20231')  # HTTP GET Request
# html = req.text  # HTML 소스 가져오기


# # # Import
# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
#

# soup = BeautifulSoup(html, 'html.parser')  # 뷰티플 소스 라이브러리 가져오기 정의 (파싱 타입 : HTML 문서)