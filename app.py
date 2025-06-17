import streamlit as st

# 스타일 추가 (st.markdown + CSS)
st.markdown("""
    <style>
    .main-title {
        color: #003366;
        font-weight: 700;
        font-size: 36px;
        margin-bottom: 10px;
    }
    .subtitle {
        color: #00509e;
        font-weight: 500;
        font-size: 18px;
        margin-bottom: 25px;
    }
    .med-card {
        background-color: #f5f9ff;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .med-name {
        font-size: 22px;
        font-weight: 700;
        color: #002244;
    }
    .price-tag {
        font-size: 18px;
        font-weight: 600;
        color: #007acc;
        margin-left: 10px;
    }
    .caution-text {
        color: #cc0000;
        font-weight: 600;
        margin-top: 10px;
    }
    .dose-box {
        background-color: #e0f0ff;
        border-radius: 8px;
        padding: 12px;
        margin-top: 15px;
        font-weight: 600;
        color: #004080;
        width: fit-content;
    }
    </style>
""", unsafe_allow_html=True)

# 약 데이터 (대체 이미지 URL, 가격, 주의사항, 용량 포함)
medications = [
    {
    "name": "멀미약 디멘히드리네이트",
    "symptoms": ["구토", "어지러움"],
    "min_age": 6,
    "max_age": 120,
    "min_weight": 20,
    "price": 12000,
    "image": "https://images.unsplash.com/photo-1588776814546-4b6e5d31e0cc?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80",
    "caution": "졸음 유발 가능, 운전 주의",
    "dose_per_kg": 0
},
{
    "name": "소화제 메토클로프라미드",
    "symptoms": ["구토", "소화불량"],
    "min_age": 12,
    "max_age": 120,
    "min_weight": 30,
    "price": 14000,
    "image": "https://images.unsplash.com/photo-1556228724-8ff4e57a90a6?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80",
    "caution": "장기간 사용 시 신경계 부작용 주의",
    "dose_per_kg": 0
},

    {
        "name": "비타민 B 컴플렉스",
        "symptoms": ["피로"],
        "min_age": 15,
        "max_age": 120,
        "min_weight": 30,
        "price": 15000,
        "image": "https://images.unsplash.com/photo-1588776814546-4b6e5d31e0cc?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80",
        "caution": "과다 복용 시 위장 장애 가능",
        "dose_per_kg": 0
    },
    {
        "name": "에너지 영양제",
        "symptoms": ["피로"],
        "min_age": 12,
        "max_age": 120,
        "min_weight": 35,
        "price": 18000,
        "image": "https://images.unsplash.com/photo-1556228724-8ff4e57a90a6?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80",
        "caution": "카페인 함유, 저녁 복용 시 수면 방해 주의",
        "dose_per_kg": 0
    },
   {
        "name": "타이레놀 성인용",
        "symptoms": ["두통", "발열", "근육통"],
        "min_age": 12,
        "max_age": 120,
        "min_weight": 40,
        "price": 8000,
        "image": "https://images.unsplash.com/photo-1582719478147-0b0ab6e6d4b5?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80",
        "caution": "간 손상 위험이 있으므로, 24시간에 4g 초과 복용 금지",
        "dose_per_kg": 15
    },
    {
        "name": "타이레놀 어린이용",
        "symptoms": ["두통", "발열"],
        "min_age": 2,
        "max_age": 11,
        "min_weight": 12,
        "price": 6000,
        "image": "https://images.unsplash.com/photo-1590080877777-5df686f385a4?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80",
        "caution": "권장 용량 준수, 과다 복용 주의",
        "dose_per_kg": 10
    },
    {
        "name": "부루펜",
        "symptoms": ["근육통", "관절통", "염증", "발열"],
        "min_age": 6,
        "max_age": 120,
        "min_weight": 20,
        "price": 10000,
        "image": "https://images.unsplash.com/photo-1606813909353-45d78f24d214?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80",
        "caution": "위장장애 유발 가능, 식후 복용 권장",
        "dose_per_kg": 20
    },
    {
        "name": "판콜에이",
        "symptoms": ["감기", "기침", "콧물", "인후통"],
        "min_age": 15,
        "max_age": 120,
        "min_weight": 45,
        "price": 9000,
        "image": "https://images.unsplash.com/photo-1600416107916-9ff7b1961186?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80",
        "caution": "알레르기 반응 주의",
        "dose_per_kg": 0
    },
    {
        "name": "챔프 시럽",
        "symptoms": ["감기", "기침", "콧물"],
        "min_age": 1,
        "max_age": 10,
        "min_weight": 10,
        "price": 7000,
        "image": "https://images.unsplash.com/photo-1582270672829-f98ee7a72810?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80",
        "caution": "정해진 용량 엄수",
        "dose_per_kg": 5
    },
    {
        "name": "훼스탈 플러스",
        "symptoms": ["소화불량", "복통", "속쓰림"],
        "min_age": 10,
        "max_age": 120,
        "min_weight": 30,
        "price": 11000,
        "image": "https://images.unsplash.com/photo-1515125520143-349f25e258e9?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80",
        "caution": "복용 전 의사 상담 권장",
        "dose_per_kg": 0
    },
]

all_symptoms = [
    "두통", "발열", "기침", "콧물", "소화불량", "복통", "근육통",
    "관절통", "염증", "감기", "인후통", "속쓰림", "피로", "구토"
]

st.markdown('<div class="main-title">💊 맞춤형 환자 약 추천 시스템</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">나이와 몸무게, 증상에 맞는 약을 신뢰성 있게 추천해드립니다.</div>', unsafe_allow_html=True)

age = st.number_input("나이 (세)", min_value=0, max_value=120, step=1)
weight = st.number_input("몸무게 (kg)", min_value=0.0, max_value=200.0, step=0.1)

symptom_input = st.multiselect(
    "증상을 선택하세요 (복수 선택 가능)",
    all_symptoms
)

if st.button("💡 약 추천 받기"):
    if not symptom_input:
        st.warning("최소 한 개 이상의 증상을 선택해주세요.")
    else:
        matched = []
        for med in medications:
            if any(symptom in med["symptoms"] for symptom in symptom_input):
                if (med["min_age"] <= age <= med["max_age"]) and (weight >= med["min_weight"]):
                    matched.append(med)

        if matched:
            st.success(f"총 {len(matched)}개의 조건에 맞는 약 중 최대 2개를 추천합니다:")
            for med in matched[:2]:
                with st.container():
                    st.markdown('<div class="med-card">', unsafe_allow_html=True)
                    cols = st.columns([1, 2])
                    with cols[0]:
                        st.image(med["image"], width=120)
                    with cols[1]:
                        st.markdown(f'<div class="med-name">{med["name"]} <span class="price-tag">{med["price"]}원</span></div>', unsafe_allow_html=True)
                        st.markdown(f'<div class="caution-text">⚠️ 주의사항: {med["caution"]}</div>', unsafe_allow_html=True)
                        if med["dose_per_kg"] > 0:
                            dose_mg = med["dose_per_kg"] * weight
                            st.markdown(f'<div class="dose-box">💊 권장 복용량: 약 {dose_mg:.1f} mg (몸무게 기준)</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="dose-box">💊 권장 복용량: 정해진 용량으로 복용하세요.</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("조건에 맞는 약을 찾을 수 없습니다. 전문의와 상담하세요.")
