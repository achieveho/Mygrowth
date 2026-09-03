import streamlit as st

temperature = st.slider("온도를 선택하세요", 0, 40, 25)     # 0 = 최솟값, 40 = 최댓값, 25 = 기본 초깃값

st.write(f'선택한 온도는 {temperature}도 입니다.')