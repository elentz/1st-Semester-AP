import media
import fresh_tomatoes

skyfall = media.Movie("Skyfall", "Undercover agents around the world are exposed", "https://en.wikipedia.org/wiki/Skyfall#/media/File:Skyfall_poster.jpg", "https://www.youtube.com/watch?v=6kw1UVovByw", "4 out of 5 Stars")
imitationgame = media.Movie("The Imitation Game", "Behind every code is an enigma", "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg", "https://www.youtube.com/watch?v=S5CjKEFb-sM", "4.5 out of 5 Stars")
afewgoodmen = media.Movie("A Few Good Men", "Can you handle the truth?", "https://upload.wikimedia.org/wikipedia/en/4/45/A_Few_Good_Men_poster.jpg", "https://www.youtube.com/watch?v=ePo91pMcu94", "4.9 out of 5 Stars")

movies = [skyfall, imitationgame, afewgoodmen]

fresh_tomatoes.open_movies_page(movies)
