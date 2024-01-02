import streamlit as st
import pickle
import pandas as pd
import requests

# def ferch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/list/{}?api_key=c3c9f0b0bf11b31d537104492454f208&language=en-US'.format(movie_id))
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
#
#     return data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies = []
    # recommend_movies_posters = []
    for i in movies_list:
        movie_id = i[0]
        #fetch poster from API
        recommend_movies.append(movies.iloc[i[0]].title)
        # recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    'Select movie of your choice?',
    movies['title'].values
)
if st.button('Recommend'):
    name = recommend(selected_movie_name)
    for i in name:
        # st.write(i)
        st.text(i)
