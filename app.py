import streamlit as st
import openai
from docx import Document

# Streamlit 설정
st.set_page_config(page_title="AI 수업 코칭 도우미", layout="centered")

# GPT API 키 불러오기 (secrets.toml에서 관리)
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("📘 AI 수업 코칭 도우미")
st.write("수업 대본(.txt 또는 .docx)을 업로드하고, 교실 상황을 선택하면 AI가 피드백을 제공합니다.")

# 선택 옵션 UI
teacher_style = st.multiselect("교사 스타일", [
    "정적인 수업", "활동적인 수업", "언변이 좋음", "자료 정리에 강점 있음"
])

classroom_status = st.multiselect("학급 상황", [
    "산만한 학생 50% 이상", "학습부진 학생 50% 이상", "도전적 행동을 보이는 학생 있음"
])

coaching_focus = st.multiselect("코칭 요청 항목", [
    "수업 참여 유도", "발문 전략", "상호작용 개선", "수업 구조 조언"
])

uploaded_file = st.file_uploader("수업 대본 업로드 (.txt 또는 .docx)", type=["txt", "docx"])

# 파일 처리
def read_text_file(file):
    return file.read().decode("utf-8")

def read_docx_file(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

# GPT 요청
def generate_feedback(text, style, status, focus):
    prompt = f"""
너는 중학교 교실 수업을 분석해주는 AI 코치야.
아래 교사 스타일, 학급 상황, 요청 항목을 바탕으로 수업 대본을 분석하고 구체적인 피드백과 개선점을 제시해줘.

[교사 스타일] {', '.join(style)}
[학급 상황] {', '.join(status)}
[코칭 요청 항목] {', '.join(focus)}

[수업 대본]
{text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 실행 버튼
if st.button("🧠 AI 코칭 받기") and uploaded_file:
    if uploaded_file.name.endswith(".txt"):
        text = read_text_file(uploaded_file)
    else:
        text = read_docx_file(uploaded_file)

    with st.spinner("AI가 수업을 분석 중입니다..."):
        feedback = generate_feedback(text, teacher_style, classroom_status, coaching_focus)

    st.subheader("📝 AI 코칭 피드백")
    st.write(feedback)
