# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#task 1
def is_above_5_5(movie):
    return movie.get('imdb', 0) > 5.5


print(is_above_5_5(movies[0]))  

#task 2

def get_movies_above_5_5(movies):
    return [movie for movie in movies if movie.get('imdb', 0) > 5.5]


above_5_5_movies = get_movies_above_5_5(movies)
print(above_5_5_movies)

#task 3

def get_movies_by_category(movies, category):
    return [movie for movie in movies if movie.get('category') == category]

category_name = input("Enter the category name: ")
category_movies = get_movies_by_category(movies, category_name)
print(category_movies)

#task 4

def compute_average_imdb_score(movies):
    total_imdb_score = sum(movie.get('imdb', 0) for movie in movies)
    num_movies = len(movies)
    if num_movies == 0:
        return 0
    return total_imdb_score / num_movies

average_score = compute_average_imdb_score(movies)
print("Average IMDB score:", average_score)

#task 5

def compute_average_imdb_score_by_category(movies, category):
    category_movies = [movie for movie in movies if movie.get('category') == category]
    total_imdb_score = sum(movie.get('imdb', 0) for movie in category_movies)
    num_movies = len(category_movies)
    if num_movies == 0:
        return 0
    return total_imdb_score / num_movies

category_name = input("Enter the category name: ")
average_score = compute_average_imdb_score_by_category(movies, category_name)
print("Average IMDB score for", category_name, "movies:", average_score)


