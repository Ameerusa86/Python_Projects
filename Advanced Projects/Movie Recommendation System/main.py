import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from fuzzywuzzy import process
import streamlit as st

# Load the dataset into a Pandas DataFrame
data = pd.read_csv("top10K-TMDB-movies.csv")

# Preprocess the data
data["genre"] = data["genre"].fillna("")  # Fill missing values with empty string
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(data["genre"])


# Build the recommendation system
def recommend_movies(movie_title, tfidf_matrix, data, top_n=10):
    # Perform fuzzy matching to find similar movie titles
    matches = process.extractBests(
        movie_title, data["title"], score_cutoff=70, limit=top_n
    )
    matched_titles = [match[0] for match in matches]

    # Get matched movie titles and release years
    matched_movies = data[data["title"].isin(matched_titles)][["title", "release_date"]]

    return matched_movies


# Streamlit App
def main():
    st.title("Movie Recommendation System")

    # Input movie title
    movie_title = st.text_input("Enter a movie title:", "")

    # Recommend movies similar to the input movie title
    if st.button("Recommend"):
        if movie_title.strip() != "":
            recommended_movies = recommend_movies(movie_title, tfidf_matrix, data)
            if not recommended_movies.empty:
                st.write("Recommended Movies:")
                for index, row in recommended_movies.iterrows():
                    st.write(f"{row['title']} ({row['release_date'].split('-')[0]})")
            else:
                st.warning("No recommendations found for the provided movie title.")
        else:
            st.error("Please enter a movie title.")


if __name__ == "__main__":
    main()
