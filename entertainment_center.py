import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys taht come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)
#avatar.show_trailer()

mulan = media.Movie("Mulan",
                        "Mulan disguises herself as a male soldier to take her father's place in the army",
                        "http://www.gstatic.com/tv/thumb/movieposters/21118/p21118_p_v8_aa.jpg",
                        "https://www.youtube.com/watch?v=MsAniqGowKE")
#mulan.show_trailer()


ratatouille = media.Movie("Ratatouille ",
                             "A rat is a chef in Paris",
                             "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                             "https://www.youtube.com/watch?v=c3sBBRxDAqk")

aristocats = media.Movie("The Aristocats",
                             "In the heart of Paris, a kind and eccentric millionairess wills her entire estate to Duchess, her high-society cat, and her three little kittens",
                             "http://www.gstatic.com/tv/thumb/movieposters/19375/p19375_p_v8_af.jpg",
                             "https://www.youtube.com/watch?v=wjA5LWNUPDY")

brave = media.Movie("Brave",
                             "Princess Merida seeks to control her own destiny in Disney and Pixar's Brave.",
                             "http://t0.gstatic.com/images?q=tbn:ANd9GcSuKUcpKMfuY1En5kWsJB2Xe-dqu-yYrQM6KTps3-Mti04lgmSY",
                             "https://www.youtube.com/watch?v=TEHWDA_6e3M")

movies = [toy_story, avatar, mulan, ratatouille, aristocats, brave]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
