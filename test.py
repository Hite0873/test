import streamlit as st
import random

# 1. 세션 상태(Session State) 초기화
# 페이지가 새로고침되어도 데이터가 날아가지 않도록 보존합니다.
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# 2. 정답 확인 로직 함수
def check_guess():
    if st.session_state.game_over:
        return
    
    # st.number_input에 연결된 key 값을 통해 사용자의 입력을 가져옵니다.
    guess = st.session_state.user_guess
    st.session_state.attempts += 1
    
    if guess < st.session_state.secret_number:
        st.session_state.history.append(f"입력값 {guess} : 📈 UP!")
    elif guess > st.session_state.secret_number:
        st.session_state.history.append(f"입력값 {guess} : 📉 DOWN!")
    else:
        st.session_state.history.append(f"🎉 정답이야! {st.session_state.attempts}번 만에 맞췄네! (정답: {st.session_state.secret_number})")
        st.session_state.game_over = True

# 3. 게임 리셋 함수
def reset_game():
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.game_over = False

# --- UI 구성 ---

st.title("🎮 숫자 맞추기 게임")
st.write("🤖: 1부터 100 사이의 숫자 하나를 골랐어. 맞춰봐!")

# 사용자 입력 폼
st.number_input("숫자를 입력하세요 (1~100):", min_value=1, max_value=100, value=50, step=1, key="user_guess")

# 버튼 배치 (두 개의 버튼을 나란히 놓기 위해 컬럼 사용)
col1, col2 = st.columns(2)
with col1:
    # 확인 버튼을 누르면 check_guess 함수가 실행됩니다. 정답을 맞추면 버튼이 비활성화됩니다.
    st.button("확인", on_click=check_guess, disabled=st.session_state.game_over, use_container_width=True)
with col2:
    # 다시 시작 버튼
    st.button("다시 시작", on_click=reset_game, use_container_width=True)

# 구분선 추가
st.divider()

# 결과 및 기록 출력 (최신 기록이 위로 올라오도록 reversed 사용)
st.subheader("📝 기록")
for msg in reversed(st.session_state.history):
    st.write(msg)
