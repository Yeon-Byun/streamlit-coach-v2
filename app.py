import streamlit as st
import openai
from openai import OpenAI  # ✅ 추가

# 🔐 비밀번호 입력
password = st.text_input("비밀번호를 입력하세요", type="password")
if password != st.secrets["app_password"]:
    st.warning("비밀번호가 틀렸거나 입력되지 않았습니다.")
    st.stop()

# 🧠 GPT 키 설정
client = OpenAI(api_key=st.secrets["openai_api_key"])  # ✅ 여기도 수정

st.title("🧑‍🏫 수업 피드백 코칭 도우미")
lesson_summary = st.text_area("📘 수업 요약을 입력해 주세요", height=200)

if st.button("✍ GPT 피드백 생성"):
    if not lesson_summary.strip():
        st.warning("수업 요약을 먼저 입력해 주세요.")
    else:
        with st.spinner("피드백 생성 중..."):
            prompt = f"""
당신은 초등학교 또는 중학교 교사입니다. 다음은 수업 요약입니다.  
이 수업을 본 교사가 다음 수업을 준비할 수 있도록 따뜻하고 구체적인 피드백을 3문장 이내로 작성해 주세요.  
[수업 요약]  
{lesson_summary}
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "당신은 교육 전문가입니다."},
                        {"role": "user", "content": prompt}
                    ]
                )
                feedback = response.choices[0].message.content
                st.success("📝 GPT 피드백:")
                st.write(feedback)
            except Exception as e:
                st.error(f"⚠️ 오류 발생: {e}")
