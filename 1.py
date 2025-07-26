import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Load Data
# -----------------------------
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies['title'].values

# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movie_indices:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("🎬 Movie Recommender System")
st.subheader("Find movies similar to your favorite!")

selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Show Recommendations"):
    recommendations = recommend(selected_movie)
    st.subheader("Top 5 Recommendations:")
    for movie in recommendations:
        st.write("✅", movie)
