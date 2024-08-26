from Context.Context import Context
from Repositories.MoviesRepository import MoviesRepository
from Repositories.ReviewsRepository import ReviewsRepository
from Repositories.UsersRepository import UsersRepository
from Models.User import User
from Models.Review import Review
from Logger.Logger import Logger
import os
from pathlib import Path
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class UsersService:
    def __init__(self,context=Context,logger=Logger):
        self._context=context
        self._usersRepository:UsersRepository=context.usersRepository
        self._moviesRepository:MoviesRepository=context.moviesRepository
        self._reviewsRepository:ReviewsRepository=context.reviewsRepository
        self._ratings = None
        self._logger = logger

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
        
        line1="Ο αριθμός των χρηστών U είναι:"+str(len(self._usersRepository.Users))
        line2="Ο αριθμός των ταινιών I είναι:"+str(len(self._moviesRepository.Movies))
       
        self._logger.appendToFile("Part1.txt")
        self._logger.writeLine(line1)
        self._logger.writeLine(line2)
        self._logger.close()
        print(line1)
        print(line2)
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
            timestamps = user.TimeStamps
            # timestamps[index] = datetime.strptime(review.date, '%d %B %Y')
            timestamps[index] = review.date
            user.TimeStamps=timestamps
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
    
    #μας δίνει την επιθυμητή μορφή του numpy array για επεξεργασία δεδομένων
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

        row_mask = np.any((self._ratings >= min) & (self._ratings <= max), axis=1)
        col_mask = np.any((self._ratings >= min) & (self._ratings <= max), axis=0)
    
        # Filter rows and columns based on the masks
        filteredRatings = self._ratings[row_mask][:, col_mask]
        # within_range = (self._ratings>=min) & (self._ratings<=max)
        # rows_within_range = np.all(within_range,axis=1)
        # filteredRatings = self._ratings[rows_within_range]
        return filteredRatings
    
    

    def showDatesGraph(self):
        first_dates=[]
        last_dates=[]
        for user in self._usersRepository.Users:
            timestamps=user.TimeStamps
            ratings = user.Ratings
            num_of_users=len(self._usersRepository.Users)
            timestamps_dt=np.array([datetime.strptime(date, '%d %B %Y') if date else None for date in timestamps])
            timestamps_dt = timestamps_dt[timestamps_dt != np.array(None)]
            first_dates.append(min(timestamps_dt))
            last_dates.append(max(timestamps_dt))

        first_dates=pd.to_datetime(first_dates)
        last_dates=pd.to_datetime(last_dates)
        # print("first_dates",first_dates)
        # print("last_dates",last_dates)
        # self._logger.appendToFile("timestamps.txt")
        # self._logger.writeObject("first dates",first_dates.tolist(),4)
        # self._logger.close()
        time_range = (last_dates-first_dates).days

        # Δημιουργία ιστογράμματος για το χρονικό εύρος των αξιολογήσεων
        plt.figure(figsize=(10, 6))
        plt.hist(time_range.dropna(), bins=20, color='green', edgecolor='black')
        plt.title('Histogram of Time Range of Ratings per User')
        plt.xlabel('Time Range (days)')
        plt.ylabel('Frequency')
        plt.grid(True)

        #  # Μορφοποίηση του άξονα χ για να εμφανίζει μήνες ή έτη
        # ax = plt.gca()
        # ax.xaxis_date()  # Ορίζει τον άξονα x σε ημερομηνίες
        # ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%B %Y'))  # Εμφανίζει μήνες και έτη



        plt.show()
        pass

    def filterData(self,min,max):
        users = self._usersRepository.Users
        filteredUsers=[]
        for user in users:
            if min<=np.count_nonzero(user.Ratings)<=max:
                filteredUsers.append(user)
        self._usersRepository.Users=filteredUsers
        
