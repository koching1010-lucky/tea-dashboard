
import streamlit as st

# 網頁標題
st.set_page_config(
    page_title="茶極限戰情儀表板",
    page_icon="🥤",
    layout="wide"
)

# 主畫面標題
st.title("🥤 茶極限戰情儀表板")

# 側邊欄
st.sidebar.title("控制面板")

# 側邊欄選單
city = st.sidebar.selectbox(
    "選擇地區",
    ["台北", "台中", "高雄"]
)

# 主畫面內容
st.subheader("今日營運概況")

st.write(f"目前查看地區：{city}")

# 三個指標
col1, col2, col3 = st.columns(3)

col1.metric("今日營收", "NT$ 120,000", "+12%")
col2.metric("來客數", "856", "+5%")
col3.metric("飲料銷量", "1,245 杯", "+18%")

# 長條圖資料
sales_data = {
    "飲料": ["紅茶", "綠茶", "奶茶", "珍奶"],
    "銷量": [150, 120, 300, 500]
}

st.bar_chart(
    data=sales_data,
    x="飲料",
    y="銷量"
)
