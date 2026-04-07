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
            '<div class="story-text">我對台北 101 的結構產生興趣，並非因為它是曾經的世界第一高樓，而是因為看了一段 Alex Honnold 攀登這座建築的影像。當我看到他懸掛在數百公尺的高空，手指扣住那些如竹節般的建築邊緣時，我意識到的不只是恐懼，而是這座建築時在物理上的「不安定感」。在高空強勁的陣風中，這座細長的幾何體是如何維持穩定，而不讓頂端的攀爬者感受到致命的擺盪？</div>',
            unsafe_allow_html=True)

        st.markdown(
            '<div class="question-text">❓ 設計提問：這座細長的幾何體，如何透過物理性的質量抵銷與幾何形狀設計，化解高空風力的強烈擾動？</div>',
            unsafe_allow_html=True)

        st.markdown('**【理性求證：雙重抗風機制】**')
        st.markdown('<div class="logic-box">101 採用了「內外兼修」的抗震策略：<br><br>'
                    '1. <b>動態平衡 TMD</b>：懸掛於高層的金屬巨球，利用物理慣性抵銷大樓晃動。<br>'
                    '2. <b>幾何流體力學 Saw-tooth Design</b>：竹節收縮設計與轉角鋸齒，能有效打碎高空氣流，降低風力推力。</div>',
                    unsafe_allow_html=True)

        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">雖然幾何形狀能干擾氣流，但這種複雜的轉角設計，在長期承受高空風壓下，對玻璃帷幕與鋼構接頭的密合度是否有特殊的材料耐久性要求？</div>',
            unsafe_allow_html=True)

        st.write("---")
        # 修正：改用官方科普主頁路徑
        st.write("官方連結：[台北101 - 阻尼器科普專頁](https://www.taipei-101.com.tw/tw/observatory/damper)")

    with tab2:
        st.markdown('<div class="section-header">陶朱隱園：螺旋地標的結構代價</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：網路上的旋轉奇觀】**')
        st.markdown(
            '<div class="story-text">雖然沒親自進去過，但從網路新聞與空拍影片中，很難不被這棟旋轉建築吸引。它最著名的標籤除了單戶高昂的售價，就是那如同 DNA 螺旋的獨特外型。看著那些層層堆疊、長滿綠色植栽的陽台，我不禁在想，這究竟是一場為了綠色建築美名的昂貴實驗，還是建築結構學上的一次極限挑戰？它是怎麼支撐起數千棵樹木與厚重土層重量的？</div>',
            unsafe_allow_html=True)

        st.markdown(
            '<div class="question-text">❓ 設計提問：旋轉外觀創造了垂直綠化露台，但在物理層面上，這種不對稱的重力負荷如何不導致建築往單側傾斜？</div>',
            unsafe_allow_html=True)

        st.markdown('**【理性求證：滑雪人結構系統】**')
        st.markdown('<div class="logic-box">陶朱隱園採用了罕見的 <b>Ski-lift System</b> 達成力學平衡：<br><br>'
                    '1. <b>核心筒與巨型桁架</b>：建築中心是強大的 RC 核心筒，頂部 21 樓設有巨型鋼桁架，如同滑雪者的身體與雙肩。<br>'
                    '2. <b>懸吊系統</b>：樓層重量透過兩側巨型鋼柱傳導至頂部桁架，再由核心筒吸收，如同滑雪桿支撐重心。<br>'
                    '3. <b>隔震技術</b>：基座安裝 48 組全球最大型等級隔震墊，確保強震時建築能像在冰上滑動般抵銷能量。</div>',
                    unsafe_allow_html=True)

        st.write("---")
        # 修正：改用首頁，並提示手動導航至「建築DNA」
        st.write("官方連結：[陶朱隱園官方入口](https://www.tao-zhu.com.tw/)")

# --- 類別二：表演藝術與文化空間 ---
elif category == "表演藝術與文化空間":
    tab1, tab2, tab3 = st.tabs(["東京巨蛋", "台中歌劇院", "台北表演藝術中心"])

    with tab1:
        st.markdown('<div class="section-header">日本東京巨蛋：漂浮的白色雲朵</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown('<div class="logic-box">這屬於空氣支撐結構。室內氣壓維持在比室外高出 0.3% 的狀態，微小的壓差產生強大向上浮力。</div>', unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[Tokyo Dome - 官方設施介紹](https://www.tokyo-dome.co.jp/dome/about/)")

    with tab2:
        st.markdown('<div class="section-header">台中國家歌劇院：流動的垂直曲面</div>', unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">這並非裝飾，而是將牆與柱合一的壺中居結構。利用 3D 噴漿混擬土技術，讓牆面本身就具備承重路徑。</div>', unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[國家歌劇院 - 建築介紹](https://www.npac-ntt.org/about/architecture)")

    with tab3:
        st.markdown('<div class="section-header">台北表演藝術中心：橫向生長的幾何</div>', unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">球體重量透過內部的鋼構桁架拉回主體核心，並配置 S-SISO 抗震系統。</div>', unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[台北表演藝術中心 - 空間特色](https://www.tpac-taipei.org/about/architecture)")

# --- 類別三：歷史與地景構造 ---
elif category == "歷史與地景構造":
    tab1, tab2, tab3 = st.tabs(["嘉義美術館", "龍騰斷橋", "故宮南院"])

    with tab1:
        st.markdown('<div class="section-header">嘉義美術館：古蹟與 CLT 的時空交疊</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：身為嘉義人】**')
        st.markdown('<div class="story-text">我見證了它翻修後的重生。它大程度地保留了日治時期煙酒公賣局的磚造結構。</div>', unsafe_allow_html=True)
        st.markdown('**【理性求證：新舊構造的融合與分離】**')
        st.markdown('<div class="logic-box">1. <b>CLT 集成材</b>：輕質高強度，減輕老舊地基負擔。<br>2. <b>結構脫離</b>：古蹟與新館設有抗震縫獨立運作。</div>', unsafe_allow_html=True)
        st.write("---")
        # 修正：嘉義美術館網址路徑非常敏感，改用穩定導覽頁面
        st.write("官方連結：[嘉義市立美術館 - 空間介紹](https://chiayiartmuseum.chiayi.gov.tw/Introduction/Architecture)")

    with tab2:
        st.markdown('<div class="section-header">龍騰斷橋：崎嶇地貌上的殘弧</div>', unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">靠紅磚堆疊的半圓拱傳力。即使地基不平，精確計算橋墩高度仍能維持水平。</div>', unsafe_allow_html=True)
        st.write("---")
        # 修正：改用國家文化資產網穩定連結
        st.write("歷史連結：[國家文化資產網 - 魚藤坪斷橋](https://nchdb.boch.gov.tw/assets/overview/historicalBuilding/20031125000004)")

    with tab3:
        st.markdown('<div class="section-header">故宮南院至美橋：不對稱的力學偏移</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：身為嘉義人】**')
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">單塔斜張橋，利用螺旋鋼樑與鋼纜系統將不對稱重力拉回主塔。</div>', unsafe_allow_html=True)
        st.write("---")
        # 修正：故宮南院改用園區介紹穩定頁面
        st.write("官方連結：[故宮南院 - 園區景觀導覽](https://south.npm.gov.tw/Explore/Architecture)")