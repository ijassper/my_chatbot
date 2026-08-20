# python 입출력함수
# -> 입력함수 input()
# -> 출력함수 print()

# streamlit 입출력함수
# -> 입력함수 text_input(), number_input()
# -> 출력함수 write()

import streamlit as st
import requests
from datetime import datetime, timedelta

#print("Hello, world")
#st.write("Hi, World")

#for num in range(1,6):
#  print(num)
#  st.write(num)

#st.button("클릭하세요.")

# 대제목 만들기
st.title("날씨 챗봇")
# 중제목 만들기
#st.header("반갑습니다.")
# 소제목 만들기
#st.subheader("날씨를 알아볼까요?")

# 텍스트박스 입력함수 input("")
# input("이름을 입력하세요: ")
#col1, col2 = st.columns(2)

#with col1:
#  name = st.text_input("이름을 입력하세요")
  # age = st.number_input("나이를 입력하세요")

#  if name:
    #출력
    # 000님 반갑습니다.
    #st.write(f"{age}살, {name}님 반갑습니다.")
    #st.write(f"{name}님 반갑습니다.")
    #st.header(f"{name}님 반갑습니다.")
    # 자료형 문자, 숫자, 불연산자, 튜플, 리스트, 딕셔너리
    #st.write(type(age))
  #else:
    #미출력
#with col2:  
#  st.subheader("날씨를 알아볼까요?")
#  if st.button("클릭하세요."):
#    option = st.selectbox("날씨를 선택하세요",["맑음","흐림","비"])
    #weather = 
#    st.write(f"날씨 선택 : {option}")

# 날씨 API 설정
SERVICE_KEY = "3c2a5f26fb58a9dc3506acf29da6d160442693bbba7ec23b401c1367712f80e5"
BASE_URL = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"  # 단기예보조회

nx = st.text_input("지역의 X좌표를 입력하세요 (예: 60)")
ny = st.text_input("지역의 Y좌표를 입력하세요 (예: 120)")

today = datetime.now().strftime('%Y%m%d')

if st.button("날씨 확인"):
  # API로 데이터 보내기
  params = {
    'serviceKey': SERVICE_KEY,
    'pageNo': '1',
    'numOfRows': '10',
    'dataType': 'JSON',
    'base_date': today,
    'base_time': '0500',
    'nx': nx,
    'ny': ny,
  }

  # 요청한 API 데이터 받기
  response = requests.get(BASE_URL, params=params)
  data = response.json()
  st.write(f"조회 날짜: {today}")

  # 받은 정보 JSON 구조 분석
  try:
    # 응답 코드 확인
    result_code = data['response']['header']['resultCode']
    if result_code == '00':
        items = data['response']['body']['items']['item']
        st.success("날씨 데이터를 성공적으로 가져왔습니다!")
        
        # 데이터 요약 출력
        for item in items[:10]: # 보기 좋게 10개만 출력
            st.write(f"항목: {item['category']} | 예보값: {item['fcstValue']}")
    else:
        st.warning(f"API 호출은 되었으나 에러가 발생했습니다: {data['response']['header']['resultMsg']}")
        
  except Exception as e:
    st.error(f"데이터 처리 중 오류 발생: {e}")
    st.json(data)
