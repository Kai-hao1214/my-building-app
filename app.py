import streamlit as st

# 1. 頁面基本設定
st.set_page_config(page_title="建築構造探索筆記", layout="wide")

# 2. 自定義樣式 (解決字體不清與深色模式對比度問題)
st.markdown("""
<style>
    /* 強制設定背景顏色，避免自動切換導致字體看不見 */
    .stApp { background-color: #0e1117; } 

    /* 主標題 */
    .main-title { 
        color: #63b3ed !important; 
        font-size: 2.5rem; 
        font-weight: 800; 
        margin-bottom: 2rem; 
        border-bottom: 3px solid #2d3748; 
        padding-bottom: 10px; 
    }

    /* 建築名稱 (分頁標題) */
    .section-header { 
        color: #ffffff !important; 
        font-size: 1.8rem; 
        margin-top: 1.5rem; 
        font-weight: 700; 
        border-left: 6px solid #4299e1; 
        padding-left: 15px; 
        margin-bottom: 20px;
    }

    /* 【我的故事】：淺灰色背景 + 深色字 */
    .story-text { 
        background-color: #e2e8f0 !important; 
        padding: 20px; 
        border-radius: 10px; 
        line-height: 1.8; 
        color: #1a202c !important; 
        font-style: italic; 
        margin-bottom: 15px; 
        font-size: 1.1rem;
        border: 1px solid #cbd5e0;
    }

    /* 【設計提問】：亮黃色背景 + 深棕色字 */
    .question-text { 
        color: #744210 !important; 
        font-weight: 700; 
        font-size: 1.15rem; 
        margin: 1.5rem 0; 
        padding: 15px; 
        background-color: #fefcbf !important; 
        border-radius: 8px; 
        border: 1px solid #faf089;
    }

    /* 【理性求證】：淺藍色背景 + 深藍色字 */
    .logic-box { 
        background-color: #bee3f8 !important; 
        padding: 20px; 
        border-radius: 10px; 
        margin-top: 10px; 
        border: 1px solid #90cdf4; 
        line-height: 1.7; 
        color: #2a4365 !important; 
        font-size: 1.1rem;
    }

    /* 【保留疑問】：淡灰色背景 + 深灰色字 */
    .doubt-box { 
        background-color: #edf2f7 !important; 
        padding: 15px; 
        border-radius: 8px; 
        border: 1px solid #cbd5e0; 
        margin-top: 10px; 
        color: #4a5568 !important; 
    }

    /* 修正 Tab 標籤顏色 */
    .stTabs [data-baseweb="tab"] { color: #a0aec0; }
    .stTabs [aria-selected="true"] { color: #63b3ed; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">建築構造探索筆記：全台 20 大案例分析</div>', unsafe_allow_html=True)

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
        st.markdown(
            '<div class="story-text">我看著攀岩大師 Alex Honnold 挑戰 101 的紀錄片，他那雙滿是滑石粉的手扣住建築轉角時，我腦子裡想的不是他會不會掉下去，而是這棟樓在高空強風裡其實像根巨大的柳條。我盯著那竹節一樣一段一段往內收縮的設計，總覺得這結構背後一定藏了什麼我們看不見的對抗遊戲。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座細長的幾何體，如何透過物理性的質量抵銷與幾何形狀設計，化解高空風力的強烈擾動？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="logic-box">1. <b>動態平衡 (TMD)</b>：懸掛於高層的 660 公噸阻尼球。2. <b>幾何流體力學</b>：竹節狀收縮與鋸齒轉角，能有效「打碎」氣流，防止形成規律的漩渦。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="doubt-box"><b>【保留疑問】</b>：這種複雜的轉角設計，在長期承受高空風壓下，對玻璃帷幕與鋼構接頭的密合度是否有特殊的耐久性要求？</div>',
            unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="section-header">陶朱隱園：扭轉 90 度的 DNA 迷宮</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">信義區這棟「旋轉麻花」真的太浮誇了，每次在網路上滑到照片都覺得這是不是 AI 生成的？每一層樓都在跟隔壁層玩「錯位」，陽台完全沒柱子就往外飄。我心裡一直有個理科生的執念：如果我帶個水平儀去頂樓，那種旋轉造成的重力感偏移，真的不會讓人走路歪一邊嗎？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：當建築樓層逐層旋轉，如何透過核心筒與大跨度懸臂桁架，抵銷旋轉產生的巨大扭矩？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="logic-box">採用「核心筒＋懸臂桁架」結構。主要重量由中間圓柱承擔，兩側伸出像翅膀一樣的桁架將重量「拉」回核心。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="doubt-box"><b>【保留疑問】</b>：面對地震的「水平扭轉效應」時，其結構位移是否會比傳統方正大樓更難預測？</div>',
            unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="section-header">高雄 85 大樓：中空懸挑的力學支撐</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">那次去高雄港，在下面仰頭看這棟樓，那個中間空掉的大洞真的很有壓迫感。這設計超像兩個巨人手牽手把中間空出來。我當時就在想，高雄颱風這麼多，風從那個洞噴過去的速度一定快得驚人，銜接點的鋼骨真的不會被這種長年的氣流撕開嗎？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：兩棟獨立的側樓在頂部交會合併，銜接處如何處理不均勻沉陷帶來的應力問題？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="logic-box">這是「三塔式」結構。透過強大的轉換層與鋼構聯繫梁，將力量在三者間分配，增加整體剛性，同時中空處可降低風壓。</div>',
            unsafe_allow_html=True)

# --- 類別二：表演藝術與文化空間 ---
elif category == "表演藝術與文化空間":
    tabs = st.tabs(
        ["東京巨蛋", "台中歌劇院", "台北北藝", "高雄衛武營", "高雄高流", "蘭陽博物館", "鶯歌美術館", "嘉義故宮南院",
         "北投圖書館"])

    with tabs[0]:
        st.markdown('<div class="section-header">東京巨蛋：漂浮的白色雲朵</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">看 WBC 轉播的時候，我發現自己一直在看天花板。那一整片白屋頂完全沒鋼樑，薄得跟紙一樣卻撐起球場。這種視覺落差讓我在想：氣壓這東西真的這麼神奇，能抵銷掉這幾萬公噸的重量？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="logic-box">屬於「空氣支撐結構」。室內氣壓維持在比室外高出 0.3% 的狀態，產生強大的向上浮力。</div>',
            unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="section-header">台中國家歌劇院：史前巨獸的內臟</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">（雲端觀察）刷到內部的照片，我瞬間起雞皮疙瘩。那空間太像某種生物的內臟了，完全找不到正常的柱子可以靠著。我不禁想，伊東豊雄當初到底是怎麼算出這些彎來彎去的曲面該怎麼承重？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="logic-box">將牆與柱合一的「壺中居」結構。利用 3D 噴漿混擬土技術，讓牆面本身就具備承重路徑。</div>',
            unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="section-header">台北北藝中心：被方塊吞噬的銀球</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">這就是「皮蛋豆腐」。大銀球重心完全偏在一邊。我盯著它跟主體接合的那一圈，總覺得那裡的鋼結構一定每天都在承受很誇張的拉扯力。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="logic-box">大跨度懸臂結構。球體重量透過內部的鋼構桁架「拉」回主體核心，並配置抗震系統。</div>',
            unsafe_allow_html=True)

    with tabs[3]:
        st.markdown('<div class="section-header">高雄衛武營：鋼鐵大魟魚</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">走在衛武營那片白色曲面下，像是一片被凝固住的海浪。我伸手去摸鋼板，想像造船廠的工人在銲接時的情景。要把幾千片鋼板拼成這麼順的曲線，這是在地表上造一艘巨大的潛水艇吧。</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="logic-box">採用造船工法。先建構幾何鋼骨架，再將數千片弧度各異的鋼板拼接。</div>',
                    unsafe_allow_html=True)

    with tabs[4]:
        st.markdown('<div class="section-header">高雄流行音樂中心：未來蜂巢</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">在愛河口散步，這些六角形房子看起來超不真實。我最感興趣的是那些接點，在海邊高鹽分的地方，如果不規則的接點太多，只要一個蝕斷掉，這座「蜂巢」會不會垮掉？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="logic-box">採用「空間桁架系統」。每個六角形節點互相傳力，將載重迅速分散到地面。</div>',
                    unsafe_allow_html=True)

    with tabs[5]:
        st.markdown('<div class="section-header">蘭陽博物館：沈入地底的三角巨石</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">（雲端觀察）這棟房子像快要倒進水裡的巨型石片。那種角度讓我有強迫症，好想把它扶正。我很好奇，住在裡面走在斜牆旁，大腦的平衡覺會不會被騙？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="logic-box">斜牆即結構牆。雖然重力路徑偏斜，但透過底部穩固的斜向地基撐起。</div>',
                    unsafe_allow_html=True)

    with tabs[6]:
        st.markdown('<div class="section-header">鶯歌美術館：蘆葦叢中的消失密室</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">外觀像把幾千根鋁管隨意插在土裡。我一直在找「骨頭」在哪，但視線總是被管子切斷。這種把結構藏起來的設計，給人一種隨時會飛走的錯覺。</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="logic-box">鋁管僅是遮陽。真正重力由內部的白色巨型鋼構架支撐。</div>',
                    unsafe_allow_html=True)

    with tabs[7]:
        st.markdown('<div class="section-header">故宮南院主體：虛實交織</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">離我家不遠，我常去看這兩棟纏在一起的建築。一邊玻璃一邊龍麟圓盤。交會的地方熱漲冷縮速度都不一樣，每次看都覺得這施工難度簡直自找麻煩。</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="logic-box">3D 建模精確定位節點，透過鋼骨桁架將載重均勻分佈在交織的支撐點。</div>',
                    unsafe_allow_html=True)

    with tabs[8]:
        st.markdown('<div class="section-header">北投圖書館：森林裡的方舟</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">在滿是硫磺味的北投，這座木造圖書館像停在樹林裡的方舟。我看著那大到不合理的屋簷，心裡盤算的是濕氣。木頭如果沒隱藏鋼件，真的能撐這麼久嗎？</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="logic-box">採用膠合木 (Glulam)，關鍵接點嵌入鋼製連接件，讓木材受壓、鋼件承受拉力。</div>',
                    unsafe_allow_html=True)

# --- 類別三：地景、橋樑與特殊構造 ---
elif category == "地景、橋樑與特殊構造":
    tabs = st.tabs(["龍騰斷橋", "至美橋", "高跟鞋教堂", "淡江大橋", "新城車站", "王功橋", "十鼓步道", "民雄星巴克"])

    with tabs[0]:
        st.markdown('<div class="section-header">龍騰斷橋：紅磚殘肢</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">沒了橋面、只剩紅磚拱門孤零零站著。以前的人沒電腦，光靠疊磚塊就能算出承重圓拱，斷了幾十年依然能對抗地震，這就是純物理的浪漫。</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="logic-box">靠紅磚堆疊的「半圓拱」傳力。重力循著拱形軌跡消散至橋墩。</div>',
                    unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="section-header">至美橋：白色髮簪</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">橋真的優雅，但我每次走上去都在找支撐點。重心歪得很有個性。對理科生來說這不平衡感很折磨人，我總在腦補它內部鋼樑是如何緊繃。</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="logic-box">單塔斜張橋，利用螺旋鋼樑支撐，將載重轉化為旋轉應力。</div>',
                    unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="section-header">高跟鞋教堂：透明骨骼</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="story-text">布袋大藍鞋，透明玻璃下全是鋼骨。這簡直是把建築剖開。我看著那些細密鋼骨，想像它們在颱風天要如何撐住大受風面的玻璃殼。</div>',
            unsafe_allow_html=True)
        st.markdown('<div class="logic-box">桁架式鋼骨內膽，玻璃透過「點支撐」掛在鋼構上。</div>', unsafe_allow_html=True)

    with tabs[3]:
        st.markdown('<div class="section-header">淡江大橋：單臂舞者</div>', unsafe_allow_html=True