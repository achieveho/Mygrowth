from __future__ import annotations

import io
import math
import time
from datetime import date, datetime, time as dtime, timedelta

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

import streamlit.components.v1 as components

try:
    import altair as alt
except ImportError:
    alt = None

try:
    import plotly.express as px
except ImportError:
    px = None

try:
    import pydeck as pdk
except ImportError:
    pdk = None


# ------------------------------------------------------------
# 0. Page config
# ------------------------------------------------------------
st.set_page_config(
    page_title="Streamlit 올인원 실습 앱",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ------------------------------------------------------------
# 1. Helper functions
# ------------------------------------------------------------
def has_streamlit_api(name: str) -> bool:
    """현재 설치된 Streamlit 버전에 특정 API가 있는지 확인합니다."""
    return hasattr(st, name)

@st.cache_data(ttl=600, show_spinner="데모 데이터를 생성하는 중입니다...")
def make_demo_dataframe(n: int = 200, seed: int = 42) -> pd.DataFrame:
    """
    st.cache_data 예제:
    같은 인자로 다시 호출하면 데이터 생성 결과를 캐시합니다.
    데이터프레임, API 조회 결과, DB 쿼리 결과 캐싱에 적합합니다.
    """
    rng = np.random.default_rng(seed)

    start = pd.Timestamp("2026-01-01")
    dates = pd.date_range(start, periods=n, freq="D")

    df = pd.DataFrame(
        {
            "date": dates,
            "age": rng.integers(20, 80, size=n),
            "sex": rng.choice(["M", "F"], size=n),
            "department": rng.choice(["내과", "외과", "소아과", "정형외과", "응급의학과"], size=n),
            "visits": rng.poisson(lam=30, size=n),
            "cost": rng.normal(loc=120_000, scale=35_000, size=n).round(0),
            "risk_score": rng.beta(a=2, b=5, size=n).round(3),
        }
    )

    df["cost"] = df["cost"].clip(lower=10_000)
    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df

@st.cache_resource(show_spinner="전역 리소스를 초기화하는 중입니다...")
def get_fake_model_resource() -> dict:
    """
    st.cache_resource 예제:
    ML 모델, DB connection, tokenizer처럼 앱 전체에서 공유할 무거운 객체에 적합합니다.
    """
    return {
        "model_name": "demo-risk-score-model",
        "loaded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "version": "0.0.1-demo"
    }

def make_sample_image(width: int = 500, height: int = 220) -> Image.Image:
    """st.image 예제용 샘플 이미지 생성"""
    img = Image.new("RGB", (width, height), color=(245, 245, 245))
    draw = ImageDraw.Draw(img)
    draw.rectangle((40, 40, width - 40, height - 40), outline=(80, 80, 80), width = 3)
    draw.text((60, 85), "Streamlit Image Demo", fill=(20, 20, 20))
    draw.text((60, 120), "PIL로 생성한 이미지입니다.", fill=(20, 20, 20))
    return img

def make_audio_array(duration_sec: float = 1.5, sample_rate: int = 44_100) -> np.ndarray:
    """st.audio 예제용 사인파 생성"""
    t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), endpoint=False)
    frequency = 440
    audio = 0.25 * np.sin(2 * np.pi * frequency * t)
    return audio

def dataframe_to_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8-sig")


# ------------------------------------------------------------
# 2. Session State 초기화
# ------------------------------------------------------------
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "assistant", "content": "안녕하세요. 저는 Streamlit 메모 챗봇입니다."}
    ]

if "form_submissions" not in st.session_state:
    st.session_state.form_submissions = []


# ------------------------------------------------------------
# 3. Sidebar
# ------------------------------------------------------------
with st.sidebar:
    st.title("🧭 Streamlit 메뉴")
    st.caption("왼쪽 옵션을 바꿔보면서 앱이 어떻게 다시 실행되는지 확인해보세요.")

    selected_section = st.radio(
        "실습 섹션 선택",
        [
            "전체 개요",
            "텍스트 / Markdown / HTML",
            "데이터 / 테이블 / 편집",
            "차트 / 지도",
            "입력 위젯",
            "레이아웃 / 컨테이너",
            "미디어 / 파일",
            "상태 표시 / 실행 흐름",
            "Session State / Cache",
            "Chat UI",
            "DB / Secrets / Multipage 템플릿",
        ],
    )

    st.divider()

    sidebar_department = st.multiselect(
        "부서 필터",
        ["내과", "외과", "소아과", "정형외과", "응급의학과"],
        default=["내과", "외과", "소아과", "정형외과", "응급의학과"],
    )

    sidebar_min_age, sidebar_max_age = st.slider(
        "연령 범위",
        min_value=20,
        max_value=80,
        value=(20, 80),
    )

    sidebar_show_raw = st.checkbox("원본 데이터 표시", value=False)

    if has_streamlit_api("toggle"):
        sidebar_dark_hint = st.toggle("토글 예제", value=False)
        st.caption(f"토글 상태: {sidebar_dark_hint}")
    
    picked_color = st.color_picker("색상 선택 예제", "#3B82F6")
    st.caption(f"선택한 색상: {picked_color}")


# ------------------------------------------------------------
# 4. Data 준비
# ------------------------------------------------------------
df = make_demo_dataframe()

filtered_df = df[
    df["department"].isin(sidebar_department)
    & df["age"].between(sidebar_min_age, sidebar_max_age)
].copy()


# ------------------------------------------------------------
# 5. Header
# ------------------------------------------------------------
st.title("🧪 Streamlit 올인원 실습 앱")
st.caption(
    "텍스트, 데이터프레임, 차트, 입력 위젯, 파일 업로드, 상태 관리, 캐시, 채팅 UI 등을 한 파일에서 연습합니다."
)

if sidebar_show_raw:
    st.info("사이드바의 '원본 데이터 표시' 옵션이 켜져 있습니다.")


# ------------------------------------------------------------
# 6. Sections
# ------------------------------------------------------------
if selected_section == "전체 개요":
    st.header("1. 전체 개요")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("행 수", f"{len(filtered_df):,}")
    c2.metric("평균 연령", f"{filtered_df['age'].mean():.1f}세")
    c3.metric("평균 비율", f"{filtered_df['cost'].mean():,.0f}원")
    c4.metric("평균 위험점수", f"{filtered_df['risk_score'].mean():.3f}")

    st.divider()

    st.subheader("현재 앱에서 실습하는 핵심 기능")
    st.markdown(
        """
        - **텍스트 출력**: title, header, markdown, code, latex, caption
        - **데이터 표시**: dataframe, table, data_editor, metric, json
        - **차트**: line, area, bar, scatter, matplotlib, Altair, Plotly, map
        - **입력 위젯**: button, chekcbox, radio, selectbox, slider, form, file_uploader 등
        - **레이아웃**: sidebar, columns, tabs, expander, container, popover
        - **미디어**: image, audio, video, camera input, audio input
        - **상태 관리**: session_state, query_params
        - **성능 최적화:** cache_data, cache_resource
        - **채팅 UI**: chat_message, chat_input
        """
    )

    st.subheader("필터링 된 데이터 미리보기")
    st.dataframe(filtered_df.head(20), use_container_width=True)

    csv_bytes = dataframe_to_csv_bytes(filtered_df)
    st.download_button(
        label="필터링 된 데이터 CSV 다운로드",
        data=csv_bytes,
        file_name="filtered_streamlit_demo_data.csv",
        mime="text/csv",
    )

elif selected_section == "텍스트 / Markdown / HTML":
    st.header("2. 텍스트 / Markdown / HTML")

    st.title("st.title 예제")
    st.header("st.header 예제")
    st.subheader("st.subheader 예제")
    st.caption("st.caption 예제: 보조 설명을 작게 표시합니다.")

    st.markdown(
        """
        ### Markdown 예제
        
        Streamlit은 Markdown 문법을 지원합니다.
        
        - **굵게**
        - *기울임*
        - 'inline code'
        - [Streamlit 공식 문서](https://docs.streamlit.io/)
        """
    )

    if has_streamlit_api("badge"):
        st.badge("New")
    
    st.text("st.text 예제: 고정폭 일반 텍스트입니다.")

    st.code(
    """
    import streamlit as st

    st.title("Hello Streamlit!")
    st.write("Python code가 웹 앱이 됩니다.")
    """,
    language="python",
    )

    st.latex(r"""
             \bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i
             """)
    
    st.json(
        {
            "tool": "Streamlit",
            "purpose": "Data App",
            "user_level": "beginner",
            "features": ["UI", "charts", "widgets", "cache", "state"],
        }
    )

    st.divider()

    st.subheader("HTML 렌더링")
    html_text = """
    <div style="padding: 1rem; border: 1px solid #ddd; border-raduis: 12px;">
        <h3 style="margin: 0;">HTML 박스</h3>
        <p>Streamlit에서 HTML을 렌더링하는 예제입니다.</p>
    </div>
    """

    if has_streamlit_api("html"):
        st.html(html_text)
    else:
        components.html(html_text, height=150)

    with st.expander("st.help 예제 열기"):
        st.help(pd.DataFrame)

elif selected_section == "데이터 / 테이블 / 편집":
    st.header("3. 데이터 / 테이블 / 편집")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["dataframe", "table", "data_editor", "column_config"]
    )

    with tab1:
        st.subheader("st.dataframe")
        st.dataframe(filtered_df, use_container_width=True)

    with tab2:
        st.subheader("st.table")
        st.table(filtered_df.head(10))

    with tab3:
        st.subheader("st.data_editor")
        st.caption("셀을 직접 수정해보세요. 수정된 결과는 edited_df 변수에 저장됩니다.")

        edited_df = st.data_editor(
            filtered_df.head(20),
            num_rows="dynamic",
            use_container_width=True,
        )

        st.write("수정된 데이터:")
        st.dataframe(edited_df, use_container_width=True)
    
    with tab4:
        st.subheader("st.column_config")
        configured_df = filtered_df.head(30)

        st.dataframe(
            configured_df,
            column_config={
                "cost": st.column_config.NumberColumn(
                    "진료비",
                    help="원 단위 비율",
                    min_value=0,
                    format="%d원"
                ),
                "risk_score": st.column_config.ProgressColumn(
                    "위험 점수",
                    help="0~1 사이 위험 점수",
                    min_value=0,
                    max_value=1,
                    format="%.3f",
                ),
                "date": st.column_config.DateColumn("방문일"),
            },
            use_container_width=True,
            hide_index=True,
        )    
    
    st.divider()

    st.subheader("집계 예제")
    summary = (
        filtered_df.groupby("department", as_index=False)
        .agg(
            count=("department", "size"),
            mean_age=("age", "mean"),
            mean_cost=("cost", "mean"),
            mean_risk=("risk_score", "mean"),
        )
        .round(2)
    )

    st.dataframe(summary, use_container_width=True)

elif selected_section == "차트 / 지도":
    st.header("4. 차트 / 지도")

    chart_df = (
        filtered_df.groupby("date", as_index=False)
        .agg(visits=("visits", "sum"), cost=("cost", "mean"), risk_score=("risk_score", "mean"))
        .sort_values("date")
    )

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["기본 차트", "Matplotlib", "Altair", "Plotly", "지도", "PyDeck"]
    )

    with tab1:
        st.subheader("Streamlit 기본 차트")

        numeric_chart_df = chart_df.set_index("date")[["visits", "risk_score"]]

        st.write("st.line_chart")
        st.line_chart(numeric_chart_df)

        st.write("st.area_chart")
        st.area_chart(numeric_chart_df)

        st.write("st.bar_chart")
        dept_count = filtered_df["department"].value_counts()
        st.bar_chart(dept_count)

        if has_streamlit_api("scatter_chart"):
            st.write("st.scatter_chart")
            scatter_df = filtered_df[["age", "cost", "risk_score"]].copy()
            st.scatter_chart(scatter_df, x="age", y="cost", size="risk_score")

    with tab2:
        st.subheader("Matplotlib 차트")

        fig, ax = plt.subplots(figsize=(8, 4))
        dept_cost = filtered_df.groupby("department")["cost"].mean().sort_values()
        ax.bar(dept_cost.index, dept_cost.values)
        ax.set_title("부서별 평균 진료비")
        ax.set_xlabel("부서")
        ax.set_ylabel("평균 진료비")
        ax.tick_params(axis="x", roattion=30)
        fig.tight_layout()

        st.pyplot(fig)

    with tab3:
        st.subheader("Altair 차트")

        if alt is None:
            st.warning("Altair가 설치되어 있지 않습니다. 'python -m pip install altair'을 실행하세요.")
        else:
            alt_chart = (
                alt.Chart(filtered_df)
                .mark_circle(size=70)
                .encode(
                    x="age",
                    y="cost",
                    color="department",
                    tooltip=["date", "age", "sex", "department", "cost", "risk_score"],
                )
                .interactive()
            )
            st.altair_chart(alt_chart, use_container_width=True)
    
    with tab4:
        st.subheader("Plotly 차트")

        if px is None:
            st.warning("Plotly가 설치되어 있지 않습니다. 'python -m pip install plotly'를 실행하세요.")
        else:
            fig = px.scatter(
                filtered_df,
                x="age",
                y="cost",
                color="departments",
                size="risk_score",
                hover_data=["date", "sex", "visits"],
                title="연령, 진료비, 위험점수 산점도"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab5:
        st.subheader("st.map")

        map_df = pd.DataFrame(
            {
                "lat": [37.5665, 37.5796, 37.5512, 37.5172],
                "lon": [126.9780, 126.9770, 126.9882, 127.0473],
                "name": ["서울시청", "경복궁", "남산", "강남구청"],
            }
        )

        st.dataframe(map_df, use_container_width=True)
        st.map(map_df, latitude="lat", longitude="lon")
    
    with tab6:
        st.subheader("PyDeck 지도")

        if pdk is None:
            st.warning("PyDeck이 설치되어 있지 않습니다. 'python -m pip install pydeck'을 실행하세요.")
        else:
            layer = pdk.Layer(
                "ScatterplotLayer",
                data=pd.DataFrame(
                    {
                        "lat": [37.5665, 37.5796, 37.5512, 37.5172],
                        "lon": [126.9780, 126.9770, 126.9882, 127.0473],
                        "size": [300, 200, 250, 220],
                    }
                ),
                get_position="[lon, lat]",
                get_radius="size",
                pickable=True,
            )

            view_state = pdk.ViewState(
                latitude=37.5665,
                longitude=126.9780,
                zoom=11,
                pitch=0,
            )

            st.pydeck_chart(
                pdk.Deck(
                    layers=[layer],
                    initial_view_state=view_state,
                    tooltip={"text": "위도: {lat}\n경도: {lon}"},
                )
            )

elif selected_section == "입력 위젯":
    st.header("5. 입력 위젯")

    st.subheader("기본 입력 위젯")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("이름 입력", value="성호님")
        memo = st.text_area("메모 입력", value="Streamlit을 공부하고 있습니다.")
        age = st.number_input("나이", min_value=0, max_value=120, value=25)
        score = st.slider("점수", min_value=0, max_value=100, value=80)
        birth = st.date_input("날짜 선택", value=date.today())
        meeting_time = st.time_input("시간 선택", value=dtime(9, 0))

        if has_streamlit_api("datetime_input"):
            schedule_dt = st.datetime_input("날짜+시간 선택", value=datetime.now())
            st.write("선택한 날짜+시간:", schedule_dt)
    
    with col2:
        agree = st.checkbox("동의 여부", value=True)
        gender = st.radio("성별 코드 예제", ["1", "2"], horizontal=True)
        department = st.selectbox("부서 선택", ["내과", "외과", "소아과", "정형외과", "응급의학과"])
        departments = st.multiselect(
            "여러 부서 선택",
            ["내과", "외과", "소아과", "정형외과", "응급의학과"],
            default=["내과", "외과"],
        )
        size = st.select_slider("크기 선택", options=["XS", "S", "M", "L", "XL"], value="M")

        if has_streamlit_api("piils"):
            st.pills("pills 예제", ["Python", "R", "SQL", "Streamlit"], selection_mode="multi")

        if has_streamlit_api("segmented_control"):
            st.segmented_control("segmented_control 예제", ["전체", "정상", "주의", "위험"])
        
        if has_streamlit_api("feedback"):
            st.feedback("stars")
    
    st.divider()

    st.subheader("버튼 계열")

    b1, b2, b3, b4 = st.columns(4)

    with b1:
        if st.button("일반 버튼"):
            st.session_state.click_count += 1
            st.success("버튼을 클릭했습니다.")
    
    with b2:
        st.download_button(
            "CSV 다운로드",
            data=dataframe_to_csv_bytes(filtered_df),
            file_name="demo.csv",
            mime="text/csv", 
        )
    
    with b3:
        if has_streamlit_api("link_button"):
            st.link_button("공식 문서 열기", "https://docs.streamlit.io/")

    with b4:
        if has_streamlit_api("menu_button"):
            selected_menu = st.menu_button("메뉴 버튼", options=["CSV", "JSON", "PDF"])
            st.write("선택:", selected_menu)
        else:
            st.caption("현재 설치된 Streamlit 버전에 st.menu_button이 없습니다.")

    st.write("현재 클릭 횟수:", st.session_state.click_count)

    st.divider()

    st.subheader("Form 예제")
    st.caption("form 안의 입력값은 submit 버튼을 누를 때 한 번에 처리됩니다.")

    with st.form("profile_form"):
        form_name = st.text_input("이름", value=name)
        form_role = st.selectbox("역할", ["학생", "데이터 분석가", "개발자", "연구자"])
        form_goal = st.text_area("목표", value="헬스케어 데이터 분석 역량 강화")
        submitted = st.form_submit_button("제출")

    if submitted:
        st.session_state.form_submissions.append(
            {
                "name": form_name,
                "role": form_role,
                "goal": form_goal,
                "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        st.success("Form이 제출되었습니다.")

    st.write("제출 기록:")
    st.json(st.session_state.form_submissions)

elif selected_section == "레이아웃 / 컨테이너":
    st.header("6. 레이아웃 / 컨테이너")

    st.subheader("Columns")
    c1, c2, c3 = st.columns([1, 2, 3])

    c1.info("왼쪽 컬럼")
    c2.success("가운데 컬럼")
    c3.warning("오른쪽 컬럼")

    st.subheader("Container")
    container = st.container(border=True)
    container.write("이 내용은 st.container 안에 있습니다.")
    container.dataframe(filtered_df.head(5), use_container_width=True)

    st.subheader("Empty placeholder")
    placeholder = st.empty()

    if st.button("placeholder 내용 바꾸기"):
        placeholder.success("st.empty() 영역의 내용이 바뀌었습니다.")
    else:
        placeholder.info("버튼을 누르면 이 영역이 교체됩니다.")
    
    st.subheader("Expander")
    with st.expander("자세한 설명 열기"):
        st.write("접었다 펼 수 있는 영역입니다.")
        st.dataframe(filtered_df.describe(), use_container_width=True)

    if has_streamlit_api("popover"):
        st.subheader("Popover")
        with st.popover("설정 열기"):
            st.checkbox("옵션 A")
            st.checkbox("옵션 B")
            st.slider("옵션 값", 0, 10, 5)
    
    if has_streamlit_api("space"):
        st.space("medium")
    
    st.subheader("Tabs")
    t1, t2, t3 = st.tabs(["탭 1", "탭 2", "탭 3"])

    with t1:
        st.write("첫 번째 탭입니다.")
    
    with t2:
        st.line_chart(filtered_df[["visits", "risk_score"]].head(30))
    
    with t3:
        st.dataframe(filtered_df.head(10), use_container_width=True)
    
    st.divider()

    st.subheader("Dialog 예제")

    if has_streamlit_api("dialog"):
        @st.dialog("프로필 입력 Dialog")
        def profile_dialog():
            dialog_name = st.text_input("이름", value="성호님")
            dialog_goal = st.text_area("목표", value="Streamlit 학습")
            if st.button("Dialog 저장"):
                st.session_state["dialog_result"] = {
                    "name": dialog_name,
                    "goal": dialog_goal,
                }
                st.rerun()

            if st.button("Dialog 열기"):
                profile_dialog()
            
            if "dialog_result" in st.session_state:
                st.write("Dialog 결과:", st.session_state.dialog_result)
            else:
                st.caption("현재 설치된 Streamlit 버전에 st.dialog가 없습니다.")
            
elif selected_section == "미디어 / 파일":
    st.header("7. 미디어 / 파일")

    tab1, tab2, tab3, tab4 = st.tabs(["Image", "Audio", "Video/PDF", "Camera/Audio input"])

    with tab1:
        st.subheader("st.image")
        sample_img = make_sample_image()
        st.image(sample_img, caption="PIL로 생성한 샘플 이미지", use_container_width=True)

        uploaded_image = st.file_uploader(
            "이미지 파일 업로드",
            type=["png", "jpg", "jpeg"],
            key="image_uploader",
        )

        if uploaded_image is not None:
            st.image(uploaded_image, caption="업로드한 이미지", use_container_width=True)
    
    with tab2:
        st.subheader("st.audio")
        audio = make_audio_array()
        st.audio(audio, sample_rate=44_100)

        uploaded_audio = st.file_uploader(
            "오디오 파일 업로드",
            type=["wav", "mp3", "ogg"],
            key="audio_uploader",
        )

        if uploaded_audio is not None:
            st.audio(uploaded_audio)
    
    with tab3:
        st.subheader("st.video / st.pdf")

        uploaded_video = st.file_uploader(
            "비디오 파일 업로드",
            type=["mp4", "mov", "avi"],
            key="video_uploader",
        )

        if uploaded_video is not None:
            st.video(uploaded_video)
        else:
            st.info("비디오 파일을 업로드하면 st.video로 표시합니다.")
        
        uploaded_pdf = st.file_uploader(
            "PDF 파일 업로드",
            type=["pdf"],
            key="pdf_uploader",
        )

        if uploaded_pdf is not None:
            if has_streamlit_api("pdf"):
                st.pdf(uploaded_pdf)
            else:
                st.warning("현재 설치된 Streamlit 버전에 st.pdf가 없습니다.")
        else:
            st.info("PDF 파일을 업로드하면 st.pdf로 표시합니다.")
    
    with tab4:
        st.subheader("st.camera_input / st.audio_input")

        camera_image = st.camera_input("카메라로 이미지 촬영")
        if camera_image is not None:
            st.image(camera_image, caption="카메라 입력 이미지")
        
        if has_streamlit_api("audio_input"):
            recorded_audio = st.audio_input("마이크로 음성 녹음")
            if recorded_audio is not None:
                st.audio(recorded_audio)
        else:
            st.caption("현재 설치된 Streamlit 버전에 st.audio_input이 없습니다.")
            
elif selected_section == "상태 표시 / 실행 흐름":
    st.header("8. 상태 표시 / 실행 흐름")

    st.subheader("상태 메시지")
    st.success("st.success: 성공 메시지")
    st.info("st.info: 정보 메시지")
    st.warning("st.warning: 경고 메시지")
    st.error("st.error: 에러 메시지")

    try:
        raise ValueError("예제용 ValueError입니다.")
    except ValueError as e:
        with st.expander("st.exception 예제 보기"):
            st.exception(e)
    
    st.divider()

    st.subheader("Progress / Spinner / Status")

    if st.button("짧은 작업 실행"):
        progress = st.progress(0, text="작업 시작")
        for i in range(101):
            progress.progress(i, text=f"진행률: {i}%")
            time.sleep(0.005)
        
        with st.spinner("결과 정리 중..."):
            time.sleep(0.5)
        
        if has_streamlit_api("status"):
            with st.status("작업 로그", expanded=True) as status:
                st.write("1단계: 데이터 로드 완료")
                time.sleep(0.2)
                st.write("2단계: 집계 완료")
                time.sleep(0.2)
                st.write("3단계: 시각화 준비 완료")
                status.update(label="작업 완료", state="complete")
        
        st.success("작업이 완료되었습니다.")

        if has_streamlit_api("toast"):
            st.toast("작업 완료!", icon="✅")
    
    st.divider()

    st.subheader("Celebration")
    c1, c2 = st.columns(2)

    with c1:
        if st.button("풍선 효과"):
            st.balloons()
    
    with c2:
        if has_streamlit_api("snow"):
            if st.button("눈 효과"):
                st.snow()
    
    st.divider()

    st.subheader("st.rerun / st.stop")

    if st.button("클릭 횟수 초기화 후 rerun"):
        st.session_state.click_count = 0
        st.rerun()
    
    stop_app = st.checkbox("여기서 앱 실행을 중단하는 st.stop() 테스트")
    if stop_app:
        st.warning("st.stop()이 호출되어 이 아래 코드는 실행되지 않습니다.")
        st.stop()

    st.write("st.stop() 체크박스가 꺼져 있으므로 이 문장이 보입니다.")

    st.divider()

    st.subheader("st.fragment 예제")

    if has_streamlit_api("fragment"):
        @st.fragment(run_every="5s")
        def live_clock_fragment():
            st.info(f"이 영역은 fragment 예제입니다. 현재 시각: {datetime.now().strftime('%H:%M:%S')}")
        
        live_clock_fragment()
    else:
        st.caption("현재 설치된 Stremalit 버전에 st.fragment가 없습니다.")
    
elif selected_section == "Session State / Cache":
    st.header("9. Session State / Cache")

    st.subheader("Session State")
    st.write("Streamlit은 위젯 조작 때마다 스크립트를 위에서 아래로 다시 실행합니다.")
    st.write("따라서 값을 유지하려면 t.session_state를 사용해야 합니다.")

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("count + 1"):
            st.session_state.click_count += 1
    
    with c2:
        if st.button("count -1"):
            st.session_state.click_count -= 1
            
    with c3:
        if st.button("count reset"):
            st.session_state.click_count = 0
    
    st.metric("현재 count", st.session_state.click_count)

    with st.expander("현재 session_state 전체 보기"):
        st.write(dict(st.session_state))

    st.divider()

    st.subheader("Cache Data")
    st.write("make_demo_dataframe 함수는 @st.cache_data로 캐시되어 있습니다.")

    seed = st.number_input("데이터 seed", min_value=0, max_value=9999, value=42)
    n_rows = st.slider("행 수", min_value=50, max_value=1000, value=200)

    cached_df = make_demo_dataframe(n=n_rows, seed=seed)
    st.dataframe(cached_df.head(10), use_container_width=True)
    
    if st.button("cache_data 비우기"):
        make_demo_dataframe.clear()
        st.success("make_demo_dataframe 캐시를 비웠습니다.")
    
    st.divider()

    st.subheader("Cache Resource")
    resource = get_fake_model_resource()
    st.json(resource)

    if st.button("cache_resource 비우기"):
        get_fake_model_resource.clear()
        st.success("get_fake_model_resource 캐시를 비웠습니다.")
    
    st.divider()

    st.subheader("Query Params")

    st.write("현재 URL query params:")
    st.write(dict(st.query_params))

    q_value = st.text_input("URL에 저장할 demo 파라미터 값", value="streamlit")
    if st.button("query param 저장"):
        st.query_params["demo"] = q_value
        st.success("URL query param을 저장했습니다.")
    
    if st.button("query params 전체 삭제"):
        st.query_params.clear()
        st.success("URL query params를 삭제했습니다.")
    
    if has_streamlit_api("context"):
        with st.expander("st.context 정보"):
            st.write("locale:", getattr(st.context, "locale", None))
            st.write("timezone:", getattr(st.context, "timezone", None))

elif selected_section == "Chat UI":
    st.header("10. Chat UI")

    st.write("간단한 규칙 기반 챗본 예제입니다. 실제 LLM API를 연결하지는 않습니다.")

    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    prompt = st.chat_input("메시지를 입력하세요")

    if prompt:
        st.session_state.chat_messages.append(
            {"role": "user", "content": prompt}
        )

        if "안녕" in prompt:
            answer = "안녕하세요. Streamlit chat_message와 chat_input 예제입니다."
        elif "데이터" in prompt:
            answer = f"현재 필터링된 데이터는 {len(filtered_df):,}행입니다."
        elif "초기화" in prompt:
            answer = "대화 초기화는 아래 버튼을 눌러주세요."
        else:
            answer = f"입력하신 내용: {prompt}"
        
        st.session_state.chat_messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()

    if st.button("채팅 기록 초기화"):
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "채팅 기록을 초기화했습니다."}
        ]
        st.rerun()

    st.divider()

    st.subheader("st.write_stream 예제")

    def stream_text():
        text = "이 문장은 st.write_straem으로 한 글자씩 출력되는 예제입니다."
        for char in text:
            yield char
            time.sleep(0.02)
        
    if has_streamlit_api("write_stream"):
        if st.button("스트리밍 출력 실행"):
            st.write_stream(stream_text)
    else:
        st.caption("현재 설치된 Streamlit 버전에 st.write_stream이 없습니다.")
    
elif selected_section == "DB / Secrets / Multipage 템플릿":
    st.header("11. DB / Secrets / Multipage 템플릿")

    st.info(
        "이 섹션은 실제 DB, 로그인, 멀티페이지 구조를 바로 실행하기보다는 "
        "프로젝트를 확장할 때 사용하는 템플릿 코드입니다."
    )

    st.subheader("Secrets 예제")

    st.markdown(
        """
        Streamlit 프로젝트에서 API Key, DB 비밀번호 값은 민감정보는 보통
        '.streamlit/secrets.toml' 파일에 저장합니다.
        """
    )

    st.code(
        """
# .streamlit/secrets.toml 예시

[database]
url = "sqlite:///demo.db"

[api]
oepnai_api_key = "YOUR_API_KEY"
        """,
        language="toml",
    )

    try:
        secret_keys = list(st.secrets.keys())
        st.write("현재 감지된 secrets key:", secret_keys)
    except Exception as e:
        st.warning("secrets.toml이 없거나 secrets를 읽을 수 없습니다.")
        st.exception(e)
    
    st.divider()

    st.subheader("DB Connection 템플릿")

    st.code(
        """
import streamlit as st

conn = st.connection("my_database", type="sql")
df = conn_query("SELECT * FROM patients LIMIT 100")
st.dataframe(df)
        """,
        language="python",
    )

    st.caption(
        "실제 DB 연결은 SQLAlchemy 드라이버, DB URL, secrets.toml 설정이 필요할 수 있습니다."
    )

    st.divider()

    st.subheader("Multipage App 구조 예시")

    st.code(
        """
my_streamlit_project/
├── app.py
├── pages/
│   ├── 1_데이터_탐색.py
│   ├── 2_모델_예측.py
│   └── 3_리포트.py
└── .streamlit/
    └── config.toml
        """,
        language="text",
    )

    st.code(
        """
# app.py
import streamlit as st

st.set_page_config(page_title="헬스케어 데이터 앱", layout="wide")

st.title("메인 페이지")
st.page_link("pages/1_데이터_탐색.py", label="데이터 탐색")
st.page_link("pages/2_모델_예측.py", label="모델 예측")
st.page_link("pages/3_리포트.py", label="리포트")
        """,
        language="python",
    )

    if has_streamlit_api("login") and has_streamlit_api("user"):
        st.divider()
        st.subheader("Authentication 템플릿")
        st.code(
            """
import streamlit as st

if not st.user.is_logged_in:
    st.login()
else:
    st.wirte(f"Welcome, {st.user.name}")
    if st.button("Log out"):
        st.logout()
            """,
            language="python",
        )
    else:
        st.caption("현재 설치된 Streamlit 버전에 st.login / st.user API가 없을 수 있습니다.")

# ------------------------------------------------------------
# 7. Footer
# ------------------------------------------------------------
st.divider()
st.caption(
    "이 앱은 Streamlit 학습용 데모입니다. 실제 서비스에서는 입력 검증, 예외 처리, 보안, 인증, 배포 설정을 별도로 강화해야 합니다."
)