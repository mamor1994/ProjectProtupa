from Models.Movie import Movie
from Utils.ListUtils import ListUtils
from Utils.DictUtils import DictUtils
class MoviesRepository:
    def __init__(self):
        self._movies=[]
        self._moviesDict={}

    @property
    def MoviesDict(self):
        return self._moviesDict

    @MoviesDict.setter
    def MoviesDict(self, value):
        self._moviesDict = value


        

    @property
    def Movies(self):
        return self._movies

    @Movies.setter
    def Movies(self, value):
        self._movies = value

    def addMovie(self,movie=Movie):
        if len(self._movies)==0:
            movie.Id=1
        elif movie.Id==0:
            movie.Id=self._movies[len(self._movies)-1].Id+1
        self._movies.append(movie)
        self._moviesDict[movie.Title]=movie

    def updateMovie(self,index,movie=Movie):
        movieToChange = self._movies
        self._moviesDict.pop(movieToChange.Title)        
        self._movies[index]=movie
        self._moviesDict[movie.Title]=movie
        pass

    def save(self,movie=Movie):                
        tempMovie = self.findMovieByTitle(movie.Title)
        if tempMovie is None:
            self.addMovie(movie)
            return                        
        index = self.findById(tempMovie.Id)
        self.updateMovie(index,movie)            
        
        

    def findById(self,id):
        listUtils = ListUtils()
        index = listUtils.binarySearchByKeyFunc(self._movies,id)
        if index==-1:
            return None
        return self._movies[index]   

    def findMovieByTitle(self,title):
        return self._moviesDict.get(title,None)
        
        

    def saveAll(self,movies=[]):
        dictUtils = DictUtils()
        self._moviesDict.clear()
        self._movies.clear()
        self._moviesDict=dictUtils.mapListToDictByTitle(movies)
        self._movies=movies

    
    