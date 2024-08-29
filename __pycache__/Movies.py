import pandas as pd
movie = pd.read_csv('movie_dataset.csv')
movie = movie.drop('index', axis=1)
print('Welcome to Movie library!')
print('How do you want to find your movie/movies? TYPE: "genre" or "year" ')
how = input()
if how ==  "genre":
    print('What kind of genre/genres of movies would you like to watch? Ex. Avengers')
    user = input()
    user = user[0].upper()+user[1:]
    print(user + ' movies')
    genre = movie[movie['genres'] == user]
    genre = genre[['title']]
    if genre == []:
        print('Please type a real genre')
    else:
        print(genre.head(10))
elif how == 'year':
    print('When was the movie released? Ex. 2009-12-10')
    year = int(input())
    year = movie[movie['release_date'] == year]
    year = year[['title']]
    print(year)

