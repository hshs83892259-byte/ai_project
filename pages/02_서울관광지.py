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
        "fun": """
• 한복 대여 후 궁궐 산책
• 근정전 및 경회루 관람
• 수문장 교대식 구경
• 국립고궁박물관 방문
"""
    },
    {
        "name": "N서울타워",
        "lat": 37.5512,
        "lon": 126.9882,
        "station": "명동역",
        "fun": """
• 서울 야경 감상
• 사랑의 자물쇠 체험
• 케이블카 탑승
• 전망대 사진 촬영
"""
    },
    {
        "name": "명동",
        "lat": 37.5636,
        "lon": 126.9820,
        "station": "명동역",
        "fun": """
• 화장품 쇼핑
• 길거리 음식 먹방
• 환전 및 쇼핑
• 카페 탐방
"""
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9236,
        "station": "홍대입구역",
        "fun": """
• 버스킹 공연 관람
• 개성 있는 카페 방문
• 맛집 탐방
• 클럽 문화 체험
"""
    },
    {
        "name": "롯데월드타워",
        "lat": 37.5131,
        "lon": 127.1025,
        "station": "잠실역",
        "fun": """
• 서울스카이 전망대
• 쇼핑몰 이용
• 석촌호수 산책
• 야경 감상
"""
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.5826,
        "lon": 126.9830,
        "station": "안국역",
        "fun": """
• 한옥 골목 산책
• 전통문화 체험
• 사진 촬영
• 공방 방문
"""
    },
    {
        "name": "동대문디자인플라자",
        "lat": 37.5665,
        "lon": 127.0092,
        "station": "동대문역사문화공원역",
        "fun": """
• 디자인 전시 관람
• 야경 촬영
• 쇼핑
• 문화 행사 참여
"""
    },
    {
        "name": "코엑스",
        "lat": 37.5125,
        "lon": 127.0588,
        "station": "삼성역",
        "fun": """
• 별마당도서관 방문
• 아쿠아리움 관람
• 쇼핑
• 맛집 탐방
"""
    },
    {
        "name": "광장시장",
        "lat": 37.5704,
        "lon": 126.9997,
        "station": "종로5가역",
        "fun": """
• 빈대떡 맛보기
• 육회 먹방
• 전통시장 체험
• 먹거리 투어
"""
    },
    {
        "name": "이태원",
        "lat": 37.5347,
        "lon": 126.9946,
        "station": "이태원역",
        "fun": """
• 세계 음식 맛보기
• 펍과 카페 방문
• 쇼핑
• 국제 문화 체험
"""
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

# 지도 출력 (기존보다 약 60% 크기)
st_folium(
    seoul_map,
    width=600,
    height=350
)

st.markdown("---")

# 관광지 선택
selected_name = st.selectbox(
    "📍 관광지를 선택하세요",
    [place["name"] for place in tour_places]
)

selected_place = next(
    place for place in tour_places
    if place["name"] == selected_name
)

# 선택 관광지 정보
st.subheader(f"🏛️ {selected_place['name']}")

st.write(f"🚇 가까운 지하철역: **{selected_place['station']}**")

st.markdown("### 🎈 놀거리")
st.markdown(selected_place["fun"])

st.markdown("### 🚉 교통 정보")
st.write(
    f"{selected_place['station']}에서 도보로 이동 가능하며 "
    "서울 지하철과 버스를 이용해 쉽게 방문할 수 있습니다."
)
