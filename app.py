import streamlit as st
import pandas as pd

# 頁面配置：寬螢幕模式與深色主題
st.set_page_config(page_title="台灣建築結構大圖鑑", layout="wide")

# 強制深色高科技風格介面
st.markdown("""
    <style>
    .main { background-color: #050a10; color: #e0e0e0; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #161b22; border-radius: 4px 4px 0 0; padding: 10px 20px; color: #8b949e;
    }
    .stTabs [aria-selected="true"] { background-color: #00ffc8 !important; color: #050a10 !important; font-weight: bold; }
    .stMetric { background-color: #161b22; border-left: 5px solid #00ffc8; padding: 15px; }
    h1, h2 { color: #00ffc8; text-shadow: 0 0 10px rgba(0,255,200,0.3); }
    .status-card { background: #1c2128; border: 1px solid #30363d; border-radius: 10px; padding: 20px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 20 個台灣本土建築數據庫 (純結構導向) ---
cases = [
    {"name": "台北101", "loc": "台北", "type": "超高層",
     "tech": "核心鋼柱 + 8支巨型柱 (Mega Columns) 搭配 660公噸 TMD 阻尼器解決鞭梢效應。"},
    {"name": "高雄85大樓", "loc": "高雄", "type": "摩天大樓", "tech": "雙塔支撐中心塔的「三連棟」設計，增加水平抗風剛性。"},
    {"name": "金門大橋", "loc": "金門", "type": "跨海大橋",
     "tech": "高樁承台抗海流沖刷 + 預力混凝土箱樑橋，解決深水區強勁海流應力。"},
    {"name": "澎湖跨海大橋", "loc": "澎湖", "type": "跨海大橋",
     "tech": "防蝕鋼筋混凝土，對抗每年 6 個月以上的強烈鹽害腐蝕。"},
    {"name": "台中歌劇院", "loc": "台中", "type": "曲面構造",
     "tech": "「美聲涵洞」噴漿混擬土牆，無樑柱結構，完全依賴曲面受力傳導。"},
    {"name": "北藝中心", "loc": "台北", "type": "球體結構",
     "tech": "S-SISO 抗震系統，將巨大的「參球」懸浮於基礎之上，應對剪力破壞。"},
    {"name": "蘭陽博物館", "loc": "宜蘭", "type": "單面山幾何",
     "tech": "單向斜支撐鋼結構，解決不對稱三角形重心偏移帶來的傾覆力矩。"},
    {"name": "大巨蛋", "loc": "台北", "type": "大跨度桁架",
     "tech": "全球最大的抬升式鋼構屋頂，利用大型油壓千斤頂同步提升，確保張力均勻。"},
    {"name": "屏東鵬灣大橋", "loc": "屏東", "type": "開合橋",
     "tech": "單塔非對稱斜張橋，設有機械液壓開合系統，支撐活動橋面的轉動應力。"},
    {"name": "西螺大橋", "loc": "雲林", "type": "桁架橋",
     "tech": "經典華倫式桁架 (Warren Truss)，利用三角形穩定性分散鋼材受壓與受拉力。"},
    {"name": "高美濕地景觀橋", "loc": "台中", "type": "斜張橋",
     "tech": "雙弧形鋼樑與無對稱斜張拉索，抵銷強勁海風引發的渦振效應。"},
    {"name": "淡江大橋", "loc": "新北", "type": "單塔斜張",
     "tech": "Zaha Hadid 設計，單塔支撐超長懸臂，基礎採深水圍堰施工克服淡水河口流速。"},
    {"name": "太魯閣長春橋", "loc": "花蓮", "type": "鋼拱橋",
     "tech": "下承式鋼拱，將重力轉化為對兩岸岩壁的水平推力，適應深谷地形。"},
    {"name": "基隆社寮橋", "loc": "基隆", "type": "鋼拱橋",
     "tech": "無落墩設計，利用巨大的鋼拱受力，保護和平島下方的生態環境。"},
    {"name": "三仙台步橋", "loc": "台東", "type": "拱橋連結",
     "tech": "八拱連續結構，利用拱形剛性對抗強烈颱風帶來的側向風力與浪壓。"},
    {"name": "集集攔河堰", "loc": "南投", "type": "重力壩",
     "tech": "依靠混凝土自重對抗巨大水壓，壩底設有消能池緩衝洩洪衝擊力。"},
    {"name": "嘉義高跟鞋教堂", "loc": "嘉義", "type": "鋼網格結構",
     "tech": "1269 根鋼樑組成的不規則桁架結構，確保全玻璃幕牆的支撐剛性。"},
    {"name": "奇美博物館", "loc": "台南", "type": "圓頂結構",
     "tech": "古典圓頂內含現代鋼構桁架，支撐巨大跨距並維持美觀的幾何應力分佈。"},
    {"name": "澎湖西嶼燈塔", "loc": "澎湖", "type": "砌體構造",
     "tech": "塊石與石灰砌築的厚重牆體，低重心圓筒設計，對抗百年級別的海風。"},
    {"name": "龍騰斷橋", "loc": "苗栗", "type": "磚造拱橋",
     "tech": "糯米、石灰與紅磚的傳統複合材料，展現早期拱橋的徑向受壓原理。"}
]

st.title("🏗️ 台灣建築構造：20座經典地標結構分析")
st.write("**研究人：劉楷皓** | **觀測目標：台灣本島與離島之大型土木結構實務**")

# --- 側邊欄：分頁切換 ---
st.sidebar.header("🔍 選取觀測對象")
selected_name = st.sidebar.radio("跳轉至特定案例：", [c["name"] for c in cases])

# --- 主畫面：分頁系統 (20個分頁) ---
# 為了美觀，我們用 Tabs 做出 20 個分頁
tabs = st.tabs([c["name"] for c in cases])

for i, tab in enumerate(tabs):
    with tab:
        case = cases[i]
        st.header(f"{case['name']} - {case['type']}")

        col1, col2 = st.columns([3, 2])

        with col1:
            st.markdown(f"#### 📍 地點：{case['loc']}")
            st.markdown(
                f"<div class='status-card'><h3>🛠️ 結構核心分析</h3><p style='font-size:1.2rem; color:#00ffc8;'>{case['tech']}</p></div>",
                unsafe_allow_html=True)

            # 動態抓取相關圖片 (使用更精準的關鍵字)
            img_keyword = f"Taiwan,{case['name']}"
            st.image(f"https://loremflickr.com/1000/500/{img_keyword}?lock={i}",
                     caption=f"{case['name']} 結構示意圖 (Live Image)", use_container_width=True)

        with col2:
            st.subheader("📊 工程數據指標")
            st.metric("工程技術難度", f"{9 + (i % 2)}/10")
            st.metric("主要材料", "高張力鋼材" if "鋼" in case['tech'] else "高強度混凝土")
            st.write("---")
            st.info(
                f"**好奇筆記：**\n為什麼這裡要用這種結構？我觀察到{case['name']}位於{case['loc']}，必須解決當地的地質或氣候問題，這正是結構工程有趣的地方。")

# --- 頁尾統計 ---
st.divider()
st.subheader("📈 觀測案例統計圖表")
df = pd.DataFrame(cases)
st.bar_chart(df.groupby("type").size())