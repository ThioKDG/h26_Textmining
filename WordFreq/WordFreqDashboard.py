import streamlit as st
import mylib.myTextAnalyzer as ta
import mylib.myStreamlitVisualizer as sv
from konlpy.tag import Okt

# 단어수 20개
# 다음 영화 리뷰
datafile = "./data/daum_movie_review.csv"
# 1. 데이터 준비
corpus = ta.load_corpus(datafile, 'review')
# 2. 빈도수 만들기
my_tags = ['Noun', 'Verb', 'Adjective']
my_stopwords = ['제', '하는', '때', '나', '내', '내내', '티', '은', '는']
counter = ta.count_word_freq(corpus, Okt().pos, my_tags, my_stopwords)
st.markdown('### 다음 영화 리뷰 분석 데이터')
# 3. 수평 막대그래프
st.markdown('#### 수평 막대그래프')
sv.visualize_barh_graph(counter, 20)
# 4. 워드 클라우드
st.markdown('#### 워드클라우드')
sv.visualize_wordcloud(counter, 50)