import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="서울 관광지 TOP10",
    layout="wide"
)

st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP10")
st.write("마커에 마우스를 올리면 가까운 지하철역이 표시됩니다.")

# 서울 중심 지도
seoul_map = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

# 관광지 데이터
tour_places = [
    {
        "name": "경복궁",
        "lat": 37.5796,
        "lon": 126.9770,
        "station": "경복궁역",
        "fun": "한복 체험과 궁궐 관람"
    },
    {
        "name": "N서울타워",
        "lat": 37.5512,
        "lon": 126.9882,
        "station": "명동역",
        "fun": "서울 야경과 케이블카"
    },
    {
        "name": "명동",
        "lat": 37.5636,
        "lon": 126.9820,
        "station": "명동역",
        "fun": "쇼핑과 길거리 음식"
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9236,
        "station": "홍대입구역",
        "fun": "버스킹과 맛집 탐방"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.5131,
        "lon": 127.1025,
        "station": "잠실역",
        "fun": "전망대와 쇼핑"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.5826,
        "lon": 126.9830,
        "station": "안국역",
        "fun": "전통 한옥 체험"
    },
    {
        "name": "동대문디자인플라자",
        "lat": 37.5665,
        "lon": 127.0092,
        "station": "동대문역사문화공원역",
        "fun": "야경과 전시회"
    },
    {
        "name": "코엑스",
        "lat": 37.5125,
        "lon": 127.0588,
        "station": "삼성역",
        "fun": "별마당 도서관과 쇼핑"
    },
    {
        "name": "광장시장",
        "lat": 37.5704,
        "lon": 126.9997,
        "station": "종로5가역",
        "fun": "빈대떡과 먹거리"
    },
    {
        "name": "이태원",
        "lat": 37.5347,
        "lon": 126.9946,
        "station": "이태원역",
        "fun": "세계 음식과 문화"
    }
]

# 마커 추가
for place in tour_places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=place["name"],
        tooltip=f"가까운 지하철역: {place['station']}",
        icon=folium.Icon(color="red")
    ).add_to(seoul_map)

# 지도 출력
st_folium(seoul_map, width=1000, height=600)

# 설명
st.markdown("---")
st.subheader("📍 관광지 정보")

for idx, place in enumerate(tour_places, start=1):
    st.markdown(f"### {idx}. {place['name']}")
    st.write(f"🚇 가까운 지하철역: {place['station']}")
    st.write(f"🎈 놀거리: {place['fun']}")
    st.markdown("---")
