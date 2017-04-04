<h1>Fresh Tomatoes Movie Trailers</h1>

<p>Writing a <strong> server side </strong> code to store a list of my favorite movies, including *poster images, storyline, and youtube trailers.* These movies are generated on a <strong> static webpage </strong> allowing the user to browse through them, read and watch the movie trailers.</p>

<h2>Modules</h2>

<ul>
    <li><strong>webbrowser</strong> This module provides a high-level interface which opens the URL in a new browser window <a href="https://docs.python.org/2/library/webbrowser.html">here</a>)</li>
    <pre><code>def run_youtube_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
</code></pre>
   <li><strong>os</strong> This module is used to manipulate and obtain the absolute path of the output file generated  <a href="https://docs.python.org/2/library/os.html">here</a>)</li>
    <pre><code>    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
</code></pre></li>
 <li><strong>re</strong> This module helps to extrat the youtube ID of the movie trailer from the URL<a href="https://docs.python.org/2/library/re.html?highlight=re#module-re"> here</a>)</li>
    <pre><code>    youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
    youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
</code></pre></li>
</ul>

<h2>Movie Details</h2>

<p>Details stored for each movie marked as favorite.</p>

<li>Movie title
<li>Storyline
<li>Poster Image
<li>Youtube trailer</li>


<h2>Steps</h2>

<ul>
    <li><strong>movie_details.py</strong> 
    Define a class which declares the layout structure for each movie. All the movies to be displayed on the webpage share the attributes described by this class. </li>
    <pre><code>def __init__(self,
            movie_title,
            movie_storyline,
            movie_poster_url,
            movie_trailer_url):
            
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url

</code></pre>
   <li><strong>list_of_favorite_movies.py</strong> Declare another class which imports the properties of the movie_details class</li>
    <pre><code>    import movie_details
</code></pre>
</li>
<li><strong>list_of_favorite_movies.py</strong> Declare a movie object, for example, and pass the parameters for the movie in order as accessed by the _init fuction in movie_details. </li>
    <pre><code>    sample_movie = movie_details.Movie(
    "Title",
    "Storyline",
    "Poster Image URL",
    "Youtube trailer URL")
</code></pre>
</li>
 <li><strong>list_of_favorite_movies.py</strong> Repeat the above step for all your favorite movies</li>
    </li>
    <li><strong>fresh_tomatoes.py</strong> This class accepts a list of movies and outputs them as tiles on the webpage. Import this class in list_of_favorite_movies.py  </li>
    <pre><code>    import fresh_tomatoes
</code></pre>
<li><strong>list_of_favorite_movies.py</strong> Declare a list with all the movie objects you want to display on the HTML webpage and call the open_movies_page function in fresh_tomatoes.py </li>
    <pre><code>    movie_list = [
    iron_man,
    iron_man_2,
    iron_man_3,
    avengers_1,
    avengers_2,
    captain_america_1,
    captain_america_2,
    captain_america_3]

fresh_tomatoes.open_movies_page(movie_list)
</code></pre>
</li>
</li>
</ul>

</body>