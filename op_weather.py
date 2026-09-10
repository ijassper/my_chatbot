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

# 사용자 입력박스
city = st.text_input("도시 이름을 영어로 입력하세요 (예:Seoul,Busan)","Seoul")

def get_weather(city_name):
    #st.write(city_name,API_KEY)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=kr"
    response = requests.get(url)
    #st.write(response.json())
    return response.json()

# 날씨를 검색할 도시를 입력받으면 검색 시작
if city:    
    Eng_city = city_map[city]
    weather_data = get_weather(Eng_city)
    st.write(weather_data)

    # 도시출력
    st.write(f"{city}의 날씨를 알려드릴게요.")
    # 온도, 날씨(맑음)
    temp = int(weather_data['main']['temp'])          # 현재 기온
    temp_min = int(weather_data['main']['temp_min'])  # 최저 기온
    temp_max = int(weather_data['main']['temp_max'])  # 최고 기온
    desc = weather_data['weather'][0]['main']   # 날씨 설명
    
    st.write(f"🌡️ 현재 기온: {temp}°C")
    st.write(f"🔽 최저 기온: {temp_min}°C")
    st.write(f"🔼 최고 기온: {temp_max}°C")
    st.write(f"☁️ 날씨 상태: {desc}")

