import streamlit as st

st.set_page_config(page_title="MBTI 책·영화 추천", page_icon="📚", layout="centered")

st.title("📚🎬 MBTI 기반 책·영화 추천")
st.write("MBTI 유형을 선택하면 어울리는 한국 책 2권과 2000년대 외국 영화 2편을 추천합니다.")

mbti_data = {
    "INTJ": {
        "books": ["82년생 김지영 - 조남주", "채식주의자 - 한강"],
        "movies": ["인셉션 (2010)", "셜록 홈즈 (2009)"]
    },
    "INTP": {
        "books": ["아몬드 - 손원평", "나는 나로 살기로 했다 - 김수현"],
        "movies": ["인터스텔라 (2014)", "소셜 네트워크 (2010)"]
    },
    "ENTJ": {
        "books": ["미움받을 용기 - 기시미 이치로", "트렌드 코리아 - 김난도"],
        "movies": ["아이언맨 (2008)", "머니볼 (2011)"]
    },
    "ENTP": {
        "books": ["죽고 싶지만 떡볶이는 먹고 싶어 - 백세희", "완벽한 공부법 - 고영성"],
        "movies": ["캐치 미 이프 유 캔 (2002)", "울프 오브 월스트리트 (2013)"]
    },
    "INFJ": {
        "books": ["달러구트 꿈 백화점 - 이미예", "서랍에 저녁을 넣어 두었다 - 한강"],
        "movies": ["이터널 선샤인 (2004)", "라이프 오브 파이 (2012)"]
    },
    "INFP": {
        "books": ["연금술사 - 최지원 번역판", "모순 - 양귀자"],
        "movies": ["어바웃 타임 (2013)", "월터의 상상은 현실이 된다 (2013)"]
    },
    "ENFJ": {
        "books": ["꽃을 보듯 너를 본다 - 나태주", "아주 작은 습관의 힘 - 제임스 클리어 번역판"],
        "movies": ["행복을 찾아서 (2006)", "굿 윌 헌팅 (2000 재개봉)"]
    },
    "ENFP": {
        "books": ["불편한 편의점 - 김호연", "여행의 이유 - 김영하"],
        "movies": ["맘마미아! (2008)", "라라랜드 (2016)"]
    },
    "ISTJ": {
        "books": ["정의란 무엇인가 - 한국어판", "총, 균, 쇠 - 한국어판"],
        "movies": ["다크 나이트 (2008)", "벤자민 버튼의 시간은 거꾸로 간다 (2008)"]
    },
    "ISFJ": {
        "books": ["엄마를 부탁해 - 신경숙", "완득이 - 김려령"],
        "movies": ["노트북 (2004)", "원더 (2017)"]
    },
    "ESTJ": {
        "books": ["마시멜로 이야기 - 호아킴 데 포사다", "아프니까 청춘이다 - 김난도"],
        "movies": ["킹스맨 (2014)", "미션 임파서블 3 (2006)"]
    },
    "ESFJ": {
        "books": ["나미야 잡화점의 기적 - 한국어판", "보건교사 안은영 - 정세랑"],
        "movies": ["악마는 프라다를 입는다 (2006)", "러브 액츄얼리 (2003)"]
    },
    "ISTP": {
        "books": ["살인자의 기억법 - 김영하", "퇴마록 - 이우혁"],
        "movies": ["매드 맥스: 분노의 도로 (2015)", "본 아이덴티티 (2002)"]
    },
    "ISFP": {
        "books": ["82년생 김지영 - 조남주", "파과 - 구병모"],
        "movies": ["비포 선라이즈 시리즈", "코코 (2017)"]
    },
    "ESTP": {
        "books": ["하얼빈 - 김훈", "칼의 노래 - 김훈"],
        "movies": ["분노의 질주 (2001)", "카지노 로얄 (2006)"]
    },
    "ESFP": {
        "books": ["오직 두 사람 - 김영하", "달러구트 꿈 백화점 - 이미예"],
        "movies": ["위대한 쇼맨 (2017)", "맘마미아! (2008)"]
    }
}

selected_mbti = st.selectbox(
    "MBTI 유형을 선택하세요",
    list(mbti_data.keys())
)

if st.button("추천 보기"):
    result = mbti_data[selected_mbti]

    st.markdown("---")
    st.subheader(f"✨ {selected_mbti} 추천 결과")

    st.markdown("## 📚 추천 한국 책 2권")
    for idx, book in enumerate(result["books"], start=1):
        st.write(f"{idx}. {book}")

    st.markdown("## 🎬 추천 외국 영화 2편")
    for idx, movie in enumerate(result["movies"], start=1):
        st.write(f"{idx}. {movie}")

st.markdown("---")
st.caption("Streamlit Cloud에서 실행 가능한 MBTI 책·영화 추천 프로그램")
