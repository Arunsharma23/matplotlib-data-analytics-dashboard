import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')
print(df)
df = df.dropna(subset = ['type','release_year','rating' , 'country' , 'duration'])
print(df)
type_count = df['type'].value_counts()
print(type_count)
print(plt.figure(figsize=(6 , 4)))
print(plt.bar(type_count.index , type_count.values , color = ['green' , 'blue']))
print(plt.title('count number of movies and Tv shows'))
print(plt.xlabel('Type') , plt.ylabel('Count'))
print(plt.tight_layout())
print(plt.savefig('netflix.png' , dpi = 300))
print(plt.show())

rating_counts = df['rating'].value_counts()
print(plt.figure(figsize=(8 , 6)))
print(plt.pie(rating_counts.values , labels = rating_counts.index , autopct = '%1.1f%%', startangle = 90 ,colors = ['teal' , 'purple']))
print(plt.savefig('rating_show.png' , dpi = 300))
print(plt.title('rating distribution'))
print(plt.tight_layout())
print(plt.show())

movie_df = df[df['type'] == 'Movie']
movie_df['duration_int'] = movie_df['duration'].str.replace('min' , ' ').astype(int)
print(plt.figure(figsize = (8 , 6)))
print(plt.hist(movie_df['duration_int'] , bins = 30 , color = 'purple' , edgecolor  = 'black'))
print(plt.title('movie duration') , plt.xlabel('duration') , plt.ylabel('count'))
print(plt.tight_layout())
print(plt.savefig('movie_duration.png' , dpi = 300))
print(plt.show())

release_counts = df['release_year'].value_counts().sort_index()
print(plt.figure(figsize=(10 , 6)))
print(plt.scatter(release_counts.index , release_counts.values , color = 'green' , marker = 'o'))
print(plt.title('release year') , plt.xlabel('year') , plt.ylabel('count'))
print(plt.tight_layout())
print(plt.savefig('release_histogram.png' , dpi = 300))
print(plt.show())

country_count = df['country'].value_counts().head(10)
print(plt.figure(figsize=(10,6)))
print(plt.bar(country_count.index , country_count.values , color = 'goldenrod' , edgecolor = 'black'))
print(plt.title('top 10 countries') , plt.xlabel('year') , plt.ylabel('country'))
print(plt.tight_layout())
print(plt.savefig('top 10 countries.png' , dpi = 300))
print(plt.show())

content_years = df.groupby(['release_year' , 'type']).size().unstack().fillna(0)
fig, ax =  plt.subplots(1,2 , figsize=(12 , 5))
#FIRST MOVIE
ax[0].plot(content_years.index , content_years['Movie'] , color = 'green')
ax[0].set_title('movie release')
ax[0].set_xlabel('year') , ax[0].set_ylabel('count')
#FIRST SHOW
ax[1].plot(content_years.index , content_years['TV Show'] , color = 'green')
ax[1].set_title('TV Show release')
ax[1].set_xlabel('year') , ax[1].set_ylabel('count')

print(plt.suptitle('content release') , plt.tight_layout())
print(plt.savefig('content_release.png' , dpi = 300))
print(plt.show())

df['listed_in'].value_counts().head(10).plot(kind = 'barh' , color = 'teal')
print(plt.title('Top 10 popular Genres') , plt.xlabel('number of title') , plt.ylabel('Genres') )
print(plt.tight_layout())
print(plt.savefig('top 10 gen' , dpi = 300))
print(plt.show())

df['director'].value_counts().head(10).plot(kind = 'bar' , color = 'brown')
print(plt.title('Top 10 Directors') , plt.xlabel('number of Director') , plt.ylabel('Titles') )
print(plt.tight_layout())
print(plt.savefig('top Directors.png', dpi = 300))
print(plt.show())
