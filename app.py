import streamlit as st

# 페이지 설정
st.set_page_config(page_title="AI 수업 코칭 도우미", layout="centered")
st.title("📘 수업 발전을 위한 AI 코칭 도우미")

# 설명 문구 (간결하게 다듬은 버전)
st.markdown("""
이 도구는 **수업을 마친 교사가 자신의 수업을 돌아보고, 더 나은 방향을 찾기 위한 AI 기반 코칭 도우미**입니다.

AI는 교사의 전문성을 바탕으로,  
**UDL(보편적 학습 설계) 관점에서 학생 다양성을 반영한 수업 아이디어**를 함께 고민합니다.

수업의 흐름, 활동 내용, 어려움 등을 정리하며  
**더 깊이 있는 수업, 더 넓은 시야를 가진 교사로 성장해보세요.**
""")

# [1] 수업 정보
st.subheader("1️⃣ 수업 정보")
subject = "과학"
grade = "중등 1학년"
lesson_theme = st.text_input("수업 주제", placeholder="예: 기체의 부피와 압력")

# [2] 수업 내용 요약
st.subheader("2️⃣ 수업 내용 요약")
lesson_summary = st.text_area("어떤 활동과 흐름이 있었나요?", height=150)

# [3] 어려움 또는 피드백 받고 싶은 부분
st.subheader("3️⃣ 피드백 받고 싶은 부분")
feedback_focus = st.multiselect("아래 중 해당하는 항목을 선택해 주세요", [
    "도입에서 학생의 몰입이 어려웠어요",
    "학생들이 핵심 개념을 헷갈려했어요",
    "참여가 저조했어요",
    "시간이 부족했어요",
    "도전적 행동이 수업 흐름에 영향을 줬어요",
    "정리·마무리가 약했어요",
    "활동이 기대만큼 효과적이지 않았어요",
    "질문에 대한 반응이 미약했어요",
    "전반적인 흐름이 매끄럽지 않았어요"
])

# [4] 교실 특성 (선택 사항)
st.subheader("4️⃣ 교실 특성 (선택)")
class_context = st.multiselect("해당하는 상황이 있다면 선택해 주세요", [
    "산만한 학생이 많음",
    "도전적 행동 있음",
    "기초학력 미달 학생 다수",
    "정서적 어려움 있는 학생 있음",
    "자폐/ADHD 학생 포함",
    "다문화 학생 포함"
])

# (선택 사항) GPT 연동 전 확인용 출력
if st.button("AI 코칭 받기 (미리보기용)"):
    st.markdown("✅ **입력 요약**")
    st.write(f"**과목:** {subject} / **학년:** {grade}")
    st.write(f"**주제:** {lesson_theme}")
    st.write(f"**수업 내용 요약:** {lesson_summary}")
    st.write(f"**피드백 요청 항목:** {feedback_focus}")
    st.write(f"**교실 특성:** {class_context}")
    st.markdown("🚧 (GPT 연동은 아직 추가되지 않았습니다)")
