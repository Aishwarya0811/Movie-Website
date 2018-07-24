import media
import fresh_tomatoes

toy_story = media.Movie(" Toy Story",
                        " A story of a boy and his toys",
                        r"C:\Users\HP\Desktop\Python Project-2\Toy Story.jpg",
                          "https://www.youtube.com/watch?v=KYz2wyBy3kc")
Avatar = media.Movie(" Avatar",
                     "A marine on an alien Planet",
                     r"C:\Users\HP\Desktop\Python Project-2\Avatar.jpg",
                       "https://www.youtube.com/watch?v=5PSNL1qE6VY")
SchoolofRock = media.Movie(" School Of Rock",
                           " Using Rock Music to Learn",
                           r"C:\Users\HP\Desktop\Python Project-2\School Of Rock.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
Ratatouille = media.Movie(" Ratatouille"," A rat is a chef in Paris",
                          r"C:\Users\HP\Desktop\Python Project-2\Ratatouille.jpg",
                            "https://www.youtube.com/watch?v=c3sBBRxDAqk")
MidnightinParis = media.Movie(" MidnightinParis"," Going back in time to meet authors",
                              r"C:\Users\HP\Desktop\Python Project-2\midnight-in-paris.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
TheHungerGames = media.Movie("The Hunger Games","Can she defeat professionals in order to survive the game? ",
                             r"C:\Users\HP\Desktop\Python Project-2\The Hunger Games.jpg",
                               "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, Avatar, SchoolofRock, Ratatouille, MidnightinParis, TheHungerGames]
fresh_tomatoes.open_movies_page(movies)
