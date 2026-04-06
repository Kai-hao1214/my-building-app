import streamlit as st

# 1. 頁面基本設定
st.set_page_config(page_title="建築構造探索筆記", layout="wide")

# 2. 自定義樣式
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
        st.markdown('<div class="section-header">台北 101：雲端的質量平衡遊戲</div>')
        st.markdown('**【我的故事：從 Alex 的挑戰說起】**')
        st.markdown(
            '<div class="story-text">我對台北 101 的結構產生興趣，是因為看了一段 Alex Honnold 攀登影像。看他懸掛在數百公尺高空扣住竹節般的邊緣時，我意識到這座建築在物理上的不安定感。在高空強風中，這座細長的幾何體是如何維持穩定？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：如何透過物理性的質量抵銷與幾何形狀設計，化解高空風力的強烈擾動？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：雙重抗風機制】**')
        st.markdown('<div class="logic-box">1. <b>調諧質量阻尼器 TMD</b>：懸掛於 87 至 92 樓的 660 公噸鋼球，利用慣性產生反向作用力，抵銷大樓擺盪。<br>'
                    '2. <b>鋸齒狀轉角 Saw-tooth Design</b>：竹節造型與鋸齒邊角可擾亂並打碎流經大樓表面的強風，防止形成規律的「漩渦脫落」現象。<br>'
                    '3. <b>巨型鋼柱結構</b>：由 8 支巨型柱（Mega Columns）灌注高強度混凝土，構成強大的剛性核心。</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[台北101官網](https://www.taipei-101.com.tw/tw/observatory/damper)")

    with tab2:
        st.markdown('<div class="section-header">陶朱隱園：螺旋地標的結構代價</div>')
        st.markdown('**【我的故事：網絡上的旋轉奇觀】**')
        st.markdown(
            '<div class="story-text">雖然沒去過，但從網路影片中很難不被這棟旋轉建築吸引。它著名的標籤除了單戶高昂售價，就是如同 DNA 的獨特外型。看著那些長滿植栽的陽台，我不禁想，這究竟是綠建築實驗，還是結構學的極限挑戰？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：旋轉外觀創造了垂直綠化，但在物理層面上，不對稱的重力負荷如何不導致建築傾斜？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：滑雪人結構系統】**')
        st.markdown('<div class="logic-box">1. <b>核心筒與巨型桁架</b>：中心為強大的 RC 核心筒，頂部 21 樓設有巨型鋼桁架，功能如同滑雪者的身體與雙肩。<br>'
                    '2. <b>Ski-lift 懸吊系統</b>：各樓層重量透過兩側巨型鋼柱傳導至頂部桁架，再由核心筒吸收，確保重心穩定。<br>'
                    '3. <b>高性能隔震墊</b>：基座安裝 48 組全球最大型等級隔震墊，確保強震時建築能位移避震。</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[陶朱隱園官網](https://www.tao-zhu.com.tw/structure.html)")

# --- 類別二：表演藝術與文化空間 ---
elif category == "表演藝術與文化空間":
    tab1, tab2, tab3 = st.tabs(["東京巨蛋", "台中歌劇院", "台北表演藝術中心"])

    with tab1:
        st.markdown('<div class="section-header">日本東京巨蛋：漂浮的白色雲朵</div>')
        st.markdown('**【理性求證：氣壓平衡與連續膜材】**')
        st.markdown('<div class="logic-box">1. <b>內部加壓系統</b>：室內氣壓始終維持在比室外高出 0.3% 的微小壓差，產生足以支撐數千公噸膜材的浮力。<br>'
                    '2. <b>高強度樹脂膜材</b>：由雙層玻璃纖維膜構成，具備極佳抗張強度，並透過鋼索網（Cable Net）進行補強。<br>'
                    '3. <b>旋轉氣閘門</b>：所有出入口皆設計為氣閘系統，防止人員進出時室內壓力迅速流失導致屋頂塌陷。</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[Tokyo Dome City](https://www.tokyo-dome.co.jp/zh-CHT/tourists/dome/about/)")

    with tab2:
        st.markdown('<div class="section-header">台中國家歌劇院：流動的垂直曲面</div>')
        st.markdown('**【理性求證：曲面剪力牆與 3D 噴漿技術】**')
        st.markdown('<div class="logic-box">1. <b>美聲涵洞 Catenoid</b>：由 58 面無樑柱曲牆組成，重力順著連續曲面滑行至地基，而非傳統垂直點對點傳導。<br>'
                    '2. <b>鋼骨編網工法</b>：以細密鋼筋編織 3D 骨架，再利用高強度噴漿混凝土（Shotcrete）澆灌而成。<br>'
                    '3. <b>聲學結構合一</b>：曲面設計同時兼顧結構承重與內部聲音反射，達成無死角的聲學效果。</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[台中國家歌劇院](https://www.npac-ntt.org/about/architecture)")

    with tab3:
        st.markdown('<div class="section-header">台北表演藝術中心：橫向生長的幾何</div>')
        st.markdown('**【理性求證：大跨度懸臂與多維隔震系統】**')
        st.markdown('<div class="logic-box">1. <b>巨型鋼構桁架 Mega Truss</b>：利用主體內部鋼桁架將圓球劇場「拉回」核心結構，化解橫向懸臂重力。<br>'
                    '2. <b>S-SISO 隔震技術</b>：在球體與方體銜接處配置滑動式隔震墊，容許地震時兩者有不同頻率的微位移。<br>'
                    '3. <b>幾何抗風玻璃</b>：球體外圍使用波浪型玻璃，藉由幾何摺皺增加表面剛性，減少內部支撐架。</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("官方連結：[台北表演藝術中心](https://www.tpac-taipei.org/about/architecture)")

# --- 類別三：歷史與地景構造 ---
elif category == "歷史與地景構造":
    tab1, tab2, tab3 = st.tabs(["嘉義美術館", "龍騰斷橋", "故宮南院"])

    with tab1:
        st.markdown('<div class="section-header">嘉義美術館：古蹟與 CLT 的時空交疊</div>')
        st.markdown('**【理性求證：新舊構造的融合與分離】**')
        st.markdown('<div class="logic-box">1. <b>CLT 集成材外牆</b>：增建區採用輕質高強度的多層次鋼性集成材，降低對歷史地基的荷重。<br>'
                    '2. <b>三叉型支撐木柱</b>：在大廳內部以木質結構支撐挑高屋頂，有效分散垂直荷重並創造無柱視域。<br>'
                    '3. <b>結構獨立策略</b>：古蹟棟與新大廳力學完全分開，設有抗震縫隙防止地震時相互碰撞。</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("參考資料：[嘉義市立美術館](https://chiayiartmuseum.chiayi.gov.tw/Introduction/Architecture)")

    with tab2:
        st.markdown('<div class="section-header">龍騰斷橋：崎嶇地貌上的殘弧</div>')
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">小時候去三義發現這裡地形極度不平整。要在這種崎嶇紅土帶疊起一座能跑火車的橋，紅磚如何達成力學上的平衡？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：在崎嶇地貌中，單純靠紅磚堆疊的拱橋如何撐起巨大的動態鐵路載重？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：重力擠壓與拱形分配】**')
        st.markdown('<div class="logic-box">1. <b>半圓拱傳力機制</b>：利用「拱型」將垂直載重轉換為斜向的擠壓力，讓磚塊與磚塊間產生強大摩擦力傳導重力。<br>'
                    '2. <b>不同高度橋墩設計</b>：針對深淺不一的河谷，工程師精確調整各橋墩深度，確保頂部保持絕對水平供鐵軌鋪設。<br>'
                    '3. <b>糯米膠泥黏結</b>：早期採用糯米與石灰混合的膠泥，具備微小的韌性彈性，輔助紅磚應付微幅熱漲冷縮。</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write(
            "歷史紀錄：[國家文化資產網](https://nchdb.boch.gov.tw/assets/overview/historicalBuilding/20031125000004)")

    with tab3:
        st.markdown('<div class="section-header">故宮南院至美橋：不對稱的力學偏移</div>')
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為嘉義人，我看這座橋重心完全偏向一側。這種非對稱的流線型設計，在力學上是如何穩定站立在水面上的？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：不對稱的雙曲面橋梁，如何克服單側支撐產生的強大扭轉應力？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：箱型鋼樑與單塔斜張系統】**')
        st.markdown('<div class="logic-box">1. <b>螺旋箱型鋼樑</b>：橋體內部採用抗扭剛性極強的螺旋狀箱型鋼結構，吸收因非對稱曲面產生的扭矩。<br>'
                    '2. <b>單塔斜張斜拉</b>：利用單側高塔懸掛高張力鋼纜，將橋面重量精確拉回主塔核心，抵銷單側沉陷壓力。<br>'
                    '3. <b>深層基礎錨座</b>：兩端設有巨大的混凝土錨室，將橋梁傳遞過來的水平與旋轉應力牢牢鎖進地層。</div>',
                    unsafe_allow_html=True)
        st.write("---")
        st.write("官方導覽：[故宮南院](https://south.npm.gov.tw/Explore/Architecture)")