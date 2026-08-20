import streamlit as st
import requests

# 1. API 키 설정
API_KEY = "8464cff4dd30fe09c5447727526f939a"

st.title("🌤️ 우리 동네 날씨 챗봇")
st.write("도시 이름을 입력하면 현재 날씨를 알려드려요!")

# 2. 사용자 입력
city = st.text_input("도시 이름을 영어로 입력하세요 (예: Seoul, Busan, London)", "Seoul")

# 3. 날씨 데이터 호출 함수
def get_weather(city_name):
    # 단위: metric(섭씨), 언어: kr(한국어)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=kr"
    response = requests.get(url)
    return response.json()

# 4. 버튼 클릭 시 데이터 처리
if st.button("날씨 확인"):
    weather_data = get_weather(city)
    
    # 5. 데이터 파싱 및 출력
    if weather_data.get("cod") == 200: # 200은 성공을 의미
        main = weather_data["main"]
        weather = weather_data["weather"][0]
        
        temp = main["temp"]
        desc = weather["description"]
        humidity = main["humidity"]
        
        st.success(f"📍 {city}의 날씨 정보입니다.")
        st.write(f"🌡️ 현재 기온: {temp}°C")
        st.write(f"☁️ 상태: {desc}")
        st.write(f"💧 습도: {humidity}%")
    else:
        st.error("도시 이름을 찾을 수 없습니다. 영문으로 정확히 입력했는지 확인해주세요!")
