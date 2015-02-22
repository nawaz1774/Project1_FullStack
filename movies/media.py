"""This Module define the class Movie.

"""
# Creating Movie class

class Movie():
	"""This class is used to create Movie objects.

	Attributes:
		title: A string type that store the title of the Movie.
		storyline: A one line story line of the movie.
		poster_image_url: URL for the poster image.
		trailer_youtube_url: URL for the movie trailer.

	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""Initilaization method for Movie class

			Args:
				movie_title: A string type that store the title of the Movie.
				movie_storyline: A one line story line of the movie.
				poster_image: URL for the poster image.
				trailer_youtube: URL for the movie trailer.

			Returns:
				Object of type Movie.
		"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.storyline = movie_storyline