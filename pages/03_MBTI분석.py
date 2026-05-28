import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(
    page_title="국가별 MBTI 분석",
    layout="centered"
)

st.title("🌍 국가별 MBTI 비율 분석")

# CSV 파일 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 국가 선택
country = st.selectbox(
    "국가를 선택하세요",
    df["Country"].unique()
)

# 선택한 국가 데이터
selected_row = df[df["Country"] == country]

# MBTI 데이터만 추출
mbti_data = selected_row.drop(columns=["Country"]).iloc[0]

# 내림차순 정렬
mbti_sorted = mbti_data.sort_values(ascending=False)

# 색상 설정
colors = ["blue"] + ["lightcoral"] * (len(mbti_sorted) - 1)

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    mbti_sorted.index,
    mbti_sorted.values * 100,
    color=colors
)

# 그래프 꾸미기
ax.set_title(f"{country} MBTI 비율", fontsize=18)
ax.set_xlabel("MBTI 유형", fontsize=12)
ax.set_ylabel("비율 (%)", fontsize=12)

# 값 표시
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.3,
        f"{height:.1f}%",
        ha='center',
        fontsize=9
    )

plt.xticks(rotation=45)

st.pyplot(fig)

# 가장 높은 MBTI 출력
top_mbti = mbti_sorted.idxmax()
top_value = mbti_sorted.max() * 100

st.success(
    f"🏆 {country}의 대표 MBTI는 **{top_mbti}** ({top_value:.1f}%) 입니다."
)
