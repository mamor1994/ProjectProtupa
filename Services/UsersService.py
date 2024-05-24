from Context.Context import Context
from Repositories.MoviesRepository import MoviesRepository
from Repositories.ReviewsRepository import ReviewsRepository
from Repositories.UsersRepository import UsersRepository
from Models.User import User
from Models.Review import Review
import numpy as np


class UsersService:
    def __init__(self,context=Context):
        self._context=context
        self._usersRepository:UsersRepository=context.usersRepository
        self._moviesRepository:MoviesRepository=context.moviesRepository
        self._reviewsRepository:ReviewsRepository=context.reviewsRepository
        self._ratings = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value

    @property
    def Ratings(self):
        return self._ratings

    @Ratings.setter
    def Ratings(self,value):
        self._ratings=value

    def writeReviewDataToUsers(self):
        for review in self._reviewsRepository.Reviews:
            self.mapReviewToUser(review)
        self._context.usersRepository=self._usersRepository

    def printData(self):
        #print user names and number of reviews per user
        # for user in self._usersRepository.Users:
        #     print(user.Username,"-->",user.total_reviews)
        # print(len(self._usersRepository.Users))
        print("Ο αριθμός των χρηστών U είναι",len(self._usersRepository.Users))
        print("Ο αριθμός των ταινιών I είναι",len(self._moviesRepository.Movies))
        pass

    def mapReviewToUser(self,review:Review):
        user=self._usersRepository.findUserByUsername(review.username)
        moviesLength = len(self._moviesRepository.Movies)
        movieTitle = review.movieTitle       
        movie = self._moviesRepository.findMovieByTitle(movieTitle)      
       
            

        if user is None:
            user=User(moviesLength)        
            user.Username=review.username
        if movie is not None:
            index = movie.Id-1
            ratings = user.Ratings
            ratings[index]=int(review.rating)
            user.Ratings=ratings
        else:
            print("movie is none with title:",movieTitle)      
        # print(user.Ratings)
        user.reviews.append(review)
        user.total_reviews=len(user.reviews)
        self._usersRepository.save(user)
        
        
    def filterUsers(self,min,max):
        users = self._usersRepository.Users
        filteredUsers=[]
        for user in users:
            if user._total_reviews>=min and user._total_reviews<=max:
                filteredUsers.append(user)            
        return filteredUsers
    
    def exractRatings(self):
        # ratings = np.zeros(len(self._usersRepository.Users),len(self._usersRepository.Users[0]))
        users = len(self._usersRepository.Users)
        movies = len(self._moviesRepository.Movies)
        ratings = np.zeros((users,movies),dtype=int)
        
        
        for index,user in enumerate(self._usersRepository.Users):
            ratings[index, :]=user.Ratings
            
            
        
        # ratings=np.vstack()
        self._ratings=ratings
        
    def filterRatings(self,min,max):
        within_range = (self._ratings>=min) & (self._ratings<=max)
        rows_within_range = np.all(within_range,axis=1)
        filteredRatings = self._ratings[rows_within_range]
