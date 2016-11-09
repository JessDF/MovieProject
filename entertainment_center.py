import media
import fresh_tomatoes   #links up the fresh_tomatoes and media pages

#toy_story is an instance of the class, "Movie"
toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys taht come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")  

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",# noqa
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8")

mulan = media.Movie("Mulan",
                        "Mulan disguises herself as a man to take her father's place in the army",
                        "http://www.gstatic.com/tv/thumb/movieposters/21118/p21118_p_v8_aa.jpg", # noqa
                        "https://www.youtube.com/watch?v=MsAniqGowKE")

ratatouille = media.Movie("Ratatouille ",
                             "A rat is a chef in Paris",
                             "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", # noqa
                             "https://www.youtube.com/watch?v=c3sBBRxDAqk")

aristocats = media.Movie("The Aristocats",
                             "In the heart of Paris, a millionairess wills her entire estate to her cats",
                             "http://www.gstatic.com/tv/thumb/movieposters/19375/p19375_p_v8_af.jpg", # noqa
                             "https://www.youtube.com/watch?v=wjA5LWNUPDY")

brave = media.Movie("Brave",
                             "Princess Merida seeks to control her own destiny in Disney and Pixar's Brave.",
                             "http://t0.gstatic.com/images?q=tbn:ANd9GcSuKUcpKMfuY1En5kWsJB2Xe-dqu-yYrQM6KTps3-Mti04lgmSY", # noqa
                             "https://www.youtube.com/watch?v=TEHWDA_6e3M")
#Below: creates an array of the "Movie" class instances
movies = [toy_story, avatar, mulan, ratatouille, aristocats, brave] 
#Below: takes the array movies and addes them to webpage
fresh_tomatoes.open_movies_page(movies)   
print(media.Movie.__doc__)  #prints documentation of the class Movie
print(media.Movie.__name__) #prints class name
print(media.Movie.__module__)   #prints the module we imported/ name of file
