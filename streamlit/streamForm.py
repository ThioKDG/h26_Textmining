import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Streamlit 위젯 연습", layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.header("1. Input widgets 실습")
    
    
    if st.button('버튼'):
        st.success('clicked button')
    
    st.button('Go to gallery')

    
    genre = st.radio(
        "머신러닝 방법",
        ('신경망', '랜덤포레스트', 'SVM')
    )
    st.info(f"나의 선택 : {genre}")

    # 체크박스
    agree = st.checkbox('토큰화')

with col2:
    st.header(" ") 
    

    st.write("머신러닝 방법")
    option = st.selectbox(" ", ('SVM', '신경망', '랜덤포레스트'), label_visibility="collapsed")
    st.info(f"{option}")


    options = st.multiselect(
        '머신러닝 방법',
        ['랜덤포레스트', '신경망', 'SVM'],
        ['랜덤포레스트', '신경망'] # 기본 선택값
    )
    st.info(f"{options}")

    # 슬라이더
    st.write("가중치")
    weight = st.slider(" ", 0, 10, 5, label_visibility="collapsed")
    st.info(f"가중치 : {weight}")

st.divider()


st.header("2. 사용자 입력 폼 만들기")


with st.form(key='my_form'):
    st.subheader("사용자 입력 폼")
    
    name = st.text_input("이름")
    
    age = st.number_input("나이", min_value=1, max_value=100, value=1)
    is_agreed = st.checkbox("약관에 동의합니다")
    
    
    submit_button = st.form_submit_button(label='제출')


if submit_button:
    st.write(f"이름: {name}, 나이: {age}")
    if is_agreed:
        st.success("약관에 동의했습니다.")
    else:
        st.warning("약관에 동의가 필요합니다.")