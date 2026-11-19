from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st
import requests

# 페이지 설정 및 제목
st.title("🤖 기상청 우리동네 날씨 챗봇")

# 기상청 지점번호 매핑 딕셔너리 (도시 이름 -> 기상청 지점 번호 stn)
station_map = {
    "서울": "108",
    "부산": "159",
    "인천": "112",
    "대구": "143",
    "광주": "156",
    "대전": "133",
    "제주": "184",
    "강릉": "105",
    "전주": "146",
    "춘천": "101"
}

# 세션 상태 초기화 (챗봇의 단기 기억 수첩)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 대화 기록 화면에 출력하기
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 기상청 데이터를 가져와서 파싱하는 함수
def get_kma_weather(stn_id):
    # 한국 시간 기준 현재 시간의 '정시' 구하기
    kst = ZoneInfo("Asia/Seoul")
    now_kst = datetime.now(kst).replace(minute=0, second=0, microsecond=0)
    tm_value = now_kst.strftime('%Y%m%d%H%M')
    
    # 인증키 및 URL 설정
    auth_key = "HKQyUIPtQ72kMlCD7UO9cw"
    url = f"https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?tm={tm_value}&stn={stn_id}&help=1&authKey={auth_key}"
    
    response = requests.get(url)
    
    try:
        # 데이터 파싱 - 전체 텍스트를 줄바꿈('\n') 기준으로 쪼개서 리스트로 만들기
        lines = response.text.split('\n')
        
        # 날씨 정보가 있는 줄만 추출할 리스트
        clean_lines = []
        for line in lines:
            # 줄이 비어있지 않고, '#'으로 시작하지 않는다면?
            if line != "" and not line.startswith('#'):
                clean_lines.append(line)  # 깨끗한 상자에 담기!
        
        # 깨끗한 줄들 중에서 가장 마지막 줄 선택하기
        data_line = clean_lines[-1]
        
        # 공백 기준으로 데이터 분리 (리스트화)
        values = data_line.split()
        
        # 명세서 기준 인덱스 매칭
        # TA(기온): 9번, WS(풍속): 3번, HM(습도): 12번 또는 13번 등 (데이터 포맷에 맞춤)
        # 안전하게 가져오기 위해 값이 있는지 확인
        ta = values[11]   # 기온
        ws = values[3]   # 풍속
        hm = values[13]  # 습도 (데이터 형식에 따라 12 또는 13)
        
        return {"temp": ta, "wind": ws, "humidity": hm, "success": True}
        
    except Exception as e:
        return {"success": False, "error": str(e)}

# 6. 채팅 입력창 (하단 고정)
if prompt := st.chat_input("도시 이름을 입력하세요 (예: 서울, 부산, 대전)"):
    # 사용자 질문 출력 및 세션 저장
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 챗봇 답변 출력 영역
    with st.chat_message("assistant"):
        # 딕셔너리에 있는 도시인지 확인 (없으면 기본값 서울 '108' 지정)
        stn_id = station_map.get(prompt)
        
        if stn_id:
            # 날씨 데이터 가져오기 실행
            result = get_kma_weather(stn_id)
            
            if result["success"]:
                reply = f"대한민국 기상청 관측 기준 [{prompt}]의 날씨입니다.\n\n" \
                        f"🌡️ **현재 기온**: {result['temp']} °C\n" \
                        f" **바람 풍속**: {result['wind']} m/s\n" \
                        f" **상대 습도**: {result['humidity']} %"
            else:
                reply = "죄송합니다. 현재 기상청 서버에서 데이터를 가져오지 못했어요. 잠시 후 다시 시도해 주세요!"
        else:
            reply = f"'{prompt}'은(는) 등록되지 않은 도시예요. 서울, 부산, 인천, 대구, 광주, 대전, 제주 중에서 입력해 주세요!"
            
        # 챗봇 답변 화면 출력 및 세션 저장
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
