from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st

# 한국 시간대 KST 설정
kst = ZoneInfo("Asia/Seoul")

# 현재 시간 가져오기
now_kst = datetime.now(kst)

# 오늘의 날짜 출력
st.write(now)
