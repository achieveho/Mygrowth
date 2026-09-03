import streamlit as st

name = st.text_input('이름을 입력하세요')
age = st.number_input('나이를 입력하세요', min_value=0, max_value=120)

if name and age:
    st.write(f'{name}님은 {age}살 입니다.')

# max_value를 초과하는 값을 입력하니 적용이 되지 않고, 에러 박스가 보임.