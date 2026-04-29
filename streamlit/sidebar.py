import streamlit as st


st.set_page_config(page_title="Sidebar 연습", layout="wide")

st.sidebar.header("설정")

user_name = st.sidebar.text_input("이름을 입력하세요")
user_age = st.sidebar.slider("나이", 0, 120, 25)
favorite_color = st.sidebar.selectbox(
    "좋아하는 색상을 선택하세요",
    ("빨강", "파랑", "초록", "노랑")
)


st.title("메인 페이지")
st.write("사이드바에서 입력한 값이 실시간으로 반영됩니다.")

if user_name:
    st.subheader(f"안녕하세요, {user_name}님!")
    st.write(f"당신의 나이는 {user_age}세이고, 좋아하는 색상은 {favorite_color}이군요!")
else:
    st.info("사이드바에 이름을 입력해 주세요.")

st.sidebar.divider() # 구분선
st.sidebar.subheader("머신러닝 설정")
genre = st.sidebar.radio("방법 선택", ('신경망', '랜덤포레스트', 'SVM'))