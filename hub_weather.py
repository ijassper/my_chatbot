from datetime import datetime
import streamlit as st

# 현재 시간 가져오기
now = datetime.now()

# 오늘의 날짜 출력
st.write(now)
