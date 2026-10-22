from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st
import requests

# 한국 시간대 KST 설정
kst = ZoneInfo("Asia/Seoul")

# 현재 시간 가져오기
now_kst = datetime.now(kst)

# 기상청 형식으로 변환
tm_value = now_kst.strftime('%Y%m%d%H%M')

# 기상청 API 허브 RestAPI
url = f"https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?tm=tm_value&stn=0&help=1&authKey=HKQyUIPtQ72kMlCD7UO9cw"
response = requests.get(url)

st.write("응답결과")
# 데이터의 길이가 길어서 text함수가 더 보기 편함.
st.text(response.text)

# 오늘의 날짜 출력
st.write(now_kst)
st.write(tm_value)
