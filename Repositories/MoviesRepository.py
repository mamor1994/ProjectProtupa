from Models.Movie import Movie
class MoviesRepository:
    def __init__(self):
        self._movies=[]

        

    @property
    def movies(self):
        return self._movies

    @movies.setter
    def movies(self, value):
        self._movies = value

    def addMovie(self,movie=Movie):
        if len(self._movies==0):
            movie.Id=1
        elif movie.Id==0:
            movie.Id=self._movies[len(self._movies)-1]+1
        self._movies.append(movie)

    def findMovieById(self,id):
        pass

    def findMovieByMovieTitle(self,title):
        pass