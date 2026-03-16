"""
Connect 4 - Clean minimal UI
"""

import streamlit as st
import time
from connect4_game import Connect4
from agent import MyAgent, RandomAgent


st.set_page_config(page_title="Connect 4", page_icon="●", layout="centered")

# Initialize
if 'game' not in st.session_state:
    st.session_state.game = Connect4()
    st.session_state.agent = MyAgent()
    st.session_state.random_agent = RandomAgent()
    st.session_state.game_over = False
    st.session_state.winner = None
    st.session_state.message = "Your turn"
    st.session_state.mode = "human_vs_agent"
    st.session_state.autoplay = False


def reset_game():
    st.session_state.game.reset()
    st.session_state.game_over = False
    st.session_state.winner = None
    st.session_state.autoplay = False
    if st.session_state.mode == "human_vs_agent":
        st.session_state.message = "Your turn"
    else:
        st.session_state.message = "Agent vs Random"


def make_human_move(col: int):
    if st.session_state.game_over or st.session_state.mode != "human_vs_agent":
        return
    
    game = st.session_state.game
    if game.current_player != 1:
        return
    
    if not game.is_valid_move(col):
        st.session_state.message = "Column full"
        return
    
    game.make_move(col)
    winner = game.check_winner()
    
    if winner is not None:
        st.session_state.game_over = True
        if winner == 1:
            st.session_state.message = "You win"
        elif winner == 2:
            st.session_state.message = "Agent wins"
        else:
            st.session_state.message = "Draw"
        return
    
    game.switch_player()
    st.session_state.message = "Agent thinking..."
    make_agent_move()


def make_agent_move():
    game = st.session_state.game
    agent = st.session_state.agent
    
    board_copy = game.get_board_copy()
    valid_moves = game.get_valid_moves()
    
    if not valid_moves:
        st.session_state.game_over = True
        st.session_state.message = "Draw"
        return
    
    agent_col = agent.get_move(board_copy, valid_moves)
    game.make_move(agent_col)
    winner = game.check_winner()
    
    if winner is not None:
        st.session_state.game_over = True
        if winner == 1:
            st.session_state.message = "You win"
        elif winner == 2:
            st.session_state.message = "Agent wins"
        else:
            st.session_state.message = "Draw"
        return
    
    game.switch_player()
    st.session_state.message = "Your turn"


def play_agent_vs_random_step():
    game = st.session_state.game
    
    if st.session_state.game_over:
        st.session_state.autoplay = False
        return
    
    if game.current_player == 1:
        current_agent = st.session_state.agent
    else:
        current_agent = st.session_state.random_agent
    
    board_copy = game.get_board_copy()
    valid_moves = game.get_valid_moves()
    
    if not valid_moves:
        st.session_state.game_over = True
        st.session_state.message = "Draw"
        st.session_state.autoplay = False
        return
    
    move_col = current_agent.get_move(board_copy, valid_moves)
    game.make_move(move_col)
    winner = game.check_winner()
    
    if winner is not None:
        st.session_state.game_over = True
        st.session_state.autoplay = False
        if winner == 1:
            st.session_state.message = "Agent wins"
        elif winner == 2:
            st.session_state.message = "Random wins"
        else:
            st.session_state.message = "Draw"
        return
    
    game.switch_player()
    next_player = "Agent" if game.current_player == 1 else "Random"
    st.session_state.message = f"{next_player}'s turn"


# CSS
st.markdown("""
<style>
    .stApp {
        background: #fafafa;
    }
    
    h1 {
        text-align: center;
        color: #2c3e50;
        font-weight: 300;
        margin-bottom: 2rem;
    }
    
    .status {
        text-align: center;
        color: #7f8c8d;
        font-size: 1.1rem;
        margin: 1.5rem 0;
    }
    
    .stButton > button {
        background: white;
        border: 1px solid #ddd;
        color: #333;
        font-weight: 400;
    }
    
    .stButton > button:hover {
        border-color: #333;
    }
    
    .stButton > button:disabled {
        background: #f5f5f5;
        color: #ccc;
    }
    
    .stRadio > div {
        background: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: 1px solid #ddd;
    }
    
    /* Center the cell content and reduce spacing */
    [data-testid="column"] {
        padding: 0 !important;
        min-width: 0 !important;
    }
    
    [data-testid="column"] > div {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        margin: 0;
    }
    
    /* Make cells centered with minimal spacing */
    [data-testid="column"] p {
        font-size: 2.8rem;
        margin: 0;
        padding: 0;
        text-align: center;
        line-height: 0.9;
    }
</style>
""", unsafe_allow_html=True)


# UI
st.title("Connect 4")

# Mode selector
mode = st.radio(
    "",
    ["Play vs Agent", "Watch: Agent vs Random"],
    horizontal=True,
    index=0 if st.session_state.mode == "human_vs_agent" else 1,
    label_visibility="collapsed"
)

new_mode = "human_vs_agent" if mode == "Play vs Agent" else "agent_vs_random"
if new_mode != st.session_state.mode:
    st.session_state.mode = new_mode
    reset_game()
    st.rerun()

# Status
st.markdown(f'<p class="status">{st.session_state.message}</p>', unsafe_allow_html=True)

# Column buttons
game = st.session_state.game
if st.session_state.mode == "human_vs_agent":
    cols = st.columns(7)
    for col_idx in range(7):
        with cols[col_idx]:
            if st.button(f"↓", key=f"btn_{col_idx}", 
                        disabled=st.session_state.game_over or not game.is_valid_move(col_idx),
                        use_container_width=True):
                make_human_move(col_idx)
                st.rerun()

# Board using streamlit components
for row in range(6):
    cols = st.columns(7, gap="small")
    for col_idx in range(7):
        with cols[col_idx]:
            cell_value = game.board[row][col_idx]
            if cell_value == 0:
                st.markdown('<p style="text-align: center; font-size: 2.8rem; margin: 0; padding: 0; color: #b0b0b0;">○</p>', unsafe_allow_html=True)
            elif cell_value == 1:
                st.markdown('<p style="text-align: center; font-size: 2.8rem; margin: 0; padding: 0; color: #dc2626;">●</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="text-align: center; font-size: 2.8rem; margin: 0; padding: 0; color: #fbbf24;">●</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Controls
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("New Game", use_container_width=True):
        reset_game()
        st.rerun()

if st.session_state.mode == "agent_vs_random":
    with col2:
        if not st.session_state.game_over:
            if st.session_state.autoplay:
                if st.button("Pause", use_container_width=True):
                    st.session_state.autoplay = False
                    st.rerun()
            else:
                if st.button("Auto Play", use_container_width=True):
                    st.session_state.autoplay = True
                    st.rerun()
    
    with col3:
        if not st.session_state.game_over and not st.session_state.autoplay:
            if st.button("Next Move", use_container_width=True):
                play_agent_vs_random_step()
                st.rerun()

# Auto-play
if st.session_state.mode == "agent_vs_random" and st.session_state.autoplay and not st.session_state.game_over:
    time.sleep(0.8)
    play_agent_vs_random_step()
    st.rerun()
