import streamlit as st

# 1. 頁面基本設定
st.set_page_config(page_title="建築構造探索 20 案", layout="wide")

# 2. 自定義樣式
st.markdown("""
    <style>
    .main-title { color: #2c3e50; font-size: 2.2rem; font-weight: 700; margin-bottom: 2rem; border-bottom: 2px solid #eee; padding-bottom: 10px; }
    .section-header { color: #34495e; font-size: 1.6rem; margin-top: 1.5rem; font-weight: 600; border-left: 5px solid #2c3e50; padding-left: 15px; }
    .story-text { background-color: #f8f9fa; padding: 25px; border-radius: 8px; line-height: 1.7; color: #4a5568; font-style: italic; margin-bottom: 15px; }
    .question-text { color: #c05621; font-weight: 600; font-size: 1.15rem; margin: 1.5rem 0; padding: 10px; background-color: #fffaf0; border-radius: 5px; }
    .logic-box { background-color: #ebf4ff; padding: 20px; border-radius: 8px; margin-top: 10px; border: 1px solid #bee3f8; line-height: 1.6; }
    .doubt-box { background-color: #f7fafc; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 10px; color: #718096; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">建築構造探索筆記：全台 20 大建築力學解構</div>', unsafe_allow_html=True)

# 3. 側邊欄分類
category = st.sidebar.selectbox("選擇建築類別", [
    "地標與超高層建築",
    "表演藝術與文化空間",
    "地景、橋樑與特殊構造"
])

# --- 類別一：地標與超高層建築 ---
if category == "地標與超高層建築":
    tabs = st.tabs(["台北 101", "陶朱隱園", "高雄 85 大樓"])

    with tabs[0]:
        st.markdown('<div class="section-header">台北 101：雲端的質量平衡遊戲</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：從 Alex 的挑戰說起】**')
        st.markdown(
            '<div class="story-text">我看了一段攀岩大師 Alex Honnold 攀登這座建築的影像。當他懸掛在數百公尺高空，手指扣住那些竹節般的邊緣時，我意識到這座細長幾何體在物理上的「不安定感」。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：如何透過物理性的質量抵銷與幾何形狀設計，化解高空風力的強烈擾動？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">1. <b>TMD 阻尼器</b>：660 公噸金屬球抵銷擺盪。<br>2. <b>鋸齒轉角</b>：打碎氣流防止渦流脫離。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">複雜轉角設計在長期高空風壓下，對玻璃帷幕接頭的密合度是否有特殊要求？</div>',
                    unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="section-header">陶朱隱園：扭轉 90 度的節點應力</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：螢幕上的 DNA 奇觀】**')
        st.markdown(
            '<div class="story-text">在空拍影像中，這棟像「旋轉麻花」的建築完全顛覆我的認知。每一層樓轉 4.5 度，最終轉了 90 度。看著懸挑陽台，我懷疑中心柱真的不會因為扭力而斷掉嗎？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：如何透過核心筒與大跨度懸臂桁架，抵銷旋轉產生的巨大扭矩？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">採用「核心筒＋懸臂桁架」結構。主要重量由中間圓柱承擔，每兩層伸出「空腹桁架」將重量拉回核心。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">面對地震的「水平扭轉效應」時，其結構位移是否會比傳統建築更難預測？</div>',
                    unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="section-header">高雄 85 大樓：中空懸挑的力學支撐</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：捕捉風的開口】**')
        st.markdown(
            '<div class="story-text">看到 85 大樓中間有一個巨大的空洞。這種下半分叉、上部合體的造型，讓我覺得它在強風下會像一個巨大的捕風器，產生不穩定的推力。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：兩棟獨立側樓在頂部交會，銜接處如何處理不均勻沉陷帶來的應力？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這是「三塔式」結構。透過強大的轉換層與鋼構聯繫梁，將力量在三者間分配，增加整體剛性並減少受風面。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">風吹過開口產生的「穿孔風流」，對建築物表面的震動頻率有何長期影響？</div>',
                    unsafe_allow_html=True)

# --- 類別二：表演藝術與文化空間 ---
elif category == "表演藝術與文化空間":
    tabs = st.tabs(
        ["東京巨蛋", "台中歌劇院", "台北北藝", "高雄衛武營", "高雄高流", "蘭陽博物館", "鶯歌美術館", "嘉義故宮主體",
         "北投圖書館"])

    with tabs[0]:
        st.markdown('<div class="section-header">日本東京巨蛋：漂浮的白色雲朵</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">看棒球經典賽時，那片微透光的白色屋頂大到不可思議卻看不見鋼樑。那種空曠讓人好奇：萬一這片膜掉下來怎麼辦？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：如何利用大氣壓差，將厚重的膜材「吹」成一座堅不可摧的建築？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">屬於「空氣支撐結構」。室內氣壓高出室外 0.3%，微小壓差產生強大浮力，讓屋頂像充飽氣的皮球。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">若遇到強震電力中斷，屋頂下降的緩衝時間有多長？是否有備援支撐？</div>',
                    unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="section-header">台中國家歌劇院：垂直曲面</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">國小表演時被那些沙漏狀曲面震懾，這跟我認知中平整牆面完全不同。它是裝飾還是結構？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：垂直延伸的沙漏狀曲面，究竟是裝飾還是取代樑柱的骨架？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這是「壺中居」結構。利用 3D 噴漿混擬土讓牆與柱合一，重力順著曲面傳導至地基。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">面對強震水平剪力，複雜弧牆如何確保應力傳導而不產生裂縫？</div>',
                    unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="section-header">台北北藝中心：橫向生長</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">巨大的銀色圓球像是從方體長出來，視覺上極度不對稱，讓我懷疑它在地震中是否站得住腳。</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：當巨型圓球橫向延伸，銜接處如何化解應力集中？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">大跨度懸臂結構。球體重量透過內部鋼構桁架「拉」回核心，並配置抗震系統緩衝。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">非對稱設計在銜接處的鋼材疲勞問題，是否更難監測維修？</div>',
                    unsafe_allow_html=True)

    with tabs[3]:
        st.markdown('<div class="section-header">高雄衛武營：鋼鐵魟魚</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">像一條巨大的白色魟魚，完全找不到轉角。堅硬的鋼鐵如何建構出像布料一樣柔軟的線條？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：如何在超大面積連續曲面上，確保鋼構骨架與蒙皮精確銜接？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">採用「造船工法」。建構幾何鋼骨後，拼接數千片弧度各異鋼板。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">夏季高溫導致熱漲冷縮，一體成型外殼如何避免異音或變形？</div>',
                    unsafe_allow_html=True)

    with tabs[4]:
        st.markdown('<div class="section-header">高雄流行音樂中心：蜂巢挑戰</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">網路照片中蜂巢般的建築極具視覺衝擊，但不規則接點要如何確保整體的剛性？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：數千個非標準六角形鋼構件，如何維持穩定？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">採用「空間桁架系統」。每個六角形透過 3D 計算出的節點互相傳力。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">沿海高鹽分環境下，非標準接點的防鏽品質如何撐過數十年？</div>',
                    unsafe_allow_html=True)

    with tabs[5]:
        st.markdown('<div class="section-header">蘭陽博物館：傾斜大地</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：倒向水中的巨石】**')
        st.markdown(
            '<div class="story-text">在照片中看它像是歪掉的巨石。牆面與地面夾角很大，這種「歪掉」的房子怎麼撐住重力？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：模仿「單面山」的傾斜牆面，如何解決自重支撐與防水難題？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">利用斜牆作為結構牆，重力路徑雖偏斜，但透過底部穩固的斜向地基撐起。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">宜蘭多雨，傾斜牆面接縫的排水坡度與密封壽命如何維持？</div>',
                    unsafe_allow_html=True)

    with tabs[6]:
        st.markdown('<div class="section-header">鶯歌美術館：隱形重力</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：雜亂中的秩序】**')
        st.markdown(
            '<div class="story-text">銀色「鋁管」雜亂地插在地上。我完全看不出哪裡是牆，這種「去結構化」讓我不解承重牆躲在哪？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：細長圓管如何與內部鋼構結合，不干擾視覺輕盈感？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">鋁管僅是「遮陽格柵」。主重力由內部「巨型鋼構架」支撐，結構隱藏在陰影中。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">數千根鋁管在強風吹過河床時，是否會產生「風鳴聲」？</div>',
                    unsafe_allow_html=True)

    with tabs[7]:
        st.markdown('<div class="section-header">嘉義故宮南院（主體）：虛實交織</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">我家附近的建築。由玻璃與龍麟牆交織，那種交會處的複雜弧度，施工極易出錯。</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：不同性質曲面交會，結構界面如何處理應力傳遞？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">使用 3D 建模精確定位節點，透過鋼骨桁架將載重均勻分佈。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">三萬多個鑄鋁圓盤在地震擺盪時，是否有局部鬆脫風險？</div>',
                    unsafe_allow_html=True)

    with tabs[8]:
        st.markdown('<div class="section-header">北投圖書館：木構造極限</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：木頭能撐多久？】**')
        st.markdown(
            '<div class="story-text">看著支撐大屋簷的木樑，理科生疑問：木頭這種材料真的能撐起大跨度而不下垂變形嗎？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：大型木構造如何提升在潮濕氣候下的抗彎強度？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">採用「膠合木 (Glulam)」。纖維膠合強度超原木，接點嵌入鋼件承受拉力。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">木頭與鋼件熱漲冷縮係數不同，接點縫隙是否會成為水氣滲透死角？</div>',
                    unsafe_allow_html=True)

# --- 類別三：地景、橋樑與特殊構造 ---
elif category == "地景、橋樑與特殊構造":
    tabs = st.tabs(
        ["龍騰斷橋", "至美橋", "高跟鞋教堂", "淡江大橋", "花蓮新城車站", "彰化王功橋", "台南十鼓步道", "合歡山松雪樓",
         "民雄星巴克"])

    with tabs[0]:
        st.markdown('<div class="section-header">龍騰斷橋：紅磚殘弧</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown('<div class="story-text">地形極不平整，沒有鋼筋的年代，紅磚疊起的橋結構上到底怎麼平衡？</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：紅磚拱橋如何透過不等高橋墩撐起水平鐵軌？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">靠「半圓拱」傳力。計算各橋墩深度讓重力循拱形軌跡消散。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">糯米黏合無鋼筋，對抗地震水平晃動的極限在哪？</div>', unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="section-header">故宮南院至美橋：不對稱偏移</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown('<div class="story-text">嘉義人必知。重心完全偏向一側，流線曲面雖然漂亮，但總讓人覺得脆弱。</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：如何克服單側支撐帶來的巨大扭力？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">單塔斜張橋。利用螺旋鋼樑系統將載重轉化為旋轉應力。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">嘉義夏季強陣風大，雙曲面受風面積大，如何計算安全極限？</div>',
                    unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="section-header">嘉義高跟鞋教堂：隱形術</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown('<div class="story-text">玻璃是脆性材料不能承重，支撐巨大高跟鞋的骨架到底躲在哪裡？</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：如何隱藏鋼骨並解決玻璃熱漲冷縮破裂風險？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">內部「桁架式鋼骨」為內膽，玻璃透過「點支撐」掛在鋼構上。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">布袋海邊風勢強，颱風過境壓力差是否導致局部玻璃爆裂？</div>',
                    unsafe_allow_html=True)

    with tabs[3]:
        st.markdown('<div class="section-header">淡江大橋：單塔平衡</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown('<div class="story-text">一座橋塔撐長跨距，重心明顯不在中心，真的不會傾斜塌陷嗎？</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：如何透過斜張鋼纜達成不對稱設計下的平衡？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">利用「平衡懸臂法」調整左右鋼纜張力，將重力轉化為垂直壓力。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">河口風力大，單塔扭矩更大，減震系統如何設計？</div>', unsafe_allow_html=True)

    with tabs[4]:
        st.markdown('<div class="section-header">新城車站：懸浮山影</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：懸浮的摺紙】**')
        st.markdown('<div class="story-text">網路照片看大門像摺紙一邊完全無柱，在地震帶花蓮，真的不會重心不穩嗎？</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：摺紙造型懸臂重量，如何透過背後鋼構拉回地面？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">「鋼構懸臂桁架」。利用倒三角形剛性，將前端重量由後方深埋混凝土壓住。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">垂直震動時，末端鞭甩效應如何控制？</div>', unsafe_allow_html=True)

    with tabs[5]:
        st.markdown('<div class="section-header">彰化王功橋：摺板奇蹟</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：薄紙板景觀橋】**')
        st.markdown('<div class="story-text">像一片摺過薄鋼板橫跨河口，在海邊強風下看起來單薄得讓人擔心。</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：單薄鋼板如何透過「摺痕」增加力學剛性免支撐？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">「摺板結構」。原理如同摺紙增加慣性矩，提升抗彎能力支撐大跨度。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">海邊腐蝕一旦讓摺痕變薄，整體幾何剛性是否會瞬間崩潰？</div>',
                    unsafe_allow_html=True)

    with tabs[6]:
        st.markdown('<div class="section-header">台南十鼓：糖罐上的步道</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：鐵道掛罐上】**')
        st.markdown('<div class="story-text">我看著鐵件步道焊接在幾十年前鏽蝕舊糖罐上，懷疑真的能承載重量嗎？</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：如何確保舊工業遺構殘餘強度與新結構銜接安全？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">超音波探傷檢測。步道重量由新設「獨立鋼管柱」承擔，舊罐僅為聯繫點。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">鋼材疲勞肉眼難見，長期微震動是否會誘發舊鋼板裂縫？</div>',
                    unsafe_allow_html=True)

    with tabs[7]:
        st.markdown('<div class="section-header">合歡山松雪樓：海拔 3000 公尺</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：抗風雪的旅店】**')
        st.markdown(
            '<div class="story-text">站在山上風大到站不穩。全台最高旅館雪季承受好幾噸積雪，設計跟山下有何不同？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：極端低溫與重雪載重下，如何防止熱橋效應並維持剛性？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">屋頂大傾斜角排雪。使用高強度鋼骨與厚層外牆保溫模具防止熱能散失。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">極低溫下鋼材是否會產生「低溫脆裂」？選材有何標號要求？</div>',
                    unsafe_allow_html=True)

    with tabs[8]:
        st.markdown('<div class="section-header">民雄星巴克：斜頂對話</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：家鄉的歐式屋頂】**')
        st.markdown('<div class="story-text">就在我家鄉民雄。誇張三角形斜頂在鄉下很突兀，但好奇大雨時排水壓力多大？</div>',
                    unsafe_allow_html=True)
        st.markdown('<div class="question-text">❓ 設計提問：極大角度斜屋頂排水效應與抗風阻力如何平衡？</div>',
                    unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown('<div class="logic-box">內部鋼構支撐斜頂迅速排水，並強化地基抵銷側向風力的傾倒力矩。</div>',
                    unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">挑高空間熱對流管理，是否造成空調效能浪費？</div>', unsafe_allow_html=True)