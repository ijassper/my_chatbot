import streamlit as st
import requests

# API 키 설정
API_KEY = "8464cff4dd30fe09c5447727526f939a"

st.title("우리동네 날씨챗봇")
st.write("도시 이름을 잊력하면 현재 날씨를 알려드려요.")

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
    weather_data = get_weather(city)
    #st.write(weather_data)

    # 도시출력
    st.write(f"{city}의 날씨를 알려드릴게요.")
    # 온도, 날씨(맑음)
    st.write(f"온도 : {weather_data['main']['temp']} C")
    #st.write(f"날씨 : {weather_data['weather'][0]['description']}")

