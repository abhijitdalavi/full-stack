import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story', 'A story of a boy and his toys that come to life',
                        'http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710',
                        'https://www.youtube.com/watch?v=4KPTXpQehio')

warcraft = media.Movie('Warcraft', 'A craft... of war!',
                        'http://cdn1-www.comingsoon.net/assets/uploads/gallery/warcraft-1387407720/warcraft_ver8_xlg.jpg',
                        'https://www.youtube.com/watch?v=2Rxoz13Bthc')

avatar = media.Movie('Avatar', 'A marine on an alien planet',
                     'http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

school_of_rock = media.Movie('School of Rock', 'Rock is the best teacher!',
                            'http://fanaru.com/school-of-rock/image/89703-school-of-rock-school-of-rock-poster-art.jpg',
                            'https://www.youtube.com/watch?v=3PsUJFEBC74')

matrix = media.Movie('The Matrix', 'Nothing is what it seems.',
                    'https://s-media-cache-ak0.pinimg.com/736x/01/b2/95/01b2953ef273ae55ff65acd8eac844eb.jpg',
                    'https://www.youtube.com/watch?v=m8e-FF8MsqU')

logan = media.Movie('Logan', 'He\'s back.',
                    'http://www.heyuguys.com/images/2016/10/Logan-Poster-Wolverine-3.jpg',
                    'https://www.youtube.com/watch?v=gbug3zTm3Ws')

#store movies in array
movies = [toy_story, warcraft, avatar, school_of_rock, matrix, logan]
#pass in movies to create website
#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
