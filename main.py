import pandas as pd

movies = pd.read_csv("./movies.csv")
ratings = pd.read_csv("./ratings.csv")

print(movies)

print(ratings)

print(ratings['rating'].unique())

print(ratings['rating'].mean())
print(ratings['rating'].max())
print(ratings['rating'].min())
print(ratings['rating'].describe())

print("Sobre Toy Story")
toyStory = ratings.query("movieId==1")
print(toyStory)
print(toyStory.describe())

print("Sobre o usuário 1")
user1 = ratings.query("userId==1")
print(user1)
print(user1.describe())


print(movies[movies['genres'].str.contains('Comedy')])
print(movies[movies['title'].str.contains('\\(2017\\)')])

import matplotlib.pyplot as plt

plt.hist(toyStory['rating'], bins=20)
plt.show()

print(toyStory['rating'].value_counts())
plt.pie(toyStory['rating'].value_counts(), labels=[4.0, 5.0, 3.0, 3.5, 4.5, 2.5, 2.0, 1.5, 0.5], autopct="%1.1f%%")
plt.show()

plt.boxplot(toyStory['rating'])
plt.show()