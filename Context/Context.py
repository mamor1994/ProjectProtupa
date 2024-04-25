from Repositories.MoviesRepository import MoviesRepository
from Repositories.ReviewsRepository import ReviewsRepository
from Repositories.UsersRepository import UsersRepository
class Context:
    def __init__(self,moviesRepository=None,usersRepository=None,reviewsRepository=None):
        if moviesRepository is None:
            self._moviesRepository=MoviesRepository()
        else:
            self._moviesRepository:MoviesRepository=moviesRepository
        if usersRepository is None:
            self._usersRepository=UsersRepository()
        else:
            self._usersRepository:UsersRepository=usersRepository
        if reviewsRepository is None:
            self._reviewsRepository=ReviewsRepository()
        else:
            self._reviewsRepository:ReviewsRepository=reviewsRepository

    @property        
    def moviesRepository(self):
        return self._moviesRepository
    
    @moviesRepository.setter
    def moviesRepository(self,value):
        self._moviesRepository=value

    @property        
    def reviewsRepository(self):
        return self._reviewsRepository
    
    @reviewsRepository.setter
    def reviewsRepository(self,value):
        self._reviewsRepository=value

    @property        
    def usersRepository(self):
        return self._usersRepository
    
    @usersRepository.setter
    def usersRepository(self,value):
        self._usersRepository=value
