# app.py

```python
import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광지 TOP10", layout="wide")

st.title("🌏 외국인들이 좋아하는 서울 관광지 TOP10")
st.write("지도 위 마커에 마우스를 올리면 가까운 지하철역을 확인할 수 있습니다.")

# 서울 중심 좌표
seoul_map = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "location": [37.5796, 126.9770],
        "station": "경복궁역",
        "fun": "한복 체험과 궁궐 관람이 유명합니다."
    },
    {
        "name": "N서울타워",
        "location": [37.5512, 126.9882],
        "station": "명동역",
        "fun": "서울 야경과 케이블카를 즐길 수 있습니다."
    },
    {
        "name": "명동",
        "location": [37.5636, 126.9820],
        "station": "명동역",
        "fun": "쇼핑과 길거리 음식이 유명합니다."
    },
    {
        "name": "홍대거리",
        "location": [37.5563, 126.9236],
        "station": "홍대입구역",
        "fun": "버스킹과 맛집, 카페를 즐길 수 있습니다."
    },
    {
        "name": "롯데월드타워",
        "location": [37.5131, 127.1025],
        "station": "잠실역",
        "fun": "전망대와 쇼핑몰, 아쿠아리움이 인기입니다."
    },
    {
        "name": "북촌한옥마을",
        "location": [37.5826, 126.9830],
        "station": "안국역",
        "fun": "전통 한옥 거리와 사진 촬영 명소입니다."
    },
    {
        "name": "동대문디자인플라자",
        "location": [37.5665, 127.0092],
        "station": "동대문역사문화공원역",
        "fun": "야경과 전시회, 쇼핑을 즐길 수 있습니다."
    },
    {
        "name": "코엑스",
        "location": [37.5125, 127.0588],
        "station": "삼성역",
        "fun": "별마당 도서관과 쇼핑이 유명합니다."
    },
    {
        "name": "광장시장",
        "location": [37.5704, 126.9997],
        "station": "종로5가역",
        "fun": "빈대떡과 마약김밥 같은 먹거리가 인기입니다."
    },
    {
        "name": "이태원",
        "location": [37.5347, 126.9946],
        "station": "이태원역",
        "fun": "세계 음식과 다양한 문화를 경험할 수 있습니다."
    }
]

# 빨간색 마커 추가
for place in places:
    folium.Marker(
        location=place["location"],
        tooltip=f"가까운 지하철역: {place['station']}",
        popup=place["name"],
        icon=folium.Icon(color="red")
    ).add_to(seoul_map)

# 지도 출력
st_folium(seoul_map, width=1000, height=600)

st.markdown("---")
st.subheader("📍 관광지 정보")

# 관광지 설명
for idx, place in enumerate(places, start=1):
    st.markdown(f"### {idx}. {place['name']}")
    st.write(f"🚇 가까운 지하철역: {place['station']}")
    st.write(f"🎈 놀거리: {place['fun']}")
    st.markdown("---")
```

# requirements.txt

```txt
streamlit
folium
streamlit-folium
```

# 실행 방법

1. app.py 파일 생성
2. requirements.txt 파일 생성
3. GitHub 업로드
4. Streamlit Cloud에서 배포

공식 사이트:

* Streamlit Cloud: [https://streamlit.io/cloud](https://streamlit.io/cloud)
