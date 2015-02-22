""" Generates a HTML page by taking in a list of Movies, makes use fresh_tomatoes module.

In this Module a list of Movie objects are created. Movie object is available in media module.
Also it makes use of fresh_tomatoes module that conatins the functuion open_movies_page that will consume the list of Movies and generate HTML file and additinally it launches the web browser and renders the HTML generated.

"""

# Inclding media Module that conatains definition for Movie class
# Inclding fresh_tomatoes Module which has open_movies_page function which creates the HTML file

import media
import fresh_tomatoes

# Creating movie objects

toy_story = media.Movie("Toy Story", "Story of Toys That Come To Life", 
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")


inception = media.Movie("Inception", "Story About Team of people who get into your dreams and steal your Ideas", 
						"http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
						"https://www.youtube.com/watch?v=66TuSJo4dZM")

babys_day_out = media.Movie("Baby's Day Out", "Story about a baby who gets kidnapped but resues himself", 
						"http://upload.wikimedia.org/wikipedia/en/3/35/Babys_day_out_poster.jpg",
						"https://www.youtube.com/watch?v=TGVwTYrkYSY")

despicable_me = media.Movie("Despicable Me", "Story of a Super Villan his minions and his 3 adopted daughters", 
						"http://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
						"https://www.youtube.com/watch?v=sUkZFetWYY0")

pk = media.Movie("pk", "Story of an Alien who lands on earth trying to understand man made religions", 
						"http://upload.wikimedia.org/wikipedia/en/2/2d/PK_Theatrical_Poster.jpg",
						"https://www.youtube.com/watch?v=82ZEDGPCkT8")

lrmb = media.Movie("Lage raho munna bhai", "Story of a Goon who becomes delusional starts seeing Gandhi ", 
						"http://upload.wikimedia.org/wikipedia/en/3/35/Lage_raho_munna_bhai.JPG",
						"https://www.youtube.com/watch?v=OE6f1oHgeDg")

# Making a list of movies
movies = [toy_story, inception, babys_day_out, despicable_me, pk, lrmb]

# Calling open_movies_page function which creates HTML page
fresh_tomatoes.open_movies_page(movies)