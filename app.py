import streamlit as st
import pickle
import pandas as pd
import streamlit as st
import requests


#________________________________functions _____________________________________
def recommend(movie):

    index = movie_list[title_list == movie].index[0]
    listsorted = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_list=[]
    recommended_movies_posters=[]


    for i in listsorted[1:6]:
        movie_id=movie_list.iloc[i[0]].id
        recommended_list.append(movie_list.iloc[i[0]].original_title)  # find movie name with indexes
        # fetch poster form api tmdb
        recommended_movies_posters.append( fetch_poster(movie_id) )
    return recommended_list,recommended_movies_posters


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7d4d62438787d2513baee2928efce110'.format(movie_id))
    data=response.json()

    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


#________________________________functions-end _____________________________________

movie_list=pickle.load(open('movie_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
#________________________________two databases _____________________________________


title_list=movie_list['original_title'].values   # names of movies  for selection
st.title('MOVIE RECOMMENDER SYSTEM')


selected_movie_name= st.selectbox(
    'Enter the name of the movie you would like to get similar recommendation on ',
    (title_list))

if st.button('Recommend'):     # button reccomend
    st.write('You selected:', selected_movie_name)         # actions when recommend is pressed. 1)display name
    st.write('5 movies similar to ',selected_movie_name, 'are:-')

    names,posters=recommend(selected_movie_name)    #   display 5 similar movies with posters



    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


