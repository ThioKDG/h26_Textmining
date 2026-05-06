from collections import Counter
import pandas as pd

def load_corpus(datafile, col_name):
    data_df = pd.read_csv(datafile)
    # 결측치 제거 후 리스트 반환
    return data_df[col_name].dropna().tolist()

# 1. 전달받은 pos_func, my_tags, my_stopwords를 사용하도록 수정
def tokenize_korean_corpus(corpus, pos_func, my_tags, my_stopwords):
    words = []
    for review in corpus:
        # 메인에서 넘겨준 Okt().pos (pos_func)를 호출
        for word, pos in pos_func(str(review), stem=True):
            # 사용자가 지정한 태그(my_tags) 필터링
            if pos in my_tags and len(word) > 1:
                # 사용자가 지정한 불용어(my_stopwords) 필터링[cite: 1]
                if word not in my_stopwords:
                    words.append(word)
    return words

# 2. 4개의 인자를 모두 받아 tokenize 함수로 전달
def count_word_freq(corpus, pos_func, my_tags, my_stopwords):
    # 수정된 토큰화 함수 호출
    tokens = tokenize_korean_corpus(corpus, pos_func, my_tags, my_stopwords)
    return Counter(tokens)