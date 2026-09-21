import streamlit as st
import requests

# API 키 설정
API_KEY = "8464cff4dd30fe09c5447727526f939a"

st.title("우리동네 날씨챗봇")
st.write("도시 이름을 잊력하면 현재 날씨를 알려드려요.")

# 한글로 도서를 입력하면 영어로 검색하는 기능
# 서울 - > Seoul
# 1. 리스트 2. 딕셔너리 3. 튜플
city_map = {
    "서울":"Seoul", "부산":"Busan", "인천":"Inchen", "대구":"Daegu", 
    "광주":"Gwangju", "대전":"Daejeon", "울산":"Ulsan", "수원":"Suwon", "제주":"Jeju"
}

# 날씨를 한글로 바뀌는 딕셔너리
weather_dict = {"Clouds":"흐림", "Clear":"맑음", "Rain":"비", "Snow":"눈", "Mist":"안개"}

# 사용자 입력박스
#city = st.text_input("도시 이름을 영어로 입력하세요 (예:서울,부산)","서울")

# 세션에 대화 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def get_weather(city_name):
    #st.write(city_name,API_KEY)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=kr"
    response = requests.get(url)
    #st.write(response.json())
    return response.json()

if prompt := st.chat_input("도시 이름을 입력하세요 (예:서울)"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 날씨를 검색할 도시를 입력받으면 검색 시작
    with st.chat_message("assistant"):    
        Eng_city = city_map[prompt, prompt]
        weather_data = get_weather(Eng_city)
        # st.write(weather_data)
    
        # 도시출력
        #st.write(f"{city}의 날씨를 알려드릴게요.")
        
        if weather_data.get("cod") == 200:
        # 온도, 날씨(맑음)
            temp = round(weather_data['main']['temp'])          # 현재 기온
            temp_min = round(weather_data['main']['temp_min'])  # 최저 기온
            temp_max = round(weather_data['main']['temp_max'])  # 최고 기온
            desc = weather_data['weather'][0]['main']   # 날씨 설명
            main_weather = weather_dict[desc]
            
            reply = f"{prompt}의 현재 날씨입니다.\n\n 기온: {temp}°C\n 상태: {desc}"
            st.markdown(reply)
            st.session_state.messages.append({"role":"assistant", "content":prompt})
        else:
            reply = "입력한 도시의 날씨 정보를 찾을 수 없어요."
            st.markdown(reply)
            st.session_state.messages.append({"role":"assistant", "content":prompt})
            
