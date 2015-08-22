import fresh_tomatoes
import media

mission_impossible_rogue_nation = media.Movie("Mission:Impossible-Rogue Nation",
                        '''IMF Agent Ethan Hunt (Cruise) is on the run from the U.S. government
as he tries to prove the existence of the Syndicate, an international criminal consortium.''',
                        "https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",
                        "https://www.youtube.com/watch?v=pXwaKB7YOjw")

cinema_paradiso = media.Movie("Cinema Paradiso",
                        "A man's connection with movies",
                        "https://upload.wikimedia.org/wikipedia/en/8/86/CinemaParadiso.jpg",
                        "https://www.youtube.com/watch?v=C2-GX0Tltgw")

who_am_i = media.Movie("Who Am I",
                        "A member of Speical Force team found the answer of Who Am I",
                        "https://upload.wikimedia.org/wikipedia/en/0/00/WhoAmIJackieChan.jpg",
                        "https://www.youtube.com/watch?v=Gdx55aI-BLw")

rush_hour = media.Movie("Rush Hour",
                        "A detective from Hong Kong Police FOrce cooperates with a policeman from LAPD to solve a hijack case",
                        "https://upload.wikimedia.org/wikipedia/en/5/55/Rush_hour_ver2.jpg",
                        "https://www.youtube.com/watch?v=JMiFsFQcFLE")

police_story_3 = media.Movie("Police Story 3: Super Cop",
                        "Jackie's third police story",
                        "https://upload.wikimedia.org/wikipedia/en/5/5a/Policestory_poster.jpg",
                        "https://www.youtube.com/watch?v=6SBsRA28ZfY")

mr_nice_guy = media.Movie("Mr. Nice Guy",
                        '''Mr. Nice Guy features a collaboration between Jackie Chan and Richard Norton,
reuniting them for the first time since 1993's City Hunter and also Jackie Chan and Sammo Hung had worked
in the 1985's Twinkle, Twinkle Lucky Stars. Mr. Nice Guy was filmed in Melbourne, Australia.''',
                        "https://upload.wikimedia.org/wikipedia/en/d/db/MrNiceGuy_DVDcover.jpg",
                        "https://www.youtube.com/watch?v=HvWznfoTFa0")

# create an array of movies

movies = [mission_impossible_rogue_nation, cinema_paradiso,
          who_am_i, rush_hour, police_story_3, mr_nice_guy]

# generate and open the html to show the movie website

fresh_tomatoes.open_movies_page(movies)
