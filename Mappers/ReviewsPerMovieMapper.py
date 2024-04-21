from DTOs.ReviewsPerMovieDTO import ReviewsPerMovieDTO
from Models.Movie import Movie
from Models.Review import Review
from Models.User import User
class ReviewsPerMovieMapper:
    def __init__(self):        
        pass


    
    def parseRowToRowData(self,row,filename):
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

    def reviewsPerMovieDToToMovie(self,dto=ReviewsPerMovieDTO):
        movie = Movie()
        movie.Title = dto.movieTitle
        return movie                

    def reviewsPerMovieDTOToReview(self,dto=ReviewsPerMovieDTO):
        review = Review()
        return review
    
    def reviewsPerMovieDTOToUser(self,dto=ReviewsPerMovieDTO):
        user=User()
        return user
    



        