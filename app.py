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
    tab1 = st.tabs(["台北 101"])

    with tab1[0]:
        st.markdown('<div class="section-header">台北 101：雲端的質量平衡遊戲</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：從 Alex 的挑戰說起】**')
        st.markdown(
            '<div class="story-text">我對台北 101 的結構產生興趣，並非因為它是曾經的世界第一高樓，而是因為看了一段 Alex Honnold 攀登這座建築的影像。當我看到他懸掛在數百公尺的高空，手指扣住那些如竹節般的建築邊緣時，我意識到的不只是恐懼，而是這座建築在物理上的「不安定感」。在高空強勁的陣風中，這座細長的幾何體是如何維持穩定，而不讓頂端的攀爬者感受到致命的擺盪？</div>',
            unsafe_allow_html=True)

        st.markdown(
            '<div class="question-text">❓ 設計提問：這座細長的幾幾何體，如何透過物理性的質量抵銷與幾何形狀設計，化解高空風力的強烈擾動？</div>',
            unsafe_allow_html=True)

        st.markdown('**【理性求證：雙重抗風機制】**')
        st.markdown('<div class="logic-box">透過資料查閱，101 採用了「內外兼修」的抗震策略：<br><br>'
                    '1. <b>動態平衡 (TMD)</b>：懸掛於高層的 660 公噸金屬巨球，利用物理慣性抵銷大樓晃動。<br>'
                    '2. <b>幾何流體力學 (Saw-tooth Design)</b>：類似竹節的收縮設計與轉角鋸齒，能有效「打碎」高空氣流，防止形成規律的漩渦（渦流脫離 Vortex Shedding），從根本上降低了風力對大樓的推力。</div>',
                    unsafe_allow_html=True)

        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">雖然幾何形狀能干擾氣流，但這種複雜的轉角設計，在長期承受高空風壓與日照熱漲冷縮的循環下，對玻璃帷幕與鋼構接頭的密合度是否有特殊的材料耐久性要求？</div>',
            unsafe_allow_html=True)

        st.write("---")
        st.write("官方連結：[台北101官網 - 阻尼器介紹](https://www.taipei-101.com.tw/tw/observatory/damper)")

# --- 類別二：表演藝術與文化空間 ---
elif category == "表演藝術與文化空間":
    tab1, tab2, tab3 = st.tabs(["東京巨蛋", "台中歌劇院", "台北表演藝術中心"])

    with tab1:
        st.markdown('<div class="section-header">日本東京巨蛋：漂浮的白色雲朵</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為運動迷，看經典賽時我的目光不只在投手丘上。巨蛋那片微透光的白色屋頂，大到不可思議卻看不見任何鋼樑支撐。那種極致的空曠，讓人在熱血之餘總有一絲不安：萬一這片輕飄飄的屋頂掉下來，底下的觀眾該怎麼辦？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座球場是如何利用看不見的大氣壓差，將厚重的膜材「吹」成一座堅不可摧的建築？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這屬於「空氣支撐結構」。室內氣壓始終維持在比室外高出 0.3% 的狀態，這微小的壓差產生了強大的向上浮力，讓屋頂像充飽氣的皮球一樣繃緊，足以對抗風雪。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">若遇到強震導致電力中斷、加壓風扇停擺，屋頂下降的緩衝時間有多長？是否有物理性的備援支撐防止塌陷？</div>',
            unsafe_allow_html=True)
        st.write("---")
        st.write(
            "官方連結：[Tokyo Dome City 官網 - 關於巨蛋的秘密](https://www.tokyo-dome.co.jp/zh-CHT/tourists/dome/about/)")

    with tab2:
        st.markdown('<div class="section-header">台中國家歌劇院：流動的垂直曲面</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">國小跟著直笛隊來這裡表演時，我先被外牆那些像沙漏般收束又展開的曲面震懾住。這些弧線是垂直延伸的，跟我認知中平整的牆面完全不同。我當時在想，這是不是在傳統柱子外面貼了一層厚水泥皮？不然沒柱子怎麼撐得住？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：垂直延伸的沙漏狀曲面，究竟是裝飾性的外衣，還是取代樑柱結構的骨架？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這並非裝飾，而是將牆與柱合一的「壺中居」結構。利用 3D 噴漿混擬土技術，讓牆面本身就具備承重路徑，重力順著曲面滑行到地下。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">雖然知道是靠牆撐住，但面對地震時的水平剪力，這些複雜的弧形牆面是如何傳導應力而不產生裂縫的？</div>',
            unsafe_allow_html=True)
        st.write("---")
        st.write("官方資料：[台中國家歌劇院官網 - 建築美學](https://www.npac-ntt.org/about/architecture)")

    with tab3:
        st.markdown('<div class="section-header">台北表演藝術中心：橫向生長的幾何</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為嘉義人，這座建築在新聞上的討論度極高，但我更在意的是那種視覺上的「突變感」。巨大的銀色圓球像是從方體中突然長出來一樣。這種違反直覺的生長方式，讓我懷疑它在地震頻繁的台灣是否真的站得住腳。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：當巨型圓球從主建築橫向延伸，銜接處如何化解應力集中與扭轉破壞？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這屬於大跨度懸臂結構。球體重量透過內部的鋼構桁架「拉」回主體核心，並配置 S-SISO 抗震系統，讓球體與主體在受震時能有微小位移空間，緩衝撕裂力。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">長期使用下，這種非對稱懸臂設計在銜接處的鋼材疲勞問題，是否會比一般對稱建築更難監測與維護？</div>',
            unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[台北表演藝術中心 - 空間特色](https://www.tpac-taipei.org/about/architecture)")

# --- 類別三：歷史與地景構造 ---
elif category == "歷史與地景構造":
    tab1, tab2 = st.tabs(["龍騰斷橋", "故宮南院"])

    with tab1:
        st.markdown('<div class="section-header">龍騰斷橋：崎嶇地貌上的殘弧</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">小時候去三義旅遊，我發現這裡的環境非常荒謬。地面極度不平整，河谷深邃且兩岸不在同一個水平線上。這種地形一點都不適合蓋橋，要在這種地方用紅磚疊起一座能跑火車的橋，在結構上到底是怎麼平衡的？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：在崎嶇不平的地貌中，紅磚拱橋如何透過高度不等的橋墩，撐起一條水平的鐵路？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">它是靠紅磚堆疊的「半圓拱」傳力。即便地基不平，工程師透過精確計算各橋墩的深度與高度，讓重力依舊能循著拱形軌跡消散。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">單純靠紅磚與糯米黏合，在完全沒有鋼筋牽引的情況下，它對抗強烈水平晃動的力學極限究竟在哪？</div>',
            unsafe_allow_html=True)
        st.write("---")
        st.write(
            "歷史紀錄：[國家文化資產網 - 魚藤坪斷橋](https://nchdb.boch.gov.tw/assets/overview/historicalBuilding/20031125000004)")

    with tab2:
        st.markdown('<div class="section-header">故宮南院至美橋：不對稱的力學偏移</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為嘉義人，我對這座橋非常熟悉。它的視覺重心完全偏向一側，在那種流線型的曲面中，雖然漂亮，但總讓人覺得它比一般的橋還要「脆弱」一些。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座橋看似輕盈地橫跨水面，在物理層面上如何克服單側支撐帶來的巨大扭力？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這是一座單塔斜張橋，利用內部的螺旋鋼樑支撐系統，將不對稱的載重與側向風力轉化為旋轉應力，傳導至兩側的混凝土錨座。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">嘉義夏季常有強陣風，這種雙曲面的大受風面積，在設計上是如何透過模擬來計算其風致振動的安全性？</div>',
            unsafe_allow_html=True)
        st.write("---")
        st.write("官方導覽：[故宮南院 - 建築美學](https://south.npm.gov.tw/Explore/Architecture)")