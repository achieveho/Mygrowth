import streamlit as st

hobbies = st.multiselect(
    "취미를 선택하세요. (여러 개 선택 가능)",
    ['독서', '영화 감상', '운동', '여행', '음악 감상']
)

if hobbies:
    st.write("선택한 취미:", hobbies)