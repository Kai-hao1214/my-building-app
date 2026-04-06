import streamlit as st

# 1. 頁面基本設定
st.set_page_config(page_title="建築構造探索筆記", layout="wide")

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

st.markdown('<div class="main-title">建築構造探索筆記：從美學直覺到理性求證</div>', unsafe_allow_html=True)

# 3. 側邊欄分類選擇
category = st.sidebar.selectbox("選擇建築類別", ["地標與超高層建築", "表演藝術與文化空間", "地景、橋樑與特殊構造"])

# --- 類別一：地標與超高層建築 ---
if category == "地標與超高層建築":
    tab1 = st.tabs(["台北 101"])
    with tab1[0]:
        st.markdown('<div class="section-header">台北 101：雲端的質量平衡遊戲</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事：從 Alex 的挑戰說起】**')
        st.markdown(
            '<div class="story-text">我對台北 101 的結構產生興趣，是因為看了一段攀岩大師 Alex Honnold 攀登這座建築的影像。當他懸掛在數百公尺高空，手指扣住那些竹節般的邊緣時，我意識到的是這座細長幾何體在物理上的「不安定感」。在高空強勁陣風中，它如何維持穩定，而不讓頂端的攀爬者感受到致命擺盪？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座細長的幾何體，如何透過物理性的質量抵銷與幾何形狀設計，化解高空風力的強烈擾動？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證：雙重抗風機制】**')
        st.markdown(
            '<div class="logic-box">1. <b>動態平衡 (TMD)</b>：懸掛於高層的 660 公噸金屬阻尼球，利用物理慣性抵銷大樓擺盪。<br>2. <b>幾何流體力學 (Saw-tooth Design)</b>：竹節狀收縮與轉角鋸齒，能有效「打碎」高空氣流，防止形成規律的漩渦（渦流脫離），從根本上降低風力推力。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">這種複雜的轉角設計，在長期承受高空風壓與日照熱漲冷縮循環下，對玻璃帷幕與鋼構接頭的密合度是否有特殊的材料耐久性要求？</div>',
            unsafe_allow_html=True)

# --- 類別二：表演藝術與文化空間 ---
elif category == "表演藝術與文化空間":
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["東京巨蛋", "台中歌劇院", "台北北藝中心", "高雄衛武營", "高雄高流中心"])

    with tab1:
        st.markdown('<div class="section-header">日本東京巨蛋：漂浮的白色雲朵</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為運動迷，看經典賽時我的目光不只在投手丘上。巨蛋那片微透光的白色屋頂，大到不可思議卻看不見任何鋼樑支撐。那種極致的空曠讓人在熱血之餘總有一絲不安：萬一這片膜掉下來怎麼辦？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座球場是如何利用看不見的大氣壓差，將厚重的膜材「吹」成一座堅不可摧的建築？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這屬於「空氣支撐結構」。室內氣壓維持在比室外高出 0.3% 的狀態，這微小的壓差產生了強大的向上浮力，讓屋頂像充飽氣的皮球一樣繃緊，足以對抗風雪載重。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">若遇到強震導致電力中斷、加壓風扇停擺，屋頂下降的緩衝時間有多長？是否有物理性的備援支撐防止塌陷？</div>',
            unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="section-header">台中國家歌劇院：流動的垂直曲面</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">國小表演時，我被外牆那些沙漏般的曲面震懾住。這些弧線是垂直延伸的，跟我認知中平整的牆面完全不同。我當時在想，這是不是在傳統柱子外面貼了一層厚水泥裝飾皮？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：垂直延伸的沙漏狀曲面，究竟是裝飾性的外衣，還是取代樑柱結構的骨架？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這並非裝飾，而是將牆與柱合一的「壺中居」結構。利用 3D 噴漿混擬土技術，讓牆面本身就具備承重路徑，重力順著曲面傳導至地基，實現無樑柱的大跨度空間。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">面對強震時的水平剪力，這些複雜的弧形牆面（曲牆）是如何確保應力均勻傳導而不產生結構性裂縫？</div>',
            unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="section-header">台北表演藝術中心：橫向生長的幾何</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">巨大的銀色圓球像是從方體中突然長出來一樣，視覺上極度不對稱且重心明顯偏移。這種違反直覺的生長方式，讓我懷疑它在地震頻繁的台灣是否真的站得住腳。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：當巨型圓球從主建築橫向延伸，銜接處如何化解應力集中與扭轉破壞？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這屬於大跨度懸臂結構。球體重量透過內部的鋼構桁架「拉」回主體核心，並配置 S-SISO 抗震系統，緩衝球體與主體間的震動撕裂力。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">長期使用下，這種非對稱懸臂設計在銜接處的鋼材疲勞問題，是否會比一般對稱建築更難監測與維修？</div>',
            unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="section-header">高雄衛武營：鋼鐵魟魚的曲面蒙皮</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">這座建築像一條貼在大地上的巨大魟魚，屋頂是連續的曲面，完全找不到傳統的轉角。我想知道，這種像布料一樣柔軟的線條，要如何用堅硬的鋼鐵建構出來？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：如何在超大面積的連續曲面上，確保鋼構骨架與金屬蒙皮的精確銜接？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">採用類似「造船」的工法。先建構精密幾何鋼骨骨架，再將數千片弧度各異的鋼板拼接。這種「單/雙曲率」的組合，讓建築外殼本身就具備極強的結構剛性。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">高雄夏季高溫會導致金屬劇烈熱漲冷縮，這種一體成型的外殼如何在受熱不均時避免應力導致的異音或變形？</div>',
            unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="section-header">高雄流行音樂中心：蜂巢狀的抗拉挑戰</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">在網路上看到照片時，很難不被那座像「蜂巢」一樣的建築吸引。它由無數個六角形組成，表面起伏不平。這種複雜的幾何外殼，讓我好奇這麼多不規則的接點，要如何確保整體的剛性？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：當建築外殼由數千個非標準化的六角形鋼構件組成，如何維持結構穩定？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">採用「空間桁架系統（Space Truss）」。每個六角形透過 3D 座標精確計算出的節點互相傳力，將載重迅速分散到地面的支撐點。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">在沿海高鹽分的環境下，如何確保每個非標準化接點的防鏽品質能支撐數十年而不產生結構弱點？</div>',
            unsafe_allow_html=True)

# --- 類別三：地景、橋樑與特殊構造 ---
elif category == "地景、橋樑與特殊構造":
    tab1, tab2, tab3, tab4 = st.tabs(["龍騰斷橋", "故宮南院至美橋", "嘉義高跟鞋教堂", "淡江大橋"])

    with tab1:
        st.markdown('<div class="section-header">龍騰斷橋：崎嶇地貌上的殘弧</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">地形極度不平整且兩岸高度不同。要在這種地方用紅磚疊起一座能跑火車的橋，在沒有鋼筋的年代，結構上到底怎麼平衡？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：在崎嶇地貌中，紅磚拱橋如何透過高度不等的橋墩撐起水平的鐵軌路徑？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">靠紅磚堆疊的「半圓拱」傳力。透過精確計算各橋墩深度與高度，讓重力循著拱形軌跡消散，確保頂端水平。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">單純靠紅磚與糯米黏合，完全沒有鋼筋牽引，它對抗強烈地震水平晃動的力學極限在哪？</div>',
            unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="section-header">故宮南院至美橋：不對稱的力學偏移</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">身為嘉義人，我對這座橋非常熟悉。它的視覺重心完全偏向一側，在流線型的曲面中，雖然漂亮，但總讓人覺得它比一般的橋還要「脆弱」一些。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座橋看似輕盈地橫跨水面，在物理層面上如何克服單側支撐帶來的巨大扭力？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這是單塔斜張橋，利用內部螺旋鋼樑支撐系統，將不對稱載重轉化為旋轉應力傳導至兩側混凝土錨座。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">嘉義夏季常有強陣風，這種雙曲面大受風面積，設計上是如何計算風致振動的安全極限？</div>',
            unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="section-header">嘉義高跟鞋教堂：骨架隱形術</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">這座建築就在我熟悉的地方。玻璃是脆性材料，不能承重。支撐這隻巨大「高跟鞋」的骨架到底躲在哪裡？為什麼看不到樑柱？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：如何在高透光的玻璃帷幕建築中隱藏鋼骨，並解決熱漲冷縮產生的破裂風險？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">內部使用「桁架式鋼骨結構」作為內膽，玻璃透過「點支撐」掛在鋼構上。鋼樑被刻意設計得輕薄並塗上淡藍色，消融在背景中。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">布袋海邊風勢極強，大面積曲面玻璃外殼在颱風過境時，其氣動壓力差是否會導致局部玻璃爆裂？</div>',
            unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="section-header">淡江大橋：單塔不對稱斜張</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">只有一座橋塔卻要撐起極長跨距，重心明顯不在中心點，這座橋真的不會因為左右不對稱而傾斜塌陷嗎？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：在不對稱的單塔設計下，如何透過斜張鋼纜的張力調整，達成整座橋樑的重力平衡？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">利用「平衡懸臂法」與精密鋼纜張力調整。透過調整左右鋼纜的拉力值，將不對稱重力轉化為對橋塔的垂直壓力。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">淡水河口風力極大，單塔結構面對側向陣風產生的「扭矩」更大，內部的減震系統如何設計？</div>',
            unsafe_allow_html=True)