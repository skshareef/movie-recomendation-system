import pickle as pk

import pandas as pd
import requests
import streamlit as st


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0024638451cae414926269730ee1a277&language=en-US'.format(movie_id))
    fin_data=response.json()
    return  "https://image.tmdb.org/t/p/w500/"+fin_data['poster_path']

def reco(movie):
    mov_index=movies[movies['title'] == movie ].index[0]
    distances = sim[mov_index]
    mov_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    reco_movies = []
    reco_posters = []
    for i in mov_list:
        movie_id = movies.iloc[i[0]].movie_id
        reco_movies.append(movies.iloc[i[0]].title)
        reco_posters.append(fetch_poster(movie_id))

    return reco_movies,reco_posters


def reco2(movie):
    mov_index=movies[movies['title'] == movie ].index[0]
    distances = sim[mov_index]
    mov_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[5:11]
    reco_movies = []
    reco_posters = []
    for i in mov_list:
        movie_id = movies.iloc[i[0]].movie_id
        reco_movies.append(movies.iloc[i[0]].title)
        reco_posters.append(fetch_poster(movie_id))

    return reco_movies,reco_posters


mov_dict = pk.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(mov_dict)
sim = pk.load(open('sim.pkl', 'rb'))

st.title('SHAREEF MOVIE RECOMMENDER SYSTEM')

movie_selected = option = st.selectbox('Enter the movie name!', movies['title'].values)


if st.button('Recommend the Movies'):
    recommendations,posters = reco(movie_selected)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])




if st.button('Load more movies'):
    recommendations,posters = reco2(movie_selected)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])



