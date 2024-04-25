from Models.Movie import Movie
from Utils.ListUtils import ListUtils
from Utils.DictUtils import DictUtils
from Logger.Logger import Logger

class MoviesRepository:
    def __init__(self):
        self._movies=[]
        self._moviesDict={}
        self._movieIds={}

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
        if not self._movies:
            movie.Id=1
        else:
            movie.Id=self._movies[-1].Id+1            
            #print(f"Added movie with id={movie.Id}")
        self._movies.append(movie)        
        self.writeMovieToDicts(movie)

    def updateMovie(self,index,movie=Movie):
        if index == -1 or index >= len(self._movies):
            print(f"No movie found at index {index} to update.")
            return
        movieToChange = self._movies[index]     
        movie.Id = movieToChange.Id
        self._moviesDict.pop(movieToChange.Title)        
        self._movieIds.pop(movieToChange.Id)        
        self._movies[index]=movie
        self.writeMovieToDicts(movie)      
        

    def save(self,movie=Movie):                
        tempMovie = self.findMovieByTitle(movie.Title)
        if tempMovie is None:
            
            self.addMovie(movie)            
            return                        
        index = self.findById(tempMovie.Id)                
        self.updateMovie(index,tempMovie)            
        
        

    def findById(self,id):
        listUtils = ListUtils()
        index = listUtils.binarySearchByKeyFunc(self._movies,id)
        return index
         
    def findMovieByTitle(self,title):
        return self._moviesDict.get(title,None)
            
    def saveAll(self,movies=[]):
        dictUtils = DictUtils()
        self._moviesDict.clear()
        self._movies.clear()
        self._moviesDict=dictUtils.mapListToDictByTitle(movies)
        self._movies=movies

    
    def writeMovieToDicts(self,movie=Movie):
        self._moviesDict[movie.Title]=movie
        self._movieIds[movie.Id]=movie