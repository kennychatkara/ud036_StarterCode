import fresh_tomatoes
import media


# Create Movie object instances
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

doctor_strange = media.Movie("Doctor Strange",
                             "A doctor turns to teachings of mystical sorcery to heal his injured hands when western medicine fails him",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=Lt-U_t2pUHI")

dark_knight = media.Movie("The Dark Knight",
                          "Storyline",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=kmJLuwP3MbY")

deadpool = media.Movie("Deadpool",
                       "Storyline",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=9vN6DHB6bJc")

xmen_first_class = media.Movie("X-Men: First Class",
                               "Storyline",
                               "https://upload.wikimedia.org/wikipedia/en/5/55/X-MenFirstClassMoviePoster.jpg",
                               "https://www.youtube.com/watch?v=UrbHykKUfTM")

# Add Movie objects to list
movies = [toy_story, avatar, doctor_strange, dark_knight, deadpool, xmen_first_class]

# Generate and open movies web page using list of created Movie objects
fresh_tomatoes.open_movies_page(movies)
