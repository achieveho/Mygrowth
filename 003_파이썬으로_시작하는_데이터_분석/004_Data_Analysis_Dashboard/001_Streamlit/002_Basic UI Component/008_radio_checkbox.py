import streamlit as st

color = st.radio(
    '좋아하는 색을 선택하세요.',
    ['빨강', '파랑', '초록']
)

agree = st.checkbox("체크박스를 누르면 이용약관에 동의하게 되는 것 입니다.")

if agree:
    st.write("동의해주셔서 감사합니다.")