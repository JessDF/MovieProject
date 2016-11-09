# MovieProject
Udacity Full Stack Developer Course - Project 1: Create a Movie Trailer Website

Steps I took:
1.Created media.py --> Created a class called "Movie", defined the __init__ function, holds: movie title, movie storyline, poster imagek, trailer youtube.
2. Created entertainment_center.py --> In this file I have 6 instances of the Movie class.
        I also imported the media file, form step 1.   
3. In Media.py --> Defined the show_trailer function, that takes in the youtube url and uses the webbrowser library to play it. Had to import webbrowser.  Also created a one line documentation between the 3 quotation marks """   """ and the ratings.
4. Dowloaded fresh_tomatoes.py and imported it to entertainment_center.py
5. In entertainment_center.py --> created an array "movies" that held the 6 different instances.
6. In enteratainment_center.py --> used the function "open_movies_page" from the fresh_tomatoes class and passed in the "movies" array.

How to run the program:
1. Unzip the movies.zip folder     //Different instructions if doing so on GitHub
2. Once it is unzipped, open the internal folder (also called movies)
3. Right click entertainment_center.py and choose - Edit with IDLE
4. Clic "run", then click "Run Module"


Note:
- For this program you will need python 2.7
- To install python 2.7 go to this website: https://www.python.org/downloads/
