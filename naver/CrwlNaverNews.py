import NaverNewsCrawler as nnc
import streamlit as st

# 1. 데이터 보존을 위한 세션 상태 초기화
if 'news_list' not in st.session_state:
    st.session_state.news_list = []
if 'start_idx' not in st.session_state:
    st.session_state.start_idx = 1
if 'last_keyword' not in st.session_state:
    st.session_state.last_keyword = ""

st.markdown('### 📰 네이버 뉴스 크로울링')

# 2. 검색어 입력 (엔터 시 작동)
keyword = st.text_input('검색어를 입력하세요')

# 새로운 검색어 입력 시 데이터 리셋
if keyword != st.session_state.last_keyword:
    st.session_state.news_list = []
    st.session_state.start_idx = 1
    st.session_state.last_keyword = keyword

if keyword:
    # 초기 데이터가 없을 때만 첫 50개 자동 로드
    if not st.session_state.news_list:
        encText = nnc.urllib.parse.quote(keyword)
        url = f"https://openapi.naver.com/v1/search/news?query={encText}"
        for _ in range(5):
            data, _ = nnc.cralwl_naver_news(url, start=st.session_state.start_idx, display=10)
            if data:
                st.session_state.news_list.extend(data)
                st.session_state.start_idx += 10

    # 3. 결과 JSON 출력
    if st.session_state.news_list:
        st.success(f"현재 총 {len(st.session_state.news_list)} 건의 뉴스를 불러왔습니다.")
        st.json(st.session_state.news_list)
        
        # 4. 결과창 바로 아래에 '더보기' 버튼 배치
        if st.button('➕ 50개 더보기', use_container_width=True):
            encText = nnc.urllib.parse.quote(keyword)
            url = f"https://openapi.naver.com/v1/search/news?query={encText}"
            for _ in range(5):
                data, _ = nnc.cralwl_naver_news(url, start=st.session_state.start_idx, display=10)
                if data:
                    st.session_state.news_list.extend(data)
                    st.session_state.start_idx += 10
            st.rerun() # 데이터 추가 후 화면 즉시 갱신