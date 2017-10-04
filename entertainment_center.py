import fresh_tomatoes
import media


# Create Movie object instances
toy_story = media.Movie("Toy Story",
                        "A story about a boy's childhood toys that secretly "
                        "come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",     # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Set in the 22nd century, as humans have depleted "
                     "Earth's natural resources and begin searching space for "
                     "a new resources, an injured marine visits an alien "
                     "planet that changes him.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",     # NOQA
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

doctor_strange = media.Movie("Doctor Strange",
                             "A doctor turns to teachings of mystical sorcery "
                             "to heal his injured hands when western medicine "
                             "fails him.",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",    # NOQA
                             "https://www.youtube.com/watch?v=Lt-U_t2pUHI")

dark_knight = media.Movie("The Dark Knight",
                          "As Batman works to keep crime in control in "
                          "Gotham, a criminal of a different level appears "
                          "and tests the hero to his limits.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",     # NOQA
                          "https://www.youtube.com/watch?v=kmJLuwP3MbY")

deadpool = media.Movie("Deadpool",
                       "A former special force operative turned mercenary "
                       "endures extreme experimentation and tortue in hopes "
                       "of a cure for his terminal disease. The experiments "
                       "are a success, but leave him with more than he was "
                       "asking for.",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",    # NOQA
                       "https://www.youtube.com/watch?v=9vN6DHB6bJc")

xmen_first_class = media.Movie("X-Men: First Class",
                               "Based on the marvel X-men comics, set in the "
                               "1960s in a world that is on the edge of a "
                               "nuclear war, two mutants from very different "
                               "backgrounds come together and create a team "
                               "of mutants to help save the world",
                               "https://upload.wikimedia.org/wikipedia/en/5/55/X-MenFirstClassMoviePoster.jpg",     # NOQA
                               "https://www.youtube.com/watch?v=UrbHykKUfTM")

# Add Movie objects to list
movies = [toy_story, avatar, doctor_strange, dark_knight, deadpool,
          xmen_first_class]

# Generate and open movies web page using list of created Movie objects
fresh_tomatoes.open_movies_page(movies)
