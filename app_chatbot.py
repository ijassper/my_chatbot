# python 입출력함수
# -> 입력함수 input()
# -> 출력함수 print()

# streamlit 입출력함수
# -> 입력함수 text_input(), number_input()
# -> 출력함수 write()

import streamlit as st

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
col1, col2 = st.columns(2)

with col1:
  name = st.text_input("이름을 입력하세요")
  # age = st.number_input("나이를 입력하세요")

  if name:
    #출력
    # 000님 반갑습니다.
    #st.write(f"{age}살, {name}님 반갑습니다.")
    #st.write(f"{name}님 반갑습니다.")
    st.header(f"{name}님 반갑습니다.")
    # 자료형 문자, 숫자, 불연산자, 튜플, 리스트, 딕셔너리
    #st.write(type(age))
  #else:
    #미출력
with col2:  
  st.subheader("날씨를 알아볼까요?")
  if st.button("클릭하세요."):
    option = st.selectbox("날씨를 선택하세요",["맑음","흐림","비"])
    #weather = 
    st.write(f"날씨 선택 : {option}")

# 1. API 기본 설정
api_key = "9D4OIHOT-9D4O-9D4O-9D4O-9D4OIHOTZC"
base_url = "https://www.safemap.go.kr/openApiService/wms/getLayerData.do"

# 2. 사용자 입력 (지도 조회를 위한 파라미터)
st.subheader("지도 조회 설정")
# 실제 서비스에서는 레이어명을 선택하게 하면 좋습니다.
layer_name = st.text_input("레이어명 (예: A2SM_TFCACDSTTUS_BIG)", "A2SM_TFCACDSTTUS_BIG")

if st.button("지도 불러오기"):
    # 3. WMS 방식의 URL 생성
    # 참고: 이미지 예시에 나온 파라미터 조합
    wms_url = f"{base_url}?apikey={api_key}&LAYERS={layer_name}&STYLES={layer_name}&FORMAT=image/png&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&CRS=EPSG:4326&BBOX=33,124,43,132&WIDTH=500&HEIGHT=500"
    
    st.write("생성된 URL:", wms_url)
    
    # 4. 이미지 출력
    try:
        st.image(wms_url, caption="생활안전지도 데이터 시각화")
        st.success("데이터를 성공적으로 불러왔습니다!")
    except Exception as e:
        st.error(f"이미지를 불러오는 중 오류가 발생했습니다: {e}")
