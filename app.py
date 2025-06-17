import streamlit as st

# 약 데이터 (이미지 URL, 가격, 주의사항, 용량 포함)
medications = [
    {
        "name": "타이레놀 성인용",
        "symptoms": ["두통", "발열", "근육통"],
        "min_age": 12,
        "max_age": 120,
        "min_weight": 40,
        "price": 8000,
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Tylenol_500mg_tablets.jpg/220px-Tylenol_500mg_tablets.jpg",
        "caution": "간 손상 위험이 있으므로, 24시간에 4g 초과 복용 금지",
        "dose_per_kg": 15  # mg/kg
    },
    {
        "name": "타이레놀 어린이용",
        "symptoms": ["두통", "발열"],
        "min_age": 2,
        "max_age": 11,
        "min_weight": 12,
        "price": 6000,
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Children%27s_tylenol_syrup.jpg",
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
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Ibuprofen-200mg-tablets.jpg",
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
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Panadol-pack.jpg",
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
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Children_syrup.jpg",
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
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/12/Medicine_bottle.jpg",
        "caution": "복용 전 의사 상담 권장",
        "dose_per_kg": 0
    },
]

# 증상 리스트 확장
all_symptoms = [
    "두통", "발열", "기침", "콧물", "소화불량", "복통", "근육통",
    "관절통", "염증", "감기", "인후통", "속쓰림", "피로", "구토"
]

st.title("💊 맞춤형 환자 약 추천 시스템")

age = st.number_input("나이 (세)", min_value=0, max_value=120, step=1)
weight = st.number_input("몸무게 (kg)", min_value=0.0, max_value=200.0, step=0.1)
location = st.selectbox("어디가 아프신가요?", ["머리", "배", "목", "관절", "기타"])
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
                st.subheader(f"{med['name']} - {med['price']}원")
                st.image(med["image"], width=150)
                st.write(f"⚠️ 주의사항: {med['caution']}")

                if med["dose_per_kg"] > 0:
                    dose_mg = med["dose_per_kg"] * weight
                    st.write(f"💊 권장 복용량: 약 {dose_mg:.1f} mg (몸무게 기준)")
                else:
                    st.write("💊 권장 복용량: 정해진 용량으로 복용하세요.")
                st.write("---")
        else:
            st.error("조건에 맞는 약을 찾을 수 없습니다. 전문의와 상담하세요.")
