# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:15:14 2026

@author: saiki
"""

import pandas as pd
df=pd.read_csv("C:/Users/saiki/Downloads/Rotten Tomatoes Movies.csv")
print(df)
df.info()
a=df[['movie_title','genre','rating','directors','studio_name','audience_count','audience_rating',]]
print(a)
print(a.duplicated().sum())
print(a[a.duplicated()])
a1=a.drop_duplicates().copy()
print(a1)
print(a1.duplicated().sum())
a1.info()
print(a1.head())
print(a1.tail())
print(a1.sample(4)[['movie_title','directors']])
print(a1.isna().sum())
print(a1['genre'].isna().value_counts())
a1['genre']=a1['genre'].fillna('unknown')
print(a1['genre'])
print(a1['genre'].isna().sum())
a1['genre']=(a1['genre']
             .str.strip()
             .str.lower()
             .str.replace(r' \s*,\s*', ', ',regex=True)
             .str.replace(r' \s*&\s*', ' & ',regex=True)
             .str.title()
             )
print(a1['genre'])
print(a1.loc[a1['genre']=='Unknown',['movie_title','genre']])
print(a1['genre'].value_counts().to_string())
print((a1['genre']=='Unknown').value_counts())
print(a1['directors'].isna().sum())
a1['directors']=a1['directors'].fillna('unknown')
print(a1['directors'].isna().sum())
print(a1['directors'].str.contains(r'&|,',regex=True,na=False).sum())
print(a1['directors'])
a1['directors']=(a1['directors']
                 .str.strip()
                 .str.lower()
                 .str.title()
                 )
print(a1['directors'])
print(a1.isna().sum())
a1['rating']=a1['rating'].str.upper()
print(a1['rating'])
print(a1['movie_title'])
a1['movie_title']=a1['movie_title'].str.title()
print(a1['movie_title'])
print(a1['studio_name'].value_counts())
a1['studio_name']=a1['studio_name'].fillna('unknown')
a1['studio_name']=a1['studio_name'].str.title()
print(a1['studio_name'].isna().sum())
print(a1.isna().sum())
print((a1['audience_count']<0).sum())
print((a1['audience_count']<0).value_counts())
a1['audience_count']=pd.to_numeric(a1['audience_count'],errors='coerce')
a1['audience_count']=a1['audience_count'].fillna(a1['audience_count'].mean())
print(a1['audience_count'])
print(a1.isna().sum())
print(a1['audience_rating'])
a1['audience_rating']=pd.to_numeric(a1['audience_rating'],errors='coerce')
print((a1['audience_rating']<0)|(a1['audience_rating']>100).sum())
print(a1['audience_rating'].min())
print(a1['audience_rating'].max())
a1['audience_rating']=a1['audience_rating'].fillna(a1['audience_rating'].mean())
a1['rating']=a1['rating'].str.replace('PG-13)','PG-13')
print(a1['rating'])
a1['rating']=a1['rating'].str.replace('R)','R')
print(a1['rating'])

print(a1.isna().sum())
a1.info()
import matplotlib.pyplot as plt
# 1. Top 10 genres by number of movies — Create a bar chart.

genre_count = a1['genre'].value_counts().head(10)

plt.bar(genre_count.index, genre_count.values)

plt.title('Top 10 Genres by Number of Movies')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')

plt.xticks(rotation=45)

plt.show()


# 2. Average audience rating by genre — Create a bar chart.

genre_rating = (
    a1.groupby('genre')['audience_rating']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.bar(genre_rating.index, genre_rating.values)

plt.title('Top 10 Genres by Average Audience Rating')
plt.xlabel('Genre')
plt.ylabel('Average Audience Rating')

plt.xticks(rotation=45)

plt.show()


# 3. Top 10 movies by audience rating — Create a bar chart.

top_movies = (
    a1.groupby('movie_title')['audience_rating']
    .max()
    .sort_values(ascending=False)
    .head(10)
)

plt.bar(top_movies.index, top_movies.values)

plt.title('Top 10 Movies by Audience Rating')
plt.xlabel('Movie')
plt.ylabel('Audience Rating')

plt.xticks(rotation=90)

plt.show()


# 4. Top 10 studios by number of movies — Create a bar chart.

studio_count = a1['studio_name'].value_counts().head(10)

plt.bar(studio_count.index, studio_count.values)

plt.title('Top 10 Studios by Number of Movies')
plt.xlabel('Studio')
plt.ylabel('Number of Movies')

plt.xticks(rotation=45)

plt.show()


# 5. Audience rating distribution — Create a histogram.

plt.hist(a1['audience_rating'], bins=10)

plt.title('Distribution of Audience Ratings')
plt.xlabel('Audience Rating')
plt.ylabel('Number of Movies')

plt.show()


# 6. Audience count vs audience rating — Create a scatter plot.

plt.scatter(
    a1['audience_count'],
    a1['audience_rating']
)

plt.title('Audience Count vs Audience Rating')
plt.xlabel('Audience Count')
plt.ylabel('Audience Rating')

plt.show()
# 7. Average rating by movie rating category — Create a bar chart.

rating_avg = (
    a1.groupby('rating')['audience_rating']
    .mean()
    .sort_values(ascending=False)
)

plt.bar(rating_avg.index, rating_avg.values)

plt.title('Average Audience Rating by Movie Rating')
plt.xlabel('Movie Rating')
plt.ylabel('Average Audience Rating')

plt.show()


# 8. Top 10 directors by number of movies — Create a bar chart.

director_count = (
    a1['directors']
    .value_counts()
    .head(10)
)

plt.bar(director_count.index, director_count.values)

plt.title('Top 10 Directors by Number of Movies')
plt.xlabel('Director')
plt.ylabel('Number of Movies')

plt.xticks(rotation=45)

plt.show()
# 1. Which genres have the highest average audience rating?
print(a1.groupby('genre')['audience_rating'].mean().sort_values(ascending=False).head(10))
# 2. Which genres have the largest audience based on audience_count?
print(a1.groupby('genre')['audience_count'].sum().sort_values(ascending=False).head(10).astype(int))

# 3. Which movie has the highest audience rating?
print(a1.groupby('movie_title')['audience_rating'].max().sort_values(ascending=False).head(1))

# 4. Which movies have the lowest audience rating?
print(a1.groupby('movie_title')['audience_rating'].min().sort_values(ascending=True).head(1))
# 5. Which studio has the highest average audience rating?
print(a1.groupby('studio_name')['audience_rating'].mean().sort_values(ascending=False).head(1))
# ==============================
# ROTTEN TOMATOES DATA ANALYSIS
# 30 BUSINESS QUESTIONS
# ==============================

# BASIC ANALYSIS


# 1. How many movies are in the dataset, and how many unique movies are there?
print(len(a1))
print(a1['movie_title'].nunique())
# 2. How many unique genres, directors, studios, and ratings are there?
print(a1[['genre','directors','studio_name','rating']].nunique())
# 3. What are the most common movie ratings in the dataset?
print(a1['rating'].value_counts().sort_values(ascending=False).head(1))
# 4. Which 10 movies have the highest audience rating?
print(a1.groupby('movie_title')['audience_rating'].max().sort_values(ascending=False).head(10))
# 5. Which 10 movies have the highest audience count?
print(a1.groupby('movie_title')['audience_count'].max().sort_values(ascending=False).head(10))

# FILTERING & CONDITIONS

# 6. Which movies have an audience rating above 90?
print(a1[a1['audience_rating']>90][['movie_title','audience_rating']])

# 7. Which movies have an audience count greater than 1,000,000?
print(a1[a1['audience_count']>1000000][['movie_title','audience_count']])


# 8. Which movies have an audience rating above 80 AND an audience count above 500,000?
print(a1[(a1['audience_rating']>80)& (a1['audience_count']>500000)][['movie_title','audience_rating','audience_count']])

# 9. Which movies have an audience rating below 50?
print(a1[a1['audience_rating']<50][['movie_title','audience_rating']])
print(a1.loc[a1['audience_rating']<50,['movie_title','audience_rating']])
# 10. Which movies have missing/Unknown genre, director, or studio information?
print(a1[(a1['genre']=='Unknown')
|(a1['directors']=='Unknown')
|(a1['studio_name']=='Unknown')]
[['movie_title','genre','directors','studio_name']])

      

# GROUPBY & AGGREGATION

# 11. Which genres have the highest average audience rating?
print(a1.groupby('genre')['audience_rating'].mean().sort_values(ascending=False).head(10))

# 12. Which genres have the highest total audience count?
print(a1.groupby('genre')['audience_count'].sum().sort_values(ascending=False).head(1).astype(int))
# 13. Which genres have the most movies?
print(a1.groupby('genre')['movie_title'].count().sort_values(ascending=False).head(1))
print(a1['genre'].value_counts().head(1))
# 14. Which studios have the highest average audience rating?
print(a1.groupby('studio_name')['audience_rating'].mean().sort_values(ascending=False).head(1))
# 15. Which studios have the highest total audience count?
print(a1.groupby('studio_name')['audience_count'].sum().sort_values(ascending=False).head(1).astype(int))
# 16. Which directors have directed the most movies?
print(a1.groupby('directors')['movie_title'].count().sort_values(ascending=False).head(1))
# 17. Which directors have the highest average audience rating?
print(a1.groupby('directors')['audience_rating'].mean().sort_values(ascending=False).head(1))
# 18. Which directors have the highest total audience count?
print(a1.groupby('directors')['audience_count'].sum().sort_values(ascending=False).head(1))

# GROUPBY + FILTERING + SORTING

# 19. Which studios have produced at least 10 movies and have an average audience rating above 75?
print(
    a1.groupby('studio_name')
      .agg(
          movie_count=('movie_title', 'count'),
          avg_rating=('audience_rating', 'mean')
      )
      .query('movie_count >= 10 and avg_rating > 75')
)

# 20. Which directors have directed at least 5 movies and have an average audience rating above 80?
print(
a1.groupby('directors')
   .agg(
     movie_count=('movie_title','count'),
     avg_rating=('audience_rating','mean')
     )
   .query('movie_count >= 5 and avg_rating > 80')
)

# 21. Which genres have more than 50 movies and an average audience rating above 70?
print(a1.groupby('genre')
  .agg(
       movie_count=('movie_title','count'),
       avg_rating=('audience_rating','mean')
       )
  .query('movie_count>=50 and avg_rating>70')
  )
#22.For each genre, what are the top 3 movies based on audience rating?
print(
    a1.sort_values(['genre', 'audience_rating'], ascending=[True, False])
      .groupby('genre')
      .head(3)
      [['genre', 'movie_title', 'audience_rating']]
)



