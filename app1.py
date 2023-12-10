


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import networkx as nx
import plotly.graph_objs as go
st.title('''
Anime
''')
st.write('''
### There is our data set 
''')
df = pd.read_csv("anime.csv")
st.dataframe(df)

df_cleaned = df.dropna()






filtered_df = df[df.episodes != "Unknown"]


filtered_df['episodes'] = pd.to_numeric(filtered_df['episodes'], errors='coerce')


fig = px.scatter(filtered_df, x="rating", y="members",
                 size="episodes", color="type",
                 hover_name="name", size_max=60,
                 color_discrete_sequence=px.colors.qualitative.Safe,
                 title="The connection between members, rating, and episodes")
st.title('''
Overall view
''')
st.plotly_chart(fig)
st.write("The size reflects the number of episodes")

st.balloons()
st.snow()










st.sidebar.header('Selection')
selected_bonus = st.sidebar.selectbox("Choose:", ["Episodes and members", "Genres"])



st.title(selected_bonus)

if selected_bonus == "Episodes and members":
    a = px.scatter(df, x=df.episodes, y=df.members, title="Dependence of episodes on number of members")
    st.plotly_chart(a)
elif selected_bonus == "Genres":
    st.write("Choose top-n animes to see distribution of genres")
    n = st.selectbox("Choose:", ["10","20","30","50","100","200","1000","5000","12000"])
    n = int(n)
    top_30_anime = df.nlargest(n, 'rating')
    genre_counts = top_30_anime['genre'].str.split(', ').explode().value_counts()
    fig = px.pie(values=genre_counts.values, names=genre_counts.index, title='Distribution of Genres in Top 30 Anime')
    st.plotly_chart(fig)






