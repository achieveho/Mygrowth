import streamlit as st

# 좋아하는 과일 선택하기
fruit = st.selectbox(
    '좋아하는 과일을 선택하세요',
    ['사과', '바나나', '오렌지', '포도']
)

st.write(f'당신이 선택한 과일은 {fruit}입니다.')

# 터미널에서 'Ctrl + C'를 눌러 강제로 종료하니, 웹 페이지가 사라지지는 않지만 selectbox가 작동하지 않도록 변경됨.