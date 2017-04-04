import webbrowser


# import webbrowser class to be able to open youtube urls
class Movie():
    # Initializing Movie class variables
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_poster_url,
                 movie_trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url

    # Play movie trailers
    def run_youtube_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
