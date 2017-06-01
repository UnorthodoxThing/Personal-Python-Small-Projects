
import webbrowser

# Uses class method to organise movie contents.
#INPUT (1)title, (2)description, (3)poster image url, (4)youtube trailer, (5)running time/duration (6)number of season, (7)number of episode, (8)tv station
#all arguments uses string elements.
class Movie():
    """This class provides a way to store movie and tv shows related information"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, duration_time='', number_of_seasons='', tv_station=''):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        self.duration = duration_time
        self.seasons = number_of_seasons
        self.station = tv_station

    def show_trailer(self):
        """Opens Trailer in webbrowser"""
        webbrowser.open(self.trailer_youtube_url)
