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
            '<div class="story-text">我對台北 101 的結構產生興趣，並非因為它是曾經的世界第一高樓，而是因為看了一段 Alex Honnold 攀登這座建築的影像。當我看到他懸掛在數百公尺的高空，手指扣住那些如竹節般的建築邊緣時，我意識到的不只是恐懼，而是這座建築在物理上的不安定感。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座細長的幾何體，如何透過物理性的質量抵銷與幾何形狀設計，化解高空風力的強烈擾動？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：雙重抗風機制】**')
        st.markdown('<div class="logic-box">1. <b>動態平衡 TMD</b>：懸掛於高層的 660 公噸金屬巨球，利用物理慣性抵銷大樓晃動。<br>'
                    '2. <b>幾何流體力學 Saw-tooth Design</b>：類似竹節的收縮設計與轉角鋸齒，能有效打碎高空氣流，防止形成規律的漩渦，降低風力推力。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">這種複雜的轉角設計，在長期承受高空風壓下，對玻璃帷幕與鋼構接頭的密合度是否有特殊的耐久性要求？</div>',
            unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[台北101官網](https://www.taipei-101.com.tw/tw/observatory/damper)")

    with tab2:
        st.markdown('<div class="section-header">陶朱隱園：螺旋地標的結構代價</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：網絡上的旋轉奇觀】**')
        st.markdown(
            '<div class="story-text">雖然沒親自進去過，但從網絡新聞與空拍影片中，很難不被這棟旋轉建築吸引。它最著名的標籤除了單戶高昂的售價，就是那如同 DNA 螺旋的獨特外型。看著那些層層堆疊、長滿綠色植栽的陽台，我不禁在想，這究竟是一場為了綠色建築美名的昂貴實驗，還是建築結構學上的一次極限挑戰？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：旋轉外觀創造了垂直綠化露台，但在物理層面上，這種不對稱的重力負荷如何不導致建築往單側傾斜？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：滑雪人結構系統】**')
        st.markdown('<div class="logic-box">1. <b>核心筒與巨型桁架</b>：建築中心是強大的 RC 核心筒，頂部 21 樓設有巨型鋼桁架，如同滑雪者的身體與雙肩。<br>'
                    '2. <b>懸吊系統</b>：樓層重量透過兩側巨型鋼柱傳導至頂部桁架，再由核心筒吸收，如同滑雪桿支撐重心。<br>'
                    '3. <b>隔震技術</b>：基座安裝 48 組全球最大型等級隔震墊，確保強震時建築能像在冰上滑動般抵銷能量。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">當樹木成年後，其根系對結構防水層的侵蝕，以及颱風天強風產生的風致振動對樹木穩定性的影響，維護成本是否超乎想像？</div>',
            unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[陶朱隱園官網](https://www.tao-zhu.com.tw/structure.html)")

# --- 類別二：表演藝術與文化空間 ---
elif category == "表演藝術與文化空間":
    tab1, tab2, tab3 = st.tabs(["東京巨蛋", "台中歌劇院", "台北表演藝術中心"])

    with tab1:
        st.markdown('<div class="section-header">日本東京巨蛋：漂浮的白色雲朵</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為運動迷，巨蛋那片微透光的白色屋頂大到不可思議卻看不見任何鋼樑支撐。那種極致的空曠讓人在熱血之餘總有一絲不安：萬一這片輕飄飄的屋頂掉下來怎麼辦？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座球場是如何利用看不見的大氣壓差，將厚重的膜材吹成一座建築？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：氣壓平衡與連續膜材】**')
        st.markdown('<div class="logic-box">1. <b>內部加壓系統</b>：室內氣壓維持在比室外高出 0.3% 的狀態，微小壓差產生強大向上浮力支撐膜材。<br>'
                    '2. <b>高強度樹脂膜材</b>：由雙層玻璃纖維膜構成，具備極佳抗張強度，並透過鋼索網補強防止崩塌。<br>'
                    '3. <b>氣閘門控管</b>：出入口皆設計為旋轉氣閘門，確保觀眾進出時室內壓力不致流失。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">若遇到強震導致電力中斷、加壓風扇停擺，屋頂下降的緩衝時間有多長？</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[Tokyo Dome City 官網](https://www.tokyo-dome.co.jp/zh-CHT/tourists/dome/about/)")

    with tab2:
        st.markdown('<div class="section-header">台中國家歌劇院：流動的垂直曲面</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">這些弧線是垂直延伸的，跟我認知中平整的牆面完全不同。我當時在想，這是不是在傳統柱子外面貼了一層厚水泥皮？不然沒柱子怎麼撐得住？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：垂直延伸的沙漏狀曲面，究竟是裝飾性的外衣，還是取代樑柱結構的骨架？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：曲面剪力牆與 3D 噴漿技術】**')
        st.markdown('<div class="logic-box">1. <b>三維曲面承重牆</b>：由 58 面曲牆組成，重力順著曲面滑行消散至地下，而非透過垂直柱子。<br>'
                    '2. <b>鋼骨編網與噴漿工法</b>：先以細密鋼筋編織 3D 骨架，再利用高強度噴漿混凝土一體成型澆灌。<br>'
                    '3. <b>結構抗震邏輯</b>：曲面結構在受震時具備多向傳力特性，有效分散剪力。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">面對地震時的水平剪力，這些複雜的弧形牆面是如何傳導應力而不產生裂縫的？</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[台中國家歌劇院官網](https://www.npac-ntt.org/about/architecture)")

    with tab3:
        st.markdown('<div class="section-header">台北表演藝術中心：橫向生長的幾何</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">巨大的銀色圓球像是從方體中突然長出來一樣。這種違反直覺的生長方式，讓我懷疑它在地震頻繁的台灣是否真的站得住腳。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：當巨型圓球從主建築橫向延伸，銜接處如何化解應力集中與扭轉破壞？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：大跨度懸臂與多維隔震系統】**')
        st.markdown('<div class="logic-box">1. <b>巨型鋼構桁架 Mega Truss</b>：透過主體建築內部的強大鋼桁架，像手臂將球體劇場拉回核心筒。<br>'
                    '2. <b>S-SISO 隔震技術</b>：在球體與主體銜接處配置滑動式隔震系統，容許微小位移空間避免撕裂。<br>'
                    '3. <b>波浪玻璃結構剛性</b>：外牆波浪型玻璃的幾何褶皺具備極強抗風壓剛性，減少支撐構件。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">長期使用下，這種非對稱懸臂設計在銜接處的鋼材疲勞問題是否更難監測？</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[台北表演藝術中心](https://www.tpac-taipei.org/about/architecture)")

# --- 類別三：歷史與地景構造 ---
elif category == "歷史與地景構造":
    tab1, tab2, tab3 = st.tabs(["嘉義美術館", "龍騰斷橋", "故宮南院"])

    with tab1:
        st.markdown('<div class="section-header">嘉義美術館：古蹟與 CLT 的時空交疊</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為嘉義人，我看過這棟建築翻修前的斑駁，也見證了它翻修後的重生。它大程度地保留了日治時期煙酒公賣局那種厚實的磚造與洗石子結構，讓年輕一代願意走進古蹟。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：如何在保留日治時期沉重磚造結構的同時，融入現代輕量化的補強設計？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：新舊構造的融合與分離】**')
        st.markdown('<div class="logic-box">1. <b>CLT 集成材</b>：增建區採用輕質高強度的集成材外牆，減輕老舊地基負擔。<br>'
                    '2. <b>三叉型集成材木柱</b>：在大廳內部支撐挑高屋頂，有效分擔垂直荷重，創造大面積無柱視野。<br>'
                    '3. <b>結構脫離設計</b>：古蹟與新大廳在力學上完全獨立，設有抗震縫避免受震時碰撞。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">在台灣潮濕多雨環境下，木構造與玻璃帷幕交接處的防水密封是否會是挑戰？</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("參考資料：[嘉義市立美術館官網](https://chiayiartmuseum.chiayi.gov.tw/Introduction/Architecture)")

    with tab2:
        st.markdown('<div class="section-header">龍騰斷橋：崎嶇地貌上的殘弧</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">小時候去三義旅遊發現這裡地形極度不平整。要在這種地方用紅磚疊起一座能跑火車的橋，在結構上到底是怎麼平衡的？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：在崎嶇不平的地貌中，紅磚拱橋如何撐起一條水平的鐵路？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證：半圓拱傳力邏輯】**')
        st.markdown(
            '<div class="logic-box">它是靠紅磚堆疊的半圓拱傳力。即便地基不平，工程師透過精確計算各橋墩深度與高度，讓重力依舊能循著拱形軌跡消散。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">單純靠紅磚與糯米黏合，在完全沒有鋼筋牽引下，它對抗水平晃動的極限在哪？</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write(
            "歷史紀錄：[國家文化資產網](https://nchdb.boch.gov.tw/assets/overview/historicalBuilding/20031125000004)")

    with tab3:
        st.markdown('<div class="section-header">故宮南院至美橋：不對稱的力學偏移</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為嘉義人，這座橋的視覺重心完全偏向一側。在流線型曲面中雖然漂亮，但總讓人覺得它比一般的橋還要脆弱一些。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座橋看似輕盈地橫跨水面，如何克服單側支撐帶來的巨大扭力？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：單塔斜張橋與螺旋鋼樑】**')
        st.markdown(
            '<div class="logic-box">這是一座單塔斜張橋，利用內部的螺旋鋼樑支撐系統，將不對稱載重與側向風力轉化為旋轉應力，傳導至混凝土錨座。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">嘉義夏季常有強陣風，這種大受風面積在設計上如何透過模擬計算其安全性？</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("官方導覽：[故宮南院](https://south.npm.gov.tw/Explore/Architecture)")