import streamlit as st
from datetime import datetime

today = st.date_input("날짜를 선택하세요.")
current_time = st.time_input("시간을 선택하세요")

st.write(f'선택한 날짜: {today}')
st.write(f'선택한 시간: {current_time}')

# 날짜는 달력 형태로 나오네. 신기하다.
# 시간은 15분 단위로 00 ~ 24시까지 선택이 가능하네.