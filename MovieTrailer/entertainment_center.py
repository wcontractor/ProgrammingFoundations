import fresh_tomatoes
import media

good_will_hunting = media.Movie("Good Will Hunting",
								"A Good Movie",
								"https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
								"https://www.youtube.com/watch?v=ReIJ1lbL-Q8")
								
lion_king = media.Movie("The Lion King",
								"The Circle of Life",
								"https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
								"https://www.youtube.com/watch?v=4sj1MT05lAA")

finding_nemo = media.Movie("Finding Nemo",
								"A movie about a fish",
								"https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
								"https://www.youtube.com/watch?v=yDPRaVX2p8c")

bourne_identity = media.Movie("The Bourne Identity",
								"Jason Bourne",
								"https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
								"https://www.youtube.com/watch?v=AfkNq0CDx6w")

#print(good_will_hunting.title)

movies = [good_will_hunting, lion_king, finding_nemo, bourne_identity]
fresh_tomatoes.open_movies_page(movies)