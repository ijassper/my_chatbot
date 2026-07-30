# python 입출력함수
# -> 입력함수 input()
# -> 출력함수 print()

# streamlit 입출력함수
# -> 입력함수 text_input(), number_input()
# -> 출력함수 write()

import streamlit

print("Hello, world")
streamlit.write("Hi, World")

for num in range(1,6):
  print(num)
  streamlit.write(num)
