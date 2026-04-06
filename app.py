import streamlit as st

# 1. 頁面基本設定
st.set_page_config(page_title="全台 20 大建築構造探索筆記", layout="wide")

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
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">我看著攀岩大師 Alex Honnold 挑戰 101 的紀錄片，他那雙滿是滑石粉的手扣住建築轉角時，我腦子裡想的不是他會不會掉下去，而是這棟樓在高空強風裡其實像根巨大的柳條。我盯著那竹節一樣一段一段往內收縮的設計，總覺得這結構背後一定藏了什麼我們看不見的對抗遊戲。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座細長的幾何體，如何透過物理性的質量抵銷與幾何形狀設計，化解高空風力的強烈擾動？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">1. <b>動態平衡 (TMD)</b>：懸掛於高層的 660 公噸阻尼球。2. <b>幾何流體力學</b>：竹節狀收縮與鋸齒轉角，能有效「打碎」氣流，防止形成規律的漩渦。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">這種複雜的轉角設計，在長期承受高空風壓下，對玻璃帷幕與鋼構接頭的密合度是否有特殊的耐久性要求？</div>',
            unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="section-header">陶朱隱園：扭轉 90 度的節點應力</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">這棟「旋轉麻花」真的太浮誇了，每次在網路上滑到照片都覺得這是不是 AI 生成的？每一層樓都在跟隔壁層玩「錯位」，陽台完全沒柱子就往外飄。我心裡一直有個理科生的執念：如果我帶個水平儀去頂樓，那種旋轉造成的重力感偏移，真的不會讓人走路歪一邊嗎？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：當建築樓層逐層旋轉，如何透過核心筒與大跨度懸臂桁架，抵銷旋轉產生的巨大扭矩？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">採用「核心筒＋懸臂桁架」結構。主要重量由中間圓柱承擔，兩側伸出像翅膀一樣的桁架將重量「拉」回核心，實現無柱空間。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">面對地震的「水平扭轉效應」時，其結構位移是否會比傳統方正大樓更難預測？</div>',
                    unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="section-header">高雄 85 大樓：中空懸挑的力學支撐</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">那次去高雄港，在下面仰頭看這棟樓，那個中間空掉的大洞真的很有壓迫感。這設計超像兩個巨人手牽手把中間空出來。我當時就在想，高雄颱風這麼多，風從那個洞噴過去的速度一定快得驚人，銜接點的鋼骨真的不會被這種長年的氣流撕開嗎？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：兩棟獨立的側樓在頂部交會合併，銜接處如何處理不均勻沉陷帶來的應力問題？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這是「三塔式」結構。透過強大的轉換層與鋼構聯繫梁，將力量在三者間分配，增加整體剛性，同時中空處可降低風壓。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">風吹過開口時產生的「穿孔風流」，對建築物表面的震動頻率有什麼影響？</div>',
                    unsafe_allow_html=True)

# --- 類別二：表演藝術與文化空間 ---
elif category == "表演藝術與文化空間":
    tabs = st.tabs(
        ["東京巨蛋", "台中歌劇院", "台北北藝", "高雄衛武營", "高雄高流", "蘭陽博物館", "鶯歌美術館", "嘉義故宮南院",
         "北投圖書館"])

    with tabs[0]:
        st.markdown('<div class="section-header">日本東京巨蛋：漂浮的白色雲朵</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">看 WBC 經典賽轉播的時候，我發現自己一直在看天花板。那一整片白色的屋頂完全沒有鋼樑，看起來薄得跟紙一樣，卻撐起了整個巨大的球場。這種「明明感覺很重卻能飄在半空」的視覺落差，讓我在看大谷翔平投球時，心裡還在想：氣壓這東西真的這麼神奇，能抵銷掉這幾萬公噸的重量？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這座球場是如何利用看不見的大氣壓差，將厚重的膜材「吹」成一座堅不可摧的建築？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">屬於「空氣支撐結構」。室內氣壓維持在比室外高出 0.3% 的狀態，產生強大的向上浮力，足以對抗風雪載重。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">若遇到強震導致電力中斷、加壓風扇停擺，屋頂下降的緩衝時間有多長？是否有物理性備援支撐？</div>',
            unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="section-header">台中國家歌劇院：誤入史前巨獸的內臟</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">在網路上刷到內部的環景照，我瞬間起雞皮疙瘩。那空間長得太像某種生物的氣孔或內臟了，完全找不到一根正常的柱子可以靠著。我不禁想，伊東豊雄當初在畫設計圖的時候，到底是怎麼算出這些彎來彎去的曲面該怎麼承重？這結構邏輯根本是外太空來的吧。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：垂直延伸的沙漏狀曲面，究竟是裝飾性的外衣，還是取代樑柱結構的骨架？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這並非裝飾，而是將牆與柱合一的「壺中居」結構。利用 3D 噴漿混擬土技術，讓牆面本身就具備承重路徑，實現大跨度無樑空間。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">面對強震時的水平剪力，這些複雜的弧形牆面（曲牆）是如何確保應力均勻傳導而不產生結構性裂縫？</div>',
            unsafe_allow_html=True)

    with tabs[2]:
        st.markdown('<div class="section-header">台北表演藝術中心：被方塊吞噬的巨型銀球</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">這就是大家都在吐槽的「皮蛋豆腐」，但我看到的是一種極致的不安全感。那個大銀球就像是硬生生塞進房子裡一樣，重心完全偏在一邊。我盯著它跟主體建築接合的那一圈，總覺得那裡的鋼結構一定每天都在承受很誇張的拉扯力，光看就覺得累。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：當巨型圓球從主建築橫向延伸，銜接處如何化解應力集中與扭轉破壞？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">屬於大跨度懸臂結構。球體重量透過內部的鋼構桁架「拉」回主體核心，並配置抗震系統，緩衝球體與主體間的位移。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">這種非對稱懸臂設計在銜接處的鋼材疲勞問題，是否會比一般對稱建築更難監測與維修？</div>',
            unsafe_allow_html=True)

    with tabs[3]:
        st.markdown('<div class="section-header">高雄衛武營：在鋼鐵大魟魚的肚子下</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">走在衛武營那片白色曲面下面，那感覺真的很難形容，像是一片被凝固住的海浪。我伸手去摸那硬邦邦的鋼板，心裡卻在想像造船廠的工人在銲接時的情景。要把幾千片各長各的鋼板拼成這麼順的曲線，這不是在蓋房子，這根本是在地表上造一艘巨大的潛水艇。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：如何在超大面積的連續曲面上，確保鋼構骨架與金屬蒙皮的精確銜接？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">採用類似「造船」的工法。先建構幾何鋼骨架，再將數千片弧度各異的鋼板拼接。這種組合讓建築外殼本身就具備極強的結構剛性。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">高雄夏季高溫會導致金屬劇烈熱漲冷縮，這種一體成型的外殼如何在受熱不均時避免異音或變形？</div>',
            unsafe_allow_html=True)

    with tabs[4]:
        st.markdown('<div class="section-header">高雄流行音樂中心：海港邊的未來蜂巢</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">在愛河口散步，這些六角形堆疊成的房子看起來超不真實，很像電影裡的未來實驗室。我最感興趣的是那些交錯的接點，在海邊這種高鹽分的地方，如果不規則的接點太多，防鏽根本是場噩夢。只要一個點蝕斷掉，這座「蜂巢」的穩定性會不會瞬間歸零？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：當建築外殼由數千個非標準化的六角形鋼構件組成，如何維持結構穩定？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">採用「空間桁架系統」。每個六角形透過 3D 座標精確計算出的節點互相傳力，將載重迅速分散到地面的支撐點。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">在沿海高鹽分的環境下，如何確保每個非標準化接點的防鏽品質能支撐數十年而不產生結構弱點？</div>',
            unsafe_allow_html=True)

    with tabs[5]:
        st.markdown('<div class="section-header">蘭陽博物館：即將沈入地底的三角巨石</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">IG 上的照片裡，這棟房子看起來就像快要倒進水裡的巨型石片。那種傾斜的角度讓我有種強迫症發作的感覺，好想把它扶正。我很好奇，住在裡面的人走在斜牆旁邊，大腦的平衡覺會不會被騙？這種「斜著站」的結構，到底得在地基埋多深才不會真的滑下去？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：這種模仿「單面山」造型的傾斜牆面，如何解決非垂直牆面的自重支撐與防水難題？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">利用斜牆作為結構牆，重力路徑雖偏斜，但透過底部穩固的斜向地基與鋼構撐起。斜面還能將雨水迅速導向景觀池。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">傾斜的落地窗與牆面接縫，在宜蘭多雨的環境下，其排水坡度與密封材料的壽命如何維持？</div>',
            unsafe_allow_html=True)

    with tabs[6]:
        st.markdown('<div class="section-header">鶯歌美術館：蘆葦叢中的消失密室</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">這建築的外觀就像是把幾千根銀色鋁管隨意插在土裡，視覺上超混亂。我一直在找這棟樓的「骨頭」在哪，但視線總是被那些管子切斷。這種把結構完全藏起來的設計，給人一種很輕、隨時會飛走的錯覺，但其實它內心應該是個超重的鋼鐵巨獸。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：外牆細長的鋁管如何與內部鋼構結合，在不干擾視覺輕盈感的狀況下完成水平抗風支撐？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">鋁管僅是「遮陽格柵」。真正的重力是由內部的一組「白色巨型鋼構架」支撐，讓支柱隱藏在鋁管的陰影中。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown('<div class="doubt-box">這幾千根管線在強風吹過鶯歌河床時，是否會產生規律的「風鳴聲」或高頻振動？</div>',
                    unsafe_allow_html=True)

    with tabs[7]:
        st.markdown('<div class="section-header">嘉義故宮南院（主體）：虛實交織的視覺糾纏</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">離我家不遠，我常去看這兩棟纏在一起的建築。一邊全是玻璃，一邊全是龍麟圓盤。我看著這兩者交會的地方，總覺得那是一個很激烈的「力學交界線」，不同材料熱漲冷縮的速度都不一樣，每次看都覺得這施工難度簡直是在自找麻煩。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：當兩個不同性質的曲面體（虛與實）交會，結構界面如何處理複雜的應力傳遞？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">使用 3D 建模精確定位每個鋼構節點，透過鋼骨桁架將載重均勻分佈在交織的支撐點上，確保整體穩定。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">龍麟牆上的三萬多個鑄鋁圓盤，在地震時產生的擺盪位移，是否會造成局部鬆脫的風險？</div>',
            unsafe_allow_html=True)

    with tabs[8]:
        st.markdown('<div class="section-header">北投圖書館：森林裡的木頭巨輪</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">在滿是硫磺味的北投，這座全木造的圖書館像是一艘停在樹林裡的方舟。我坐在陽台看著那延伸出去、大到不合理的屋簷，心裡盤算的不是文青感，而是台灣的濕氣。木頭這東西，如果沒有隱藏的鋼件在裡面撐著，真的能這樣漂漂亮亮地撐這麼久嗎？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：大型木構造如何透過集成材與鋼製連接件，提升木材在潮濕氣候下的抗彎強度與耐久性？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">採用膠合木 (Glulam)，強度遠超原木。關鍵接點嵌入了鋼製連接件，讓木材負責受壓，鋼件承受拉力，解決木材易裂問題。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">木頭與鋼件的熱漲冷縮係數不同，在長期溫度變化下，接點處的細微裂縫是否會導致內部腐朽？</div>',
            unsafe_allow_html=True)

# --- 類別三：地景、橋樑與特殊構造 ---
elif category == "地景、橋樑與特殊構造":
    tabs = st.tabs(
        ["龍騰斷橋", "故宮南院至美橋", "嘉義高跟鞋教堂", "淡江大橋", "花蓮新城車站", "彰化王功橋", "台南十鼓步道",
         "合歡山松雪樓", "民雄星巴克"])

    with tabs[0]:
        st.markdown('<div class="section-header">龍騰斷橋：紅磚殘肢的幾何奇蹟</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">站在斷橋下面，看那些沒了橋面、只剩紅磚拱門孤零零站著的樣子，心裡真的很有感觸。在那個連計算機都沒有的年代，先民是怎麼靠著疊磚塊的工法，就算出這麼精確的承重圓拱？即便斷了幾十年，剩下的結構依然能對抗地震，這就是純物理的浪漫。</div>',
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

    with tabs[1]:
        st.markdown('<div class="section-header">故宮南院至美橋：橫跨湖面的白色髮簪</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">這橋真的優雅到不行，但我每次走上去，目光都在找它的支撐點。它沒有對稱的塔架，重心歪得很有個性。對我這種理科生來說，這種不平衡的美感其實很折磨人，我總是在腦補它內部鋼樑是如何為了抵抗側向拉力而處於極度緊繃的狀態。</div>',
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

    with tabs[2]:
        st.markdown('<div class="section-header">嘉義高跟鞋教堂：被透明化的鋼鐵骨骼</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">布袋海邊這隻大藍鞋，雖然有人說它土，但我卻對它透明玻璃下的鋼鐵骨架著迷。這簡直是把建築剖開給你看。我看著那些細密的鋼骨，想像它們在颱風天要如何像牙籤一樣撐住這大受風面的玻璃殼，這絕對是海濱力學的一大挑戰。</div>',
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

    with tabs[3]:
        st.markdown('<div class="section-header">淡江大橋：夕陽下的單臂舞者</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">我看設計圖時差點沒看懂，竟然只有一座橋塔要撐起兩邊長短不一樣的橋面。這結構就像是一個人單腳站立還要單手提重物。這根橋塔得在地底下紮多深，才能確保在強大的側向風力下，不會連根拔起或是像翹翹板一樣翻過去？</div>',
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

    with tabs[4]:
        st.markdown('<div class="section-header">花蓮新城車站：在太魯閣口的白色摺紙</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">到站時被那個巨大的摺紙大門帥到了。它有一大半是懸空的，造型尖銳得很有攻擊性。但在花蓮這種地震熱區，這種「懸臂」設計真的很大膽。我盯著那個尖角，想像著縱波來的時候，它在那裡劇烈上下彈跳的樣子，這心臟得要很大顆才敢設計。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：摺紙造型產生的強大懸臂重量，如何透過背後的斜撐鋼構將重心拉回地面？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">這是巨大的「鋼構懸臂桁架」。利用倒三角形的幾何剛性，將前端重量轉化為後方基礎的「拉力」，後方有重石般的混凝土塊壓住。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">花蓮地震頻率高，這種長懸臂構造在面對垂直震動時，末端的鞭甩效應如何控制？</div>',
            unsafe_allow_html=True)

    with tabs[5]:
        st.markdown('<div class="section-header">彰化王功橋：薄如蟬翼的防風摺板</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">這橋看起來薄得不可思議，完全不像能載人的重型結構。它利用鋼板折疊的原理來增加強度，這點真的很有意思。但站在出海口那個強風吹得你站不穩的地方，看著這座輕盈的小橋，我真的很好奇，這種幾何形狀在面對「側向剪力」時真的夠硬嗎？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：看似單薄的鋼板摺紙造型，如何透過「摺痕」增加力學剛性，達到大跨度免中間撐柱效果？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">運用「摺板結構 (Folded Plate)」。摺痕改變了截面的慣性矩，大幅提升抗彎能力，讓鋼板能以極輕重量跨越長距離。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">王功海岸的高鹽分腐蝕環境若讓摺痕變薄，整體的幾何剛性是否會發生突發性崩潰？</div>',
            unsafe_allow_html=True)

    with tabs[6]:
        st.markdown('<div class="section-header">台南十鼓天空步道：環繞廢墟的驚悚透明</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">在舊工廠裡走這種掛在天上的步道，真的會手腳發軟。我看著步道的扣件直接鎖在那些已經生鏽、甚至有點斑駁的舊糖罐鋼板上，心裡不斷在想：這就是新舊力學的博弈。雖然工程師說沒問題，但每當前面的遊客走快一點，步道傳來的震動還是讓我滿腦子都是鋼材疲勞的畫面。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：在舊有的工業遺構上增建載重步道，如何確保舊結構的殘餘強度與新結構的銜接安全性？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">利用「獨立基腳」或避開鏽蝕處。步道重量主要傳導至新基礎，糖罐僅作為側向聯繫。施工前會進行超音波探傷檢測鋼板厚度。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">工業鋼材的疲勞損傷是不可逆的，長期遊客負載產生的微震動，是否會誘發舊鋼板內部的微裂縫擴張？</div>',
            unsafe_allow_html=True)

    with tabs[7]:
        st.markdown('<div class="section-header">合歡山松雪樓：海拔 3000 公尺的力學</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">站在海拔 3000 多公尺的山上，風大到讓人站不穩。這棟全台灣最高的旅館，在雪季時要承受好幾噸的積雪，它的結構設計跟山下的房子有什麼不同？我一直在想，如果是普通的鋼筋水泥，在這種冰天雪地裡真的不會被凍裂嗎？</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：在高海拔極端低溫與重雪載重下，建築如何結合結構剛性與斷熱設計防止熱橋效應？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">強化屋頂傾斜角度加速排雪。採用高強度鋼骨與特殊厚層保溫模具，並在施工中加入抗凍劑確保混凝土品質。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">在極度低溫下，鋼材是否會產生「低溫脆裂」現象？這在選材上有什麼特殊標號要求？</div>',
            unsafe_allow_html=True)

    with tabs[8]:
        st.markdown('<div class="section-header">嘉義民雄星巴克：鄉間稻田裡的歐式屋頂</div>', unsafe_allow_html=True)
        st.markdown('**【我的故事】**')
        st.markdown(
            '<div class="story-text">就在家鄉民雄，那黑色大屋簷斜得很有氣勢。我常在下大雨的時候去買咖啡，盯著那大斜面的水瀑往下衝。這種造型在美學上很有特色，但在力學上，它其實像是一面巨大的帆。我想知道，地基裡到底用了多少混凝土，才確保這間咖啡店在強陣風來時不會像風箏一樣飛走。</div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div class="question-text">❓ 設計提問：極大角度的斜屋頂在視覺與排水效應間如何平衡？其結構對側向風力的阻力又是如何設計的？</div>',
            unsafe_allow_html=True)
        st.markdown('**【理性求證】**')
        st.markdown(
            '<div class="logic-box">內部採用鋼構支撐大角度斜頂，斜面能迅速排開積水。地基部分經過特別加重，用以抵銷大受風面產生的側向翻轉力矩。</div>',
            unsafe_allow_html=True)
        st.markdown('**【保留疑問】**')
        st.markdown(
            '<div class="doubt-box">大面積斜頂造成的室內挑高空間，在熱對流管理上是否會造成空調效能的巨大浪費？</div>',
            unsafe_allow_html=True)