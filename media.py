import webbrowser
class Movie():
    """
    This class provides a way to store movie related information.
    VALID_RATINGS - variable to ensure the ratings of each movie (unused).
    The first/ initial function of the program takes in the following:
        movie_title - A string variable holding the title of the movie.
        movie_storyline - Also a string with a brief description of the movie.
        poster_image - url link pointing to poster image of the movie
        trailer_youtube - url linking to the youtube trailer of movie
    The show_trailer function:
        Doesn't take in any variables, but does call on the inital function to grab
        the trailer-youtube variable. Uses the library webbrowser to open the video.
    """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
