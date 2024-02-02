# Moviesmine

# Movie Recommendation using ML
## Overview
This project employs both **Content-Based Filtering** and **Collaborative-Based Filtering** techniques to create a Movie Recommendation System. The system gathers movie information from the TMDb website, undergoes data cleaning, and employs machine learning algorithms to deliver personalized movie suggestions.

## Demo
https://github.com/JayeshJain246/movie-mine/assets/77563599/38bdbc93-c02b-419b-a203-50f6677d2780

## Data Sets
- [TMDB dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata): The dataset consist of 3 files:
  - tmdb_5000_credits.csv (contains information about the cast and crew of the movie)
  - tmdb_5000_movies.csv (contains information about the movie such as genres, overview etc.)
  - ratings.csv (contains user and movie ratings)

## Content Based Filtering
The section labeled "Based on what you like" showcases movie recommendations derived from Content Filtering. Content-Based Filtering suggests items by considering the inherent characteristics and features of those items. It depends on analyzing the content or attributes of the items, taking into account both the properties of the items and the user's preferences.

![ContentBased](https://github.com/JayeshJain246/movie-mine/assets/77563599/750e7fbe-3f2d-4b49-a3f0-912b99923688
)
<br> The following approach was used - 
- Cleaning the data by retaining only relevant information.
- Creating tags for each movie based on genres, overview, keywords, top 3 cast, and director.
- Calculating the distance among vectors using cosine similarity.


## Colaborative Based Filtering
Collaborative Filtering suggests items by analyzing user behavior and preferences, taking into account the actions and choices of other users who share similarities with the target user. The section labeled "You may also like" presents movie recommendations using Collaborative Filtering.
![collaborative](https://github.com/JayeshJain246/movie-mine/assets/77563599/162383ff-9150-4b38-b4f8-1c7825ff60b4
)

## Popular Movies based on user voting
![popular](https://github.com/JayeshJain246/movie-mine/assets/77563599/de5ab532-7241-4e33-bf97-2ca7e2cafe5c
)


