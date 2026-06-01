import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울시 연령별 인구",
    layout="wide"
)

st.title("서울시 연령별 인구 분석")

# 데이터 불러오기
df = pd.read_csv("aaa.csv")

# 첫 번째 컬럼을 행정구명으로 사용
region_col = df.columns[0]

# 연령 컬럼
age_columns = [
    '0~9세',
    '10~19세',
    '20~29세',
    '30~39세',
    '40~49세',
    '50~59세',
    '60~69세',
    '70~79세',
    '80~89세',
    '90~99세',
    '100세 이상'
]

# 숫자형 변환
for col in age_columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(',', '')
        .astype(float)
    )

# 행정구 선택
selected_region = st.selectbox(
    "행정구 선택",
    df[region_col].unique()
)

# 선택 데이터
row = df[df[region_col] == selected_region].iloc[0]

ages = age_columns
population = [row[col] for col in age_columns]

# 그래프
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=ages,
        y=population,
        mode="lines+markers",
        line=dict(
            color="red",
            width=4
        ),
        marker=dict(
            size=10,
            color="red"
        ),
        name="인구수"
    )
)

# 배경 파란색
fig.update_layout(
    title=f"{selected_region} 연령별 인구",
    xaxis_title="나이",
    yaxis_title="인구수",
    plot_bgcolor="lightblue",
    paper_bgcolor="white",
    height=600,
    font=dict(size=14)
)

st.plotly_chart(fig, use_container_width=True)

# 데이터 보기
st.subheader("연령별 인구수")

display_df = pd.DataFrame({
    "나이대": ages,
    "인구수": population
})

st.dataframe(
    display_df,
    use_container_width=True
)
