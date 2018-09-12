import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of aboy and his toys that come to life",
"https://vignette.wikia.nocookie.net/pixar/images/c/ca/Toy_story_ver1_xlg.jpg/revision/latest?cb=20110515142143",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print (toy_story.storyline)


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/ar/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=2YxZDmB5ubA")
print (avatar.storyline)
avatar.show_trailer()


school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "http://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouilla = media.Movie("Ratatouille",
                          "Storyline",
                          "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline",
                                "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games",
                           "Storyline",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, school_of_rock, ratatouilla, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
