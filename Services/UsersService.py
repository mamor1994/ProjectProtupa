from Context.Context import Context
from Models.User import User


class UsersService:
    def __init__(self,context=Context):
        self._context=context
        self._usersRepository=context.usersRepository
        self._moviesRepository=context.moviesRepository
        self._reviewsRepository=context.reviewsRepository

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        self._context = value

    def writeReviewDataToUsers(self):
        for review in self._reviewsRepository.Reviews:
            self.mapReviewToUser(review)
        self._context.usersRepository=self._usersRepository

    def printData(self):
        #print user names and number of reviews per user
        for user in self._usersRepository.Users:
            print(user.Username,"-->",user.total_reviews)
        print(len(self._usersRepository.Users))

    def mapReviewToUser(self,review):
        user=self._usersRepository.findUserByUsername(review.username)
        if user is None:
            user=User()        
            user.Username=review.username
        user.reviews.append(review)
        user.total_reviews=len(user.reviews)
        self._usersRepository.save(user)
        