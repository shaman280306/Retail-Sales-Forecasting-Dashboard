import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Retail Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("clean_superstore.csv")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

df = load_data()

st.sidebar.title("📋 Navigation")

page = st.sidebar.selectbox(
    "Choose Section",
    [
        "Dashboard",
        "Category Analysis",
        "Region Analysis",
        "Monthly Sales Trend"
    ]
)

if page=="Dashboard":

    st.title("📈 Retail Sales Forecasting Dashboard")

    st.markdown("### Business Overview")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("💰 Total Sales",f"${df['Sales'].sum():,.0f}")
    c2.metric("📦 Orders",len(df))
    c3.metric("🗂 Categories",df["Category"].nunique())
    c4.metric("🌎 Regions",df["Region"].nunique())

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

elif page=="Category Analysis":

    st.title("📦 Category Sales")

    sales=df.groupby("Category")["Sales"].sum()

    fig,ax=plt.subplots(figsize=(8,5))

    ax.bar(sales.index,sales.values)

    ax.set_ylabel("Sales")

    st.pyplot(fig)

    st.subheader("Sales Share")

    fig2,ax2=plt.subplots(figsize=(6,6))

    ax2.pie(
        sales.values,
        labels=sales.index,
        autopct="%1.1f%%"
    )

    st.pyplot(fig2)

elif page=="Region Analysis":

    st.title("🌍 Region Sales")

    region=df.groupby("Region")["Sales"].sum()

    fig,ax=plt.subplots(figsize=(8,5))

    ax.bar(region.index,region.values)

    ax.set_ylabel("Sales")

    st.pyplot(fig)

elif page=="Monthly Sales Trend":

    st.title("📈 Monthly Sales Trend")

    monthly=(
        df
        .groupby(
            pd.Grouper(
                key="Order Date",
                freq="ME"
            )
        )["Sales"]
        .sum()
    )

    fig,ax=plt.subplots(figsize=(12,5))

    ax.plot(
        monthly.index,
        monthly.values,
        linewidth=3
    )

    ax.set_ylabel("Sales")

    ax.grid(alpha=.3)

    st.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.success("Developed by Shaman Sharma")