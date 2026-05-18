import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", page_icon="💼", layout="centered")

st.title("💼 MBTI 기반 진로 추천 프로그램")
st.write("MBTI 유형을 선택하면 추천 진로 2가지와 관련 정보를 보여줍니다.")

mbti_data = {
    "INTJ": [
        {
            "career": "데이터 분석가",
            "major": "통계학과, 컴퓨터공학과",
            "personality": "논리적이고 분석적인 성격",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "career": "연구원",
            "major": "자연과학계열, 공학계열",
            "personality": "집중력이 높고 문제 해결을 좋아하는 성격",
            "salary": "평균 연봉 약 6,000만 원"
        }
    ],
    "INTP": [
        {
            "career": "소프트웨어 개발자",
            "major": "컴퓨터공학과",
            "personality": "창의적이고 호기심이 많은 성격",
            "salary": "평균 연봉 약 5,800만 원"
        },
        {
            "career": "대학교수",
            "major": "교육학과, 전공 관련 학과",
            "personality": "탐구심이 강하고 독립적인 성격",
            "salary": "평균 연봉 약 7,000만 원"
        }
    ],
    "ENTJ": [
        {
            "career": "경영 컨설턴트",
            "major": "경영학과",
            "personality": "리더십이 강하고 목표 지향적인 성격",
            "salary": "평균 연봉 약 7,500만 원"
        },
        {
            "career": "기업 관리자",
            "major": "경영학과, 경제학과",
            "personality": "결단력이 있고 조직 운영에 능한 성격",
            "salary": "평균 연봉 약 8,000만 원"
        }
    ],
    "ENTP": [
        {
            "career": "마케팅 기획자",
            "major": "광고홍보학과, 경영학과",
            "personality": "아이디어가 풍부하고 도전적인 성격",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "career": "창업가",
            "major": "경영학과",
            "personality": "모험을 좋아하고 창의적인 성격",
            "salary": "평균 연봉 개인 사업 규모에 따라 다양"
        }
    ],
    "INFJ": [
        {
            "career": "심리상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어나고 배려심 있는 성격",
            "salary": "평균 연봉 약 4,500만 원"
        },
        {
            "career": "작가",
            "major": "문예창작과",
            "personality": "상상력이 풍부하고 감수성이 높은 성격",
            "salary": "평균 연봉 개인 역량에 따라 다양"
        }
    ],
    "INFP": [
        {
            "career": "디자이너",
            "major": "디자인학과",
            "personality": "창의적이고 감성적인 성격",
            "salary": "평균 연봉 약 4,800만 원"
        },
        {
            "career": "사회복지사",
            "major": "사회복지학과",
            "personality": "따뜻하고 타인을 돕는 것을 좋아하는 성격",
            "salary": "평균 연봉 약 3,500만 원"
        }
    ],
    "ENFJ": [
        {
            "career": "교사",
            "major": "교육학과",
            "personality": "사람을 이끄는 능력이 뛰어난 성격",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "career": "인사 담당자",
            "major": "경영학과, 심리학과",
            "personality": "소통 능력이 좋고 친화력이 높은 성격",
            "salary": "평균 연봉 약 5,000만 원"
        }
    ],
    "ENFP": [
        {
            "career": "방송인",
            "major": "방송연예과",
            "personality": "활발하고 에너지가 넘치는 성격",
            "salary": "평균 연봉 개인 활동에 따라 다양"
        },
        {
            "career": "광고 기획자",
            "major": "광고홍보학과",
            "personality": "창의적이고 사람과의 소통을 좋아하는 성격",
            "salary": "평균 연봉 약 5,200만 원"
        }
    ],
    "ISTJ": [
        {
            "career": "회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감 있는 성격",
            "salary": "평균 연봉 약 7,000만 원"
        },
        {
            "career": "공무원",
            "major": "행정학과",
            "personality": "성실하고 안정적인 성격",
            "salary": "평균 연봉 약 4,500만 원"
        }
    ],
    "ISFJ": [
        {
            "career": "간호사",
            "major": "간호학과",
            "personality": "배려심이 깊고 책임감 있는 성격",
            "salary": "평균 연봉 약 5,000만 원"
        },
        {
            "career": "유치원 교사",
            "major": "유아교육과",
            "personality": "친절하고 인내심이 강한 성격",
            "salary": "평균 연봉 약 3,800만 원"
        }
    ],
    "ESTJ": [
        {
            "career": "경찰관",
            "major": "경찰행정학과",
            "personality": "규칙을 잘 지키고 리더십 있는 성격",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "career": "은행원",
            "major": "경제학과, 금융학과",
            "personality": "체계적이고 신뢰감 있는 성격",
            "salary": "평균 연봉 약 6,000만 원"
        }
    ],
    "ESFJ": [
        {
            "career": "호텔리어",
            "major": "호텔관광학과",
            "personality": "친절하고 서비스 정신이 뛰어난 성격",
            "salary": "평균 연봉 약 4,200만 원"
        },
        {
            "career": "승무원",
            "major": "항공서비스학과",
            "personality": "사교적이고 배려심 있는 성격",
            "salary": "평균 연봉 약 5,000만 원"
        }
    ],
    "ISTP": [
        {
            "career": "기계 엔지니어",
            "major": "기계공학과",
            "personality": "실용적이고 문제 해결 능력이 뛰어난 성격",
            "salary": "평균 연봉 약 6,000만 원"
        },
        {
            "career": "파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 판단력이 좋은 성격",
            "salary": "평균 연봉 약 8,000만 원"
        }
    ],
    "ISFP": [
        {
            "career": "플로리스트",
            "major": "원예학과",
            "personality": "감각적이고 따뜻한 성격",
            "salary": "평균 연봉 약 3,500만 원"
        },
        {
            "career": "사진작가",
            "major": "사진학과",
            "personality": "예술적 감각이 뛰어난 성격",
            "salary": "평균 연봉 개인 역량에 따라 다양"
        }
    ],
    "ESTP": [
        {
            "career": "영업 전문가",
            "major": "경영학과",
            "personality": "적극적이고 사교적인 성격",
            "salary": "평균 연봉 약 5,500만 원"
        },
        {
            "career": "스포츠 코치",
            "major": "체육학과",
            "personality": "활동적이고 도전 정신이 강한 성격",
            "salary": "평균 연봉 약 4,500만 원"
        }
    ],
    "ESFP": [
        {
            "career": "배우",
            "major": "연극영화과",
            "personality": "표현력이 풍부하고 밝은 성격",
            "salary": "평균 연봉 활동 경력에 따라 다양"
        },
        {
            "career": "이벤트 기획자",
            "major": "이벤트학과, 관광학과",
            "personality": "사람들과 어울리는 것을 좋아하는 성격",
            "salary": "평균 연봉 약 4,800만 원"
        }
    ]
}

mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("MBTI 유형을 선택하세요", mbti_list)

if st.button("진로 추천 보기"):
    st.subheader(f"✨ {selected_mbti} 추천 진로")

    careers = mbti_data[selected_mbti]

    for idx, item in enumerate(careers, start=1):
        st.markdown(f"---")
        st.markdown(f"### {idx}. {item['career']}")
        st.write(f"📚 적합한 학과: {item['major']}")
        st.write(f"😊 적합한 성격: {item['personality']}")
        st.write(f"💰 평균 연봉: {item['salary']}")

st.markdown("---")
st.caption("Streamlit Cloud에서 바로 실행 가능한 MBTI 진로 추천 앱")
