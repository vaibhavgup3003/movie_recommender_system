import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7020d23cba80bd9f908198870ba599a2&&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies_details[movies == movie].index[0]
    distances = similarity[movie_index]    # is the distance array of movies from movie at this index
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # this is the ans list

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies_details.iloc[i[0]].movie_id
        # fetch poster from api
        recommended_movies.append(movies_details.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


# this is fetching the data frame movies.pkl in read binary(rb) mode
movies_details = pickle.load(open('movies.pkl', 'rb'))
movies = movies_details['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommender System')  # this is the title of the project


selected_movie_name = st.selectbox('Enter the movie for which you want the recommendations', movies)


# if st.button('Recommend'):
#     recommendations = recommend(selected_movie_name)
#     for i in recommendations:
#         st.write(i)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

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

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()