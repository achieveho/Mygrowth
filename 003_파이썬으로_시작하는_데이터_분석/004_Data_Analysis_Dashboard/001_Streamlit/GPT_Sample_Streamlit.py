import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = "첫 Streamlit 앱",
    page_icon = "📊",
    layout = "wide"
)

st.title("안녕하세요, Streamlit! 반갑습니다 :D")
st.write("이것은 제 첫 번째 Streamlit 애플리케이션입니다.")

st.divider()

name = st.text_input("이름을 입력하세요.", value = "성호님")
st.success(f"{name}, Streamlit 앱이 정상적으로 실행되고 있습니다.")

st.subheader("간단한 데이터프레임 예제")

sample_size = st.slider(
    "샘플 개수",
    min_value = 10,
    max_value = 200,
    value = 50,
    step = 10
)

df = pd.DataFrame({
    "x": np.arange(sample_size),
    "y": np.random.randn(sample_size).cumsum()
})

st.dataframe(df)

st.subheader("간단한 선 그래프")
st.line_chart(df.set_index("x"))