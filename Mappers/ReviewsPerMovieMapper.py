from DTOs.ReviewsPerMovieDTO import ReviewsPerMovieDTO
from DTOs.MovieDetailsDTO import MovieDetailsDTO
from Utils.StringUtils import StringUtils
from Models.Movie import Movie
from Models.Review import Review
from Models.User import User
class Mapper:
    def __init__(self):        
        pass


    
    def parseReviewRowToRowData(self,row,filename):
        dto = ReviewsPerMovieDTO()
        dto.username = row[0]
        dto.rating = row[1]
        dto.helpful = row[2]
        dto.total = row[3]
        dto.date = row[4]
        dto.title = row[5]
        dto.review = row[6]
        dto.movieTitle = filename
        return dto

    def reviewsPerMovieDTOToMovie(self,dto=ReviewsPerMovieDTO):        
        movie = Movie()
        movie.Title = self.convertFileNameToMovieTitle(dto.movieTitle)
        return movie                

    def reviewsPerMovieDTOToReview(self,dto=ReviewsPerMovieDTO):
        review = Review()
        review.username=dto.username
        review.rating=dto.rating        
        review.date=dto.date                        
        return review
    
    def reviewsPerMovieDTOToUser(self,dto=ReviewsPerMovieDTO):
        user=User()
        user.Username=dto.username
        return user
    
    def parseMovieDetailsToDTO(self,row,filename):
        dto = MovieDetailsDTO()
        dto.name = row[0]
        dto.year = row[1]
        dto.movie_rated=row[2]
        dto.run_length=row[3]
        dto.genres=row[4]
        dto.release_date=row[5]
        dto.rating=row[6]
        dto.num_raters=row[7]
        dto.num_reviews=row[8]
        dto.reviews_url=row[9]
        dto.movieGenreFileName=filename
        return dto
    
    def movieDetailsDTOToMovie(self,dto=MovieDetailsDTO):
        movie = Movie()
        movie.Title=dto.name        
        movie.length = dto.run_length
        movie.genres=dto.genres
        movie.released_date=dto.release_date
        movie.rating = dto.rating
        movie._number_of_rates = dto.num_raters
        movie.number_of_reviews = dto.num_reviews
        movie.review_url = dto.reviews_url        
        return movie
        
    def removeYear(self,string):
        stringUtils = StringUtils()
        cuttedString = stringUtils.retrieveStringBeforeRegex(string,r"[0-9]{4}$")
        return cuttedString
    
    

    def convertFileNameToMovieTitle(self,string):
        stringUtils = StringUtils()
        modifiedString = stringUtils.removeFirstPortion(string,".csv")
        modifiedString = self.removeYear(modifiedString).rstrip()
        if modifiedString == "3_10 to Yuma":            
            return "3:10 to Yuma"
        if modifiedString.endswith("_"):
            modifiedString = modifiedString.replace("_","?")
        modifiedString = modifiedString.replace("_ ",": ")
        return modifiedString
        