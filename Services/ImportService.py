from Importer.FileReader import FileReader
from Mappers.ReviewsPerMovieMapper import ReviewsPerMovieMapper
from Repositories.MoviesRepository import MoviesRepository
from Repositories.ReviewsRepository import ReviewsRepository
class ImportService:
    def __init__(self) -> None:
        self._reviewsPerMovieDTOS=[]
        self._moviesRepository = MoviesRepository()
        self._reviewsRepository=ReviewsRepository()
        self._reviewsPerMovieMapper=ReviewsPerMovieMapper()
        pass

    def importFromFolder2(self):
        filereader = FileReader("2_reviews_per_movie_raw")
        
        #key filename,rows list
        rowsDict = filereader.retrieveData()              
        self.parseRowsDictToDTOS(rowsDict)
        self.parseDTOsToMoviesRepository()
        self.parseDTOsToReviewsRepository()
        
        
        # for movie in self._moviesRepository.Movies:
        #     print(movie.Title)
        # for movie in self._moviesRepository.MoviesDict:
        #     print(movie,"->",self._moviesRepository.MoviesDict[movie].Id)
        
        for review in self._reviewsRepository.ReviewsDict:
            print(review,"-->",self._reviewsRepository.ReviewsDict[review].title)
        #read files
        #parse data to DTOs
        #map data to Repositories->they will be sorted by id
        #sort users by username
        #sort movies by title
        pass

    def parseRowsDictToDTOS(self,rowsDict):
          for filename in rowsDict:
            
            rows = rowsDict[filename]
            for row in rows:                
                reviewsPerMovieDTO = self._reviewsPerMovieMapper.parseRowToRowData(row,filename)
                self._reviewsPerMovieDTOS.append(reviewsPerMovieDTO)

    def parseDTOsToMoviesRepository(self):
        for reviewsPerMovieDTO in self._reviewsPerMovieDTOS:
            movie = self._reviewsPerMovieMapper.reviewsPerMovieDToToMovie(reviewsPerMovieDTO)
            self._moviesRepository.save(movie)
    
    def parseDTOsToReviewsRepository(self):        
        for reviewsPerMovieDTO in self._reviewsPerMovieDTOS:
            review = self._reviewsPerMovieMapper.reviewsPerMovieDTOToReview(reviewsPerMovieDTO)
            self._reviewsRepository.save(review)
        pass
        