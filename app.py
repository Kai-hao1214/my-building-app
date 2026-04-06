import streamlit as st

# 頁面基本設定
st.set_page_config(page_title="建築構造探索筆記", layout="wide")

# 自定義界面樣式（去除冗餘裝飾，保持大學生筆記的質感）
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #2c3e50; }
    .main-title { color: #1a73e8; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem; }
    .sub-title { color: #5f6368; font-size: 1.1rem; margin-bottom: 2rem; }
    .section-header { color: #1a73e8; border-left: 4px solid #1a73e8; padding-left: 1rem; margin-top: 2rem; }
    .question-text { font-style: italic; color: #e67e22; font-weight: 500; font-size: 1.2rem; margin: 1.5rem 0; }
    .ref-box { background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin-top: 20px; font-size: 0.9rem; }
    </style>
    """, unsafe_allow_html=True)

# 標題與個人資訊
st.markdown('<div class="main-title">建築構造探索筆記</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">探索者：劉楷皓 | 關於物理法則與建築美學的邊界觀測</div>', unsafe_allow_html=True)

# 側邊欄分類選擇
category = st.sidebar.selectbox(
    "選擇建築類別",
    ["表演藝術與文化空間", "歷史與地景構造", "其他待定案例"]
)

# --- 第一類：表演藝術與文化空間 ---
if category == "表演藝術與文化空間":
    tab1, tab2, tab3 = st.tabs(["日本東京巨蛋", "台中國家歌劇院", "台北表演藝術中心"])

    with tab1:
        st.markdown('<h2 class="section-header">東京巨蛋 — 漂浮於沸騰之上的白色雲朵</h2>', unsafe_allow_html=True)
        st.write("身為一名熱血運動迷，看經典賽時我的目光不只在投手丘上。東京巨蛋那片純白、微透光的屋頂總讓我感到不安——它大到不可思議，卻在內部看不見任何一根鋼樑或立柱。這種極致的空曠，讓人在熱血吶喊之餘，也會不自覺地擔心：萬一這片像雲朵一樣輕飄飄的屋頂掉下來，底下的球員與數萬名觀眾該怎麼辦？")
        st.markdown('<div class="question-text">消失的樑柱：如何利用看不見的大氣壓差，將厚重的膜材吹成一座堅不可摧的球場？</div>', unsafe_allow_html=True)
        st.write("技術關鍵在於場館內部的氣壓。透過 36 台大型送風機不間斷地運作，室內氣壓始終維持在比室外高出 0.3% 的狀態。這看似微小的壓差，卻能對屋頂產生每平方米約 30 公斤的向上浮力，扣除膜材重量後，剩餘的張力讓屋頂像被充飽氣的皮球一樣繃緊，即便面對強風與積雪，依然能維持結構的穩定與彈性。")
        st.image("https://via.placeholder.com/1000x500?text=Tokyo+Dome+Photo", caption="日本東京巨蛋：空氣支撐結構示意")
        with st.expander("參考資料"):
            st.markdown("""
            * Tokyo Dome City 官網：關於巨蛋的秘密：氣壓與屋頂結構。
            * 朝日新聞報導：2014年大雪中球場如何透過增加氣壓防止崩塌的實戰經驗。
            """)

    with tab2:
        st.markdown('<h2 class="section-header">台中國家歌劇院 — 擺脫束縛的流動構造</h2>', unsafe_allow_html=True)
        st.write("國小跟著直笛隊來這裡表演時，我並非直接走入大廳，而是先被建築外牆那一個個巨大的、像沙漏般收束又展開的曲面給震懾住。那些弧線完全是垂直延伸的，跟我認知中平整的牆面大相徑庭。我當時甚至在想，這是不是在原本方正的鋼筋混凝土柱子外面，刻意貼上了一層厚厚的水泥裝飾？畢竟，如果裡面沒有直挺挺的樑柱，這座巨大的建築怎麼可能支撐得住？")
        st.markdown('<div class="question-text">結構的視覺詐術：這些垂直延伸的沙漏狀曲面，究竟是裝飾性的外衣，還是支撐建築命脈的骨架？</div>', unsafe_allow_html=True)
        st.write("這並非裝飾，而是將牆與柱合而為一的極致工程。這些看到的沙漏狀曲面，在工程上被稱為「壺中居」結構單元。工程師捨棄傳統板模，將鋼筋依照 3D 模型編織成網後，直接使用 3D 噴漿混凝土技術。這意味著每一道弧線本身就是這棟建築的受力路徑，重力順著曲面滑行、消散到地下。")
        st.image("https://via.placeholder.com/1000x500?text=Taichung+Opera+House+Photo", caption="台中國家歌劇院：曲面牆受力結構")
        with st.expander("參考資料"):
            st.markdown("""
            * 天下雜誌：伊東豊雄專訪——台中歌劇院，是我建築職涯最難的挑戰。
            * 建築現場觀察：曲面牆體接合點無直角特徵，證實結構一體化論點。
            """)

    with tab3:
        st.markdown('<h2 class="section-header">台北表演藝術中心 — 懸浮於城市的銀色行星</h2>', unsafe_allow_html=True)
        st.write("這座建築最吸引我的是那種視覺上的突變感——那個巨大的銀色圓球像是從方正的主建築中突然長出來一樣。這種不自然的銜接讓我感到困惑：在物理法則下，一個如此巨大的球體突出於結構主體之外，它的交界處難道不會因為重量不均而產生巨大的撕裂力嗎？這種違反直覺的生長方式，到底是如何在結構上實現支撐？")
        st.markdown('<div class="question-text">結構的斷層：當圓球從方盒體中橫向生長，銜接處是如何化解極端的應力集中與扭轉破壞？</div>', unsafe_allow_html=True)
        st.write("這在結構上屬於大跨度懸臂結構。球體並非只是貼在表面，而是透過一組強大的內核鋼構桁架，將重量往回拉進主建築的核心牆中。為了應對地震，球體與主體交接處配置了 S-SISO 抗震系統與阻尼裝置，讓球體在受震動時能與主體達成動態協調，化解不同幾何形狀產生的剪力。")
        st.image("https://via.placeholder.com/1000x500?text=Taipei+Performing+Arts+Center+Photo", caption="台北表演藝術中心：懸臂鋼構與球體銜接")
        with st.expander("參考資料"):
            st.markdown("""
            * 建築師 Rem Koolhaas 紀錄片：詳述球體劇院的懸浮設計挑戰。
            * ARCHDAILY 建築評論：探討北藝中心如何透過結構創新解決不對稱形體的重心問題。
            """)

# --- 第二類：歷史與地景構造 ---
elif category == "歷史與地景構造":
    tab1, tab2 = st.tabs(["龍騰斷橋", "故宮南院"])

    with tab1:
        st.markdown('<h2 class="section-header">龍騰斷橋 — 在不可能的地基上與重力角力</h2>', unsafe_allow_html=True)
        st.write("小時候跟家人去三義旅遊，我發現這裡的環境非常荒謬——橋址的地面根本不平整，兩岸高低落差極大且河谷深邃。在我的直覺裡，這地方一點都不適合蓋橋。我一直在想，要在這種不平的地方用紅磚疊起一座能跑火車的橋，在結構上到底是怎麼平衡的？難道當時的工程師看不出地貌條件極差嗎？")
        st.markdown('<div class="question-text">地標的生存邏輯：在崎嶇不平的河谷中，紅磚拱橋是如何透過高度不等、甚至不在同一水平線上的橋墩，撐起平直的鐵道？</div>', unsafe_allow_html=True)
        st.write("這座橋採用了多連連續拱結構。為了克服深谷地形，工程師針對不同位置的橋墩設計了不等的深度與高度。透過半圓拱原理，將磚頭之間的壓力導向不對稱的橋墩。雖然地貌崎嶇，但計算出的受力分佈確保了頂端鐵軌的水平。斷裂主因是 1935 年地震碎了最脆弱的拱心石，導致力學平衡瓦解。")
        st.image("https://via.placeholder.com/1000x500?text=Longteng+Bridge+Photo", caption="龍騰斷橋：磚造拱橋力學路徑")
        with st.expander("參考資料"):
            st.markdown("""
            * 台灣總督府鐵道部史料：關於魚藤坪溪橋修築紀錄。
            * 國家地震工程研究中心：早期砌體拱橋的震災行為模擬報告。
            """)

    with tab2:
        st.markdown('<h2 class="section-header">故宮南院 — 跨越水岸的墨色虛實</h2>', unsafe_allow_html=True)
        st.write("故宮南院是我最熟悉的地方。每次經過那片廣闊的平原，看著那座橫跨在人工湖上、弧度極大的景觀橋，我總覺得它的線條非常強烈。這座橋的跨度如此之大，中間卻幾乎沒有落墩支撐，它如何承受嘉義夏季強烈的風壓？這種不對稱的設計，在物理層面上該如何克服單側支撐帶來的扭力？")
        st.markdown('<div class="question-text">視覺的輕盈與結構的沈重：這座橋樑如何利用不對稱的鋼構，在單側支撐的情況下維持橫跨水面的穩定？</div>', unsafe_allow_html=True)
        st.write("至美橋採用了不對稱的鋼構箱樑與螺旋狀鋼樑支撐系統。這種設計能將行人震動與側向風力轉化為旋轉應力，傳導至兩側的鋼筋混凝土錨座。主建築外牆大量的不鏽鋼圓盤則隱藏了雙層牆體結構，在展現潑墨美學的同時，也透過氣候調適技術減少內部的熱負荷。")
        st.image("https://via.placeholder.com/1000x500?text=Southern+Palace+Museum+Photo", caption="故宮南院：至美橋鋼構桁架設計")
        with st.expander("參考資料"):
            st.markdown("""
            * 大元建築工場紀錄：至美橋景觀橋設計紀實，解決非對稱受力挑戰。
            * 建築師姚仁喜訪談：南方建築論壇中關於「虛實交構」的設計理念分享。
            """)

# --- 第三類：預留區 ---
else:
    st.info("這裡預留給未來想要討論的酷建築，目前正在資料收集階段...")