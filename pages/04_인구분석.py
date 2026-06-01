
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(
    page_title="인구분석",
    layout="wide"
)

st.title("📊 서울시 연령별 인구 분석")

# --------------------------------------------------
# CSV 읽기
# --------------------------------------------------

csv_path = Path(__file__).parent.parent / "aaa.csv"

df = None

for enc in ["utf-8", "utf-8-sig", "cp949", "euc-kr"]:
    try:
        df = pd.read_csv(csv_path, encoding=enc)
        st.success(f"파일 로드 성공 (인코딩: {enc})")
        break
    except Exception:
        continue

if df is None:
    st.error("CSV 파일을 읽을 수 없습니다.")
    st.stop()

# --------------------------------------------------
# 컬럼 확인
# --------------------------------------------------

st.write("데이터 미리보기")
st.dataframe(df.head())

region_col = df.columns[0]

# 총인구 제외
age_columns = []

for col in df.columns:
    if (
        "세" in str(col)
        and "계" not in str(col)
        and "총" not in str(col)
    ):
        age_columns.append(col)

# --------------------------------------------------
# 숫자 변환
# --------------------------------------------------

for col in age_columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace(" ", "", regex=False)
    )

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# --------------------------------------------------
# 행정구 선택
# --------------------------------------------------

selected_region = st.selectbox(
    "행정구 선택",
    df[region_col].unique()
)

row = df[df[region_col] == selected_region].iloc[0]

population = [row[col] for col in age_columns]

# --------------------------------------------------
# 그래프
# --------------------------------------------------

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=age_columns,
        y=population,
        mode="lines+markers",
        name="인구수",
        line=dict(
            color="red",
            width=4
        ),
        marker=dict(
            color="red",
            size=10
        )
    )
)

fig.update_layout(
    title=f"{selected_region} 연령별 인구",
    xaxis_title="나이",
    yaxis_title="인구수",
    plot_bgcolor="lightblue",
    paper_bgcolor="white",
    height=650,
    font=dict(size=15)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# 데이터 표
# --------------------------------------------------

st.subheader("연령별 인구수")

display_df = pd.DataFrame({
    "연령대": age_columns,
    "인구수": population
})

st.dataframe(
    display_df,
    use_container_width=True
)
