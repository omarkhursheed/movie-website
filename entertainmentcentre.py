import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "a boy's toys come to life",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "a marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/3/38/Avatarjakeneytiri.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()

inception = media.Movie("Inception","dreams within dreams",
                        "https://upload.wikimedia.org/wikipedia/en/1/18/Inception_OST.jpg",
                       "https://www.youtube.com/watch?v=YoHD9XEInc0")

movies = [toy_story, avatar, inception]

fresh_tomatoes.open_movies_page(movies)
