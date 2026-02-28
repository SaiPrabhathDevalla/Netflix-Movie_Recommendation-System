import streamlit as st
import pandas as pd
import pickle
import base64


# ---------- PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND) ----------
st.set_page_config(
    page_title="Netflix Recommender",
    layout="wide"
)


# ---------- FUNCTION TO ADD BACKGROUND IMAGE ----------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{data}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* Make text white */
        h1, h2, h3, h4, h5, h6, p, label {{
            color: white !important;
        }}

        /* Style selectbox */
        .stSelectbox > div > div {{
            background-color: rgba(0,0,0,0.6);
            color: white;
        }}

        /* Style button */
        .stButton>button {{
            background-color: #E50914;
            color: white;
            border-radius: 8px;
            padding: 8px 16px;
            font-weight: bold;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


# ---------- LOAD DATA ----------
with open('movies similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

df = pd.read_csv('tmdbdf.csv')
df = df.iloc[:len(similarity)]


# ---------- ADD BACKGROUND ----------
add_bg_from_local("image.png")   


# ---------- CENTER NETFLIX LOGO ----------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/7/7a/Logonetflix.png",
        width=800   
    )

# ---------- CENTER TITLE ----------
st.markdown("""
<h1 style='text-align: center; 
           font-size: 60px; 
           color: white;'>
🎬 Netflix Movie Recommendation System
</h1>
""", unsafe_allow_html=True)


# ---------- MOVIE SELECT ----------
movie_name = st.selectbox('Select the Movie', df['title'].values)


# ---------- RECOMMEND FUNCTION ----------
def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distance)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommend_movie = []
    recommend_poster = []

    for tag in movie_list:
        recommend_movie.append(df.iloc[tag[0]].title)
        poster = df.iloc[tag[0]]['poster_path']

        if pd.notnull(poster):
            recommend_poster.append(
                'https://image.tmdb.org/t/p/w500/' + poster
            )
        else:
            recommend_poster.append(
                'https://via.placeholder.com/500x750?text=No+Poster'
            )

    return recommend_poster, recommend_movie


# ---------- BUTTON ----------
if st.button('Click here for getting similar movies'):
    posters, names = recommend(movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx], width=350) 
            st.markdown(
                f"<h5 style='text-align:center; color:white;'>{names[idx]}</h5>",
                unsafe_allow_html=True
            )