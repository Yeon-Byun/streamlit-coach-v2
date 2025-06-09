import streamlit as st

st.set_page_config(page_title="AI 수업 코칭 도우미", layout="centered")
st.title("📘 AI 수업 코칭 도우미")

st.write("아래 항목을 선택하면, 교실 상황에 맞는 수업 피드백을 AI가 제공합니다.")

# [1] 교사 스타일
st.subheader("1️⃣ 교사 스타일")
teacher_style = st.multiselect("수업 진행 방식", [
    "정적인 강의형", "활동 중심형", "토론·질문 중심형", "시청각 자료 중심형"
])
teacher_strength = st.multiselect("수업 강점", [
    "언변이 좋음", "자료 정리에 강점", "학생 참여 유도에 능숙함", "유머·몰입 유도"
])
teaching_design = st.radio("수업 설계 스타일", ["계획형(사전 준비 중심)", "즉흥형(유연한 흐름 중심)"])

# [2] 학급 특성
st.subheader("2️⃣ 학급 특성")
attention_span = st.radio("학생들의 집중 유지 수준은?", [
    "단기 유지형(~10분)", "중기 유지형(20~30분)", "장기 유지형(40분 이상)"
])
distraction_level = st.radio("산만한 학생 비율", ["30% 이하", "30~50%", "50% 이상"])
low_achievement_level = st.radio("학습부진 학생 비율", ["30% 이하", "30~50%", "50% 이상"])
challenging_behavior = st.radio("도전적 행동을 보이는 학생이 있나요?", ["있음", "없음"])
special_needs = st.multiselect("특수한 정서·행동적 요구", [
    "자폐 경향", "충동성·분노 조절 어려움", "불안·위축", "관계 미숙"
])

# [3] 수업 목표
st.subheader("3️⃣ 수업 목표 및 초점")
teaching_focus = st.multiselect("수업의 주된 목표", [
    "지식 전달", "탐구 및 문제 해결", "감정 표현·사회성", "자기조절 및 생활 기술",
    "참여와 협력", "문해력 강화", "기본학력 보장"
])

# [4] 선호 수업 형태
st.subheader("4️⃣ 선호 수업 형태 및 매체")
teaching_tools = st.multiselect("활용하고 싶은 수업 도구", [
    "디지털 매체", "활동지", "게임·퀴즈", "이야기·롤플레이", "실험·조작", "교과 융합", "개별 맞춤 활동"
])

# [5] AI 피드백 영역
st.subheader("5️⃣ AI 피드백 희망 영역")
coaching_focus = st.selectbox("어떤 분야의 피드백이 필요하신가요?", [
    "수업 도입 아이디어", "학생 참여 전략", "도전 행동 대응", "수준별 질문 제안",
    "활동지 아이디어", "정리·평가 전략", "전체 수업 흐름 구조"
])
