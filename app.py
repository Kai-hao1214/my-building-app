import streamlit as st

# 1. 頁面基本設定
st.set_page_config(page_title="建築構造探索筆記", layout="wide")

# 2. 自定義樣式 (保持冷靜、乾淨的大學生筆記質感)
st.markdown("""
    <style>
    .main-title { color: #2c3e50; font-size: 2.2rem; font-weight: 700; margin-bottom: 2rem; border-bottom: 2px solid #eee; padding-bottom: 10px; }
    .section-header { color: #34495e; font-size: 1.5rem; margin-top: 1.5rem; font-weight: 600; }
    .story-text { background-color: #f8f9fa; padding: 25px; border-radius: 8px; border-left: 5px solid #4a5568; line-height: 1.7; color: #4a5568; }
    .question-text { color: #c05621; font-weight: 600; font-size: 1.15rem; margin: 1.5rem 0; border-left: 3px solid #c05621; padding-left: 15px; }
    .logic-box { background-color: #ebf4ff; padding: 20px; border-radius: 8px; margin-top: 10px; border: 1px solid #bee3f8; }
    .doubt-box { background-color: #fffaf0; padding: 15px; border-radius: 8px; border: 1px solid #feebc8; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">建築構造探索筆記：從美學直覺到理性求證</div>', unsafe_allow_html=True)

# 3. 側邊欄分類選擇
category = st.sidebar.selectbox(
    "選擇建築類別",
    ["地標與超高層建築", "表演藝術與文化空間", "歷史與地景構造"]
)

# --- 類別一：地標與超高層建築 ---
if category == "地標與超高層建築":
    tab1, tab2 = st.tabs(["台北 101", "陶朱隱園"])

    with tab1:
        st.markdown('<div class="section-header">台北 101：雲端的質量平衡遊戲</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：從 Alex 的挑戰說起】**')
        st.markdown(
            '<div class="story-text">我對台北 101 的結構產生興趣，並非因為它是曾經的世界第一高樓，而是因為看了一段 Alex Honnold 攀登這座建築的影像。當我看到他懸掛在數百公尺的高空，手指扣住那些如竹節般的建築邊緣時，我意識到的不只是恐懼，而是這座建築在物理上的不安定感。在高空強勁的陣風中，這座細長的幾何體是如何維持穩定？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座細長的幾何體，如何透過物理性的質量抵銷與幾何形狀設計，化解高空風力的強烈擾動？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：雙重抗風機制】**')
        st.markdown('<div class="logic-box">101