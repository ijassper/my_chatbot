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

# 테이터 파싱
# API에서 데이터를 가져와서 필요한 정보 찾기

# 1단계 : 전체 내용을 줄 단위로 분리
all_lines = response.text.split('\n')

# 2. 필요한 정보 검색(반복문)
clean_lines = []
# 샘플데이터 중에서 온도 정보가 있는 자료 검색
# sample_data = [0.3, 10.0, 1.6, 56.0, 6.9, -9.0, -9.0, -9.0, -9.0, -9.0]
for line in all_lines:
  if line != "" and not line.startswith('#'):
    # 만들어놓은 정제라인 변수에 리스트자료형으로 데이터 처리  
    clean_lines.append(line)

# 3. 분리시켜놓은 정보에서 마지막 정보만 추출
data_line = clean_lines[-1]

# 4. 최종 정보에서 온도 데이터 추출

#st.write("정재데이터")
st.write(data_line)

# 오늘의 온도 출력
st.write("현재 온도 : _________")

sample_text = "Hello, python world"
#인뎅싱으로 hello만 출력
#st.write(sample_text[13:])


st.write("응답결과")
# 데이터의 길이가 길어서 text함수가 더 보기 편함.
st.text(response.text)

# 오늘의 날짜 출력
st.write("현재 시간 : ", now_kst)
st.write("변환된 현재 시간 : ",tm_value)

# 오늘에 기상 데이터 출력

st.write("현재 온도 : ", )
