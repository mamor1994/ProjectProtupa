from Importer.FileReader import FileReader
from Mappers.ReviewsPerMovieMapper import ReviewsPerMovieMapper
from Repositories.MoviesRepository import MoviesRepository
class ImportService:
    def __init__(self) -> None:
        self._reviewsPerMovieDTOS=[]
        self._moviesRepository = MoviesRepository()
        pass

    def importFromFolder1(self):
        filereader = FileReader("2_reviews_per_movie_raw")
        reviewsPerMovieMapper=ReviewsPerMovieMapper()
        rowsDict = filereader.retrieveData()
        
        for filename in rowsDict:
            reviewsPerMovieDTO = reviewsPerMovieMapper.parseRowToRowData(rowsDict[filename],filename)
            self._reviewsPerMovieDTOS.append(reviewsPerMovieDTO)
        for reviewsPerMovieDTO in self._reviewsPerMovieDTOS:
            movie = reviewsPerMovieMapper.reviewsPerMovieDToToMovie(reviewsPerMovieDTO)
            self._moviesRepository.save(movie)
        print("In import service")
        # for movie in self._moviesRepository.Movies:
        #     print(movie.Title)
        for movie in self._moviesRepository.MoviesDict:
            print(movie,"->",self._moviesRepository.MoviesDict[movie].Id)
        #read files
        #parse data to DTOs
        #map data to Repositories->they will be sorted by id
        #sort users by username
        #sort movies by title
        pass