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
            '<div class="story-text">我對台北 101 的結構產生興趣，並非因為它是曾經的世界第一高樓，而是因為看了一段 Alex Honnold 攀登這座建築的影像。當我看到他懸掛在數百公尺的高空，手指扣住那些如竹節般的建築邊緣時，我意識到的不只是恐懼，而是這座建築在物理上的「不安定感」。在高空強勁的陣風中，這座細長的幾何體是如何維持穩定，而不讓頂端的攀爬者感受到致命的擺盪？</div>',
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

    with tab2:
        st.markdown('<div class="section-header">陶朱隱園：螺旋地標的結構代價</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：網路上的旋轉奇觀】**')
        st.markdown(
            '<div class="story-text">雖然沒親自進去過，內從網路新聞與空拍影片中，很難不被這棟旋轉建築吸引。它最著名的標籤除了單戶高昂的售價，就是那如同 DNA 螺旋的獨特外型。看著那些層層堆疊、長滿綠色植栽的陽台，我不禁在想，這究竟是一場為了綠色建築美名的昂貴實驗，還是建築結構學上的一次極限挑戰？它是怎麼支撐起數千棵樹木與厚重土層重量的？</div>',
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

        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">當數千棵樹木成年後，其根系對結構防水層的侵蝕，以及颱風天強風產生的風致振動對樹木穩定性的影響，長期維護成本是否會高到超乎想像？</div>',
            unsafe_allow_html=True)

        st.write("---")

# --- 類別二：表演藝術與文化空間 ---
elif category == "表演藝術與文化空間":
    tab1, tab2, tab3, tab4 = st.tabs(["東京巨蛋", "台中歌劇院", "台北表演藝術中心", "高雄流行音樂中心"])

    with tab1:
        st.markdown('<div class="section-header">日本東京巨蛋：漂浮的白色雲朵</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為運動迷，看經典賽時我的目光不只在投手丘上。巨蛋那片微透光的白色屋頂，大到不可思議卻看不見任何鋼樑支撐。那種極致的空曠，讓人在熱血之餘總有一絲不安：萬一這片輕飄飄的屋頂掉下來，底下的觀眾該怎麼辦？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座球場是如何利用看不見的大氣壓差，將厚重的膜材吹成一座堅不可摧的建築？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這屬於空氣支撐結構。室內氣壓維持在比室外高出 0.3% 的狀態，微小的壓差產生強大向上浮力，讓屋頂像充飽氣的皮球一樣繃緊對抗風雪。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">若遇到強震導致電力中斷、加壓風扇停擺，屋頂下降的緩衝時間有多長？是否有物理性的備援支撐防止塌陷？</div>',
            unsafe_allow_html=True)
        st.write("---")

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
            '<div class="logic-box">這並非裝飾，而是將牆與柱合一的壺中居結構。利用 3D 噴漿混擬土技術，讓牆面本身就具備承重路徑，重力順著曲面滑行到地下。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">雖然知道是靠牆撐住，但面對地震時的水平剪力，這些複雜的弧形牆面是如何傳導應力而不產生裂縫的？</div>',
            unsafe_allow_html=True)
        st.write("---")

    with tab3:
        st.markdown('<div class="section-header">台北表演藝術中心：橫向生長的幾何</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為嘉義人，這座建築在新聞上的討論度極高，但我更在意的是那種視覺上的突變感。巨大的銀色圓球像是從方體中突然長出來一樣。這種違反直覺的生長方式，讓我懷疑它在地震頻繁的台灣是否真的站得住腳？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：當巨型圓球從主建築橫向延伸，銜接處如何化解應力集中與扭轉破壞？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這屬於大跨度懸臂結構。球體重量透過內部的鋼構桁架拉回主體核心，並配置 S-SISO 抗震系統，讓球體與主體在受震時能有微小位移空間。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">長期使用下，這種非對稱懸臂設計在銜接處的鋼材疲勞問題，是否會比一般對稱建築更難監測與維護？</div>',
            unsafe_allow_html=True)
        st.write("---")

    with tab4:
        st.markdown('<div class="section-header">高雄流行音樂中心：愛河灣畔的幾何浪潮</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：滑到脆（Threads）上面的幾何奇觀】**')
        st.markdown(
            '<div class="story-text">最近在 Threads 上一直刷到高雄這座白色建築，空拍視角下那些六角形排列得密密麻麻，多到讓人有點「密集恐懼症」。網友們都在打卡說那是「海平面上的珊瑚礁」，但我越看越覺得不對勁，這種積木一樣東拼西湊、角度怪異的蜂巢牆面，真的不是純粹為了拍照好看嗎？在海邊這種鹽分高、颱風強的地方，這些細碎的窗格接縫如果漏水或生鏽，裡面那堆精密音響器材不就毀了？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這種由大量非對稱六角形組成之「蜂巢網格」，在力學上如何確保受力均勻，而不是只是一層空有其表的幾何外殼？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：空間網格與參數建模】**')
        st.markdown('<div class="logic-box">1. <b>空間網格 (Space Frame)</b>：它將受力分散到數以千計的鋼管節點上。即便某個局部受壓，網格會像蜘蛛網一樣將力量導向四周。<br>2. <b>數位參數化建模</b>：每個六角形的尺寸都經過精密計算，透過數位模擬確保外殼在承受強大風壓時，整體位移量能控制在安全範圍內。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">雖然網格很強，但每個窗格的矽利康（Silicone）封膠長度加起來驚人，在高雄烈日曝曬下，材料老化的速度是否會導致未來出現毀滅性的滲漏問題？</div>',
            unsafe_allow_html=True)
        st.write("---")

# --- 類別三：歷史與地景構造 ---
elif category == "歷史與地景構造":
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["嘉義美術館", "龍騰斷橋", "故宮南院", "西螺大橋", "澎湖跨海大橋"])

    with tab1:
        st.markdown('<div class="section-header">嘉義美術館：古蹟與 CLT 的時空交疊</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：身為嘉義人】**')
        st.markdown(
            '<div class="story-text">身為嘉義人，我看過這棟建築翻修前的斑駁與沉寂，也見證了它翻修後的重生。最讓我欣賞的是，它並沒有為了迎合現代審美而抹去歷史，反而大程度地保留了日治時期煙酒公賣局那種厚實、沉穩的磚造與洗石子結構。那種新舊並置的視覺衝擊，成功地讓年輕一代願意走進古蹟。</div>',
            unsafe_allow_html=True)

        st.markdown(
            '<div class="question-text">❓ 設計提問：如何在保留日治時期沉重磚造結構的同時，融入現代輕量化的補強設計，達成古今並置的空間美感？</div>',
            unsafe_allow_html=True)

        st.markdown('**【理性求證：新舊構造的融合與分離】**')
        st.markdown('<div class="logic-box">'
                    '這座建築的魅力來自於精準的補強與新舊脫離的策略：<br><br>'
                    '1. <b>CLT 集成材</b>：增建區採用輕質高強度的多層次鋼性集成材外牆，減輕老舊地基負擔。<br>'
                    '2. <b>三叉型集成材木柱</b>：在大廳內部支撐挑高屋頂，有效分擔荷重與水平力。<br>'
                    '3. <b>結構脫離設計</b>：古蹟棟與新大廳在力學上獨立，設有抗震縫避免受震時碰撞。</div>',
                    unsafe_allow_html=True)

        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">在台灣潮濕多雨環境下，木構造與玻璃帷幕交點的防水密封，對古蹟保存單位而言是否會是長期挑戰？</div>',
            unsafe_allow_html=True)
        st.write("---")

    with tab2:
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
            '<div class="logic-box">它是靠紅磚堆疊的半圓拱傳力。即便地基不平，工程師透過精確計算各橋墩深度與高度，讓重力依舊能循著拱形軌跡消散。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">單純靠紅磚與糯米黏合，在完全沒有鋼筋牽引的情況下，它對抗強烈水平晃動的力學極限究竟在哪？</div>',
            unsafe_allow_html=True)
        st.write("---")

    with tab3:
        st.markdown('<div class="section-header">故宮南院至美橋：不對稱的力學偏移</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：身為嘉義人】**')
        st.markdown(
            '<div class="story-text">身為嘉義人，我對這座橋非常熟悉。它的視覺重心完全偏向一側，在那種流線型的曲面中，雖然漂亮，但總讓人覺得它比一般的橋還要脆弱一些。</div>',
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
            '<div class="doubt-box">嘉義夏季常有強陣風，這種雙曲面的大受風面積，在設計上是如何透過模擬來計算其風致振動安全性？</div>',
            unsafe_allow_html=True)
        st.write("---")

    with tab4:
        st.markdown('<div class="section-header">西螺大橋：濁水溪上的紅色脊樑</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：那年環島的踏板記憶】**')
        st.markdown(
            '<div class="story-text">還記得那年高中環島，我騎著腳踏車來到雲林與彰化的交界。當這座鮮紅色的巨獸出現在濁水溪上方時，那種視覺壓迫感真的很強。我騎在狹窄的車道裡，旁邊是一格格重複出現的三角形鋼架，感覺自己像是穿梭在某種工業時代的時光隧道。我當時就在想，這座橋這麼長，在那個連電腦計算都沒有的年代，是怎麼確保這麼多鋼鐵拼出的桁架，能站得這麼穩？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：長度近兩公里的西螺大橋，如何利用三角形桁架的剛性，在寬闊且土質鬆軟的河床維持結構穩定？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：華倫式桁架與多孔跨接】**')
        st.markdown('<div class="logic-box">1. <b>華倫式桁架 (Warren Truss)</b>：利用幾何學中最穩定的三角形組成，將荷重均勻導向橋墩。<br>2. <b>多孔跨接設計</b>：全橋由 31 個獨立鋼橋孔組成，有效分散河水沖刷對單一橋墩的負擔。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">這座橋使用了大量鋼性鉚釘連接。經過一甲子的風雨侵蝕，這些關鍵連結點的疲勞損傷要如何進行非破壞性的精準檢測？</div>',
            unsafe_allow_html=True)
        st.write("---")

    with tab5:
        st.markdown('<div class="section-header">澎湖跨海大橋：橋頭路口的風速震撼</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：站在白色拱門下的敬畏】**')
        st.markdown(
            '<div class="story-text">去澎湖時，我站在跨海大橋起點的白色拱門前。雖然只是在路口觀賞，但看著那條看不見盡頭的橋樑橫跨海面，視覺衝擊極大。當時東北季風強勁，風聲大到刺耳。我心想，這座橋每天被強烈鹽水沖刷，還要承受世界級的風速，到底是用什麼材料做的？那些橋墩看起來並不粗壯，是如何在兇猛的海浪中站穩幾十年？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：在極高鹽分與強烈潮流的嚴苛環境下，如何透過結構設計避免鋼筋鏽蝕，並維持長期的抗浪穩定性？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：預力與流線型設計】**')
        st.markdown('<div class="logic-box">1. <b>預力混凝土</b>：事先對混凝土施加壓力以抵銷海浪產生的拉力，有效減少裂縫，阻絕鹽分滲入鋼筋。<br>2. <b>流線型防護橋墩</b>：橋墩外型設計成流線型，主動降低強大海流造成的側向推力，讓水流順利通過以減輕負擔。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">在長期乾濕交替的鹽害環境下，結構內部的鋼索若發生肉眼看不見的鏽蝕，目前的監測技術是否有辦法在斷裂發生前精準偵測？</div>',
            unsafe_allow_html=True)
        st.write("---")