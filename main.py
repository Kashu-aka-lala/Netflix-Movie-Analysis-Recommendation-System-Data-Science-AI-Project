import streamlit as st
import pandas as pd
import random

# Load the dataset
df = pd.read_csv("Netflix_data.csv")

# Clean relevant columns
filter_columns = ['Category', 'Country', 'Rating', 'Type']
for col in filter_columns:
    df[col] = df[col].fillna('').astype(str).str.strip()

# Sidebar filters
st.sidebar.header("🎬 Netflix Recommendation System")
st.sidebar.subheader("📌 Filter below to get personalized Netflix recommendations:")

genre = st.sidebar.selectbox("Select Genre (Category):", sorted(df['Category'].unique()))
country = st.sidebar.selectbox("Select Country:", sorted(df['Country'].unique()))
rating = st.sidebar.selectbox("Select Maturity Rating:", sorted(df['Rating'].unique()))
content_type = st.sidebar.selectbox("Select Type:", sorted(df['Type'].unique()))

# Filter dataset based on user input
filtered_df = df[
    (df['Category'] == genre) &
    (df['Country'] == country) &
    (df['Rating'] == rating) &
    (df['Type'] == content_type)
]

st.title("🎞️ Your Netflix Recommendation")

if not filtered_df.empty:
    # Pick a random movie/show from filtered results
    selected = filtered_df.sample(1).iloc[0]

    st.markdown(f"### 🎥 {selected['Title']}")
    st.write(f"**Category:** {selected['Category']}")
    st.write(f"**Type:** {selected['Type']}")
    st.write(f"**Rating:** {selected['Rating']}")
    st.write(f"**Director:** {selected['Director']}")
    st.write(f"**Cast:** {selected['Cast']}")
    st.write(f"**Country:** {selected['Country']}")
    st.write(f"**Release Date:** {selected['Release_Date']}")
    st.write(f"**Duration:** {selected['Duration']}")
    st.write(f"**Description:** {selected['Description']}")
else:
    st.warning("❌ No matches found for the selected filters. Try different options.")
