import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import platform

def visualize_barh_graph(counter, num_word):
    # 빈도수가 높은 상위 n개 추출[cite: 2]
    top_words = counter.most_common(num_word)
    words = [x[0] for x in top_words][::-1]  # 높은 빈도가 위로 오게 역순 정렬
    counts = [x[1] for x in top_words][::-1]
    
    # 한글 폰트 설정 (OS별 처리)
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin': # macOS
        plt.rc('font', family='AppleGothic')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(words, counts, color='skyblue')
    ax.set_title(f'상위 {num_word}개 단어 빈도수')
    st.pyplot(fig)

def visualize_wordcloud(counter, num_word):
    # 상위 n개 단어를 딕셔너리로 변환
    data = dict(counter.most_common(num_word))
    
    # 폰트 경로 설정 (Windows 기준, 본인 환경에 맞춰 수정 필요)
    font_path = "C:/Windows/Fonts/malgun.ttf" 
    
    wc = WordCloud(
        font_path=font_path,
        background_color='white',
        width=800,
        height=400
    ).generate_from_frequencies(data)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off') # 축 숨기기
    st.pyplot(fig)