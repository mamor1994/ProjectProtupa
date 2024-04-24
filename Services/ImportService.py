from Importer.FileReader import FileReader
from Mappers.ReviewsPerMovieMapper import Mapper
from Repositories.MoviesRepository import MoviesRepository
from Repositories.ReviewsRepository import ReviewsRepository
from Context.Context import Context
class ImportService:
    def __init__(self) -> None:
        self._reviewsPerMovieDTOS=[]
        self._movieDetailsDTOs=[]
        self._moviesRepository = MoviesRepository()
        self._reviewsRepository=ReviewsRepository()
        self._mapper=Mapper()
        pass

    def importFromFolder2(self):
        filereader = FileReader("2_reviews_per_movie_raw")
        
        #key filename,rows list
        rowsDict = filereader.retrieveData()              
        self.parseReviewsDictToDTOS(rowsDict)
        #print(len(self._reviewsPerMovieDTOS))
        self.parseReviewsDTOsToMoviesRepository()
        self.parseReviewsDTOsToReviewsRepository()
        
        #read files
        #parse data to DTOs
        #map data to Repositories->they will be sorted by id
        #sort users by username
        #sort movies by title
        pass
    
    def importFromFolder1(self):
        fileReader = FileReader("1_movies_per_genre")
        rowsDict = fileReader.retrieveData()
        self.parseMoviesDictToDTOs(rowsDict)
        self.parseMovieDetailsDTOsToMoviesRepository()


    def parseReviewsDictToDTOS(self,rowsDict):
          for filename in rowsDict:            
            rows = rowsDict[filename]
            for row in rows:                
                reviewsPerMovieDTO = self._mapper.parseReviewRowToRowData(row,filename)
                self._reviewsPerMovieDTOS.append(reviewsPerMovieDTO)

    def parseMoviesDictToDTOs(self,rowsDict):
        for filename in rowsDict:        
            rows = rowsDict[filename]
            for row in rows:                
                movieDetailsDTO = self._mapper.parseMovieDetailsToDTO(row,filename)
                self._movieDetailsDTOs.append(movieDetailsDTO)
        return

    def parseReviewsDTOsToMoviesRepository(self):        
        for reviewsPerMovieDTO in self._reviewsPerMovieDTOS:
            movie = self._mapper.reviewsPerMovieDTOToMovie(reviewsPerMovieDTO)
            self._moviesRepository.save(movie)
    
    def parseReviewsDTOsToReviewsRepository(self):        
        for reviewsPerMovieDTO in self._reviewsPerMovieDTOS:
            review = self._mapper.reviewsPerMovieDTOToReview(reviewsPerMovieDTO)
            self._reviewsRepository.save(review)
        pass

    def parseMovieDetailsDTOsToMoviesRepository(self):
        for movieDetailsDTO in self._movieDetailsDTOs:
            movie = self._mapper.movieDetailsDTOToMovie(movieDetailsDTO)
            self._moviesRepository.save(movie)
        return    
    
    def writeToContext(self):
        context = Context()
        context.moviesRepository = self._moviesRepository
        context.reviewsRepository = self._reviewsRepository
        return context