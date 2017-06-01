


import fresh_tomatoes
import media

#Movies
#INPUT (1)title, (2)description, (3)poster image url, (4)youtube trailer, (5)running time/duration and the rest = None
pirates_and_the_carribean_awe = media.Movie("Pirates and the Caribbean: At World's End",
                            "The Navy and the Pirates are at war, and Jack Sparrow is at the other side of the world.",
                            "https://upload.wikimedia.org/wikipedia/en/5/5a/Pirates_AWE_Poster.jpg",
                            "https://youtu.be/HKSZtp_OGHY")

hot_fuzz = media.Movie("Hot Fuzz",
                        "A city cop transfer into a country that is too good to be true.",
                        "https://video-images.vice.com/articles/58f8c3404f1b2b08f9702e38/lede/1492697921013-2007-hot_fuzz-4.jpeg",
                        "https://youtu.be/ayTnvVpj9t4")

austin_powers = media.Movie("Austin Powers: International Man of Mystery",
                            "Super agent was frozen in his year and unfrozen in another year when there's an evil vilian.",
                            "https://s-media-cache-ak0.pinimg.com/originals/0d/35/b9/0d35b9eb21939f0290204e00a529345d.jpg",
                            "https://youtu.be/5vsANcS4Ml8")

mrs_doubtfire = media.Movie("Mrs. Doubtfire",
                "A Husband pretends to be a grandma to babysit his children since the marriage wasn't working",
                "https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/19/1963bd5135521d623f6c29e6b1174975_500x735.jpg",
                "https://youtu.be/i8bONcsjaVo")

kungfupanda_1 = media.Movie("Kung fu Panda",
                "The panda from the noodle shop who plays with figurines is chose to be the Dragon Warrior",
                "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
                "https://youtu.be/PXi3Mv6KMzY")

djanggo = media.Movie("Django",
                    "A slave work his way up to save his wife and become the most skilled gunmanship in town",
                    "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                    "https://youtu.be/eUdM9vrCbow")

#TV show
#INPUT (1)title, (2)description, (3)poster image url, (4)youtube trailer, (5)running time/duration (6)number of season, (7)number of episode, (8)tv station
bobs_burgers = media.Movie("Bob's burgers",
                "A family started a burger restaurant",
                "http://www.gstatic.com/tv/thumb/tvbanners/13001523/p13001523_b_v8_ab.jpg",
                "https://youtu.be/_GxKewypGT8",
                "30 minutes",
                "7season",
                "Fox")

rick_and_morty = media.Movie("Rick and Morty",
                "Join Rick and his crazy scientist Uncle on space adventures",
                "http://static.tvtropes.org/pmwiki/pub/images/ramsignedmailer.jpg",
                "https://youtu.be/WNhH00OIPP0",
                "22 minutes",
                "3season",
                "Adult Swim")

sherlock_elemntary = media.Movie("Elementary",
                    "A recovering drug addict and former consultant Sherlock Holmes accompanied by his sober companion Dr. Joan Watson assists the NYC Police Department in solving crimes.",
                    "https://images-na.ssl-images-amazon.com/images/I/71ZBGKzqLXL._SL1058_.jpg",
                    "https://youtu.be/aRMBFMXyf-Q",
                    "43-46minutes",
                    "5season",
                    "CBS")

# Movies and Tv shows list
movies = [pirates_and_the_carribean_awe,hot_fuzz,austin_powers,mrs_doubtfire,kungfupanda_1,djanggo,bobs_burgers, rick_and_morty, sherlock_elemntary]


fresh_tomatoes.open_movies_page(movies)
