# python 입출력함수
# -> 입력함수 input()
# -> 출력함수 print()

# streamlit 입출력함수
# -> 입력함수 text_input(), number_input()
# -> 출력함수 write()

import streamlit as st

print("Hello, world")
st.write("Hi, World")

#for num in range(1,6):
#  print(num)
#  st.write(num)


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
    st.write(f"{name}님 반갑습니다.")
    # 자료형 문자, 숫자, 불연산자, 튜플, 리스트, 딕셔너리
    #st.write(type(age))
  #else:
    #미출력

with col2:  
  option = st.selectbox("날씨를 선택하세요",["맑음","흐림","비"])
  st.write(option)
