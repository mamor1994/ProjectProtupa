from Models.Movie import Movie
from Models.Review import Review
from Models.User import User
class Encoder:
    def __init__(self) -> None:
        pass

    def encode_obj(self,obj):
        if isinstance(obj, Movie):
            return self.encode_movie(obj)
        if isinstance(obj, User):
            return self.encode_user(obj)
        if isinstance(obj, Review):
            return self.encode_review(obj)
        self.raiseErrorString(obj)
        
    def encode_movie(self,movie):        
        return {'Title':movie.Title}
        
    def encode_user(self,user):
        return {'Username':user.Username}
        
    def encode_review(self,review):        
        return {'Review_rating':review.rating}
        
    def raiseErrorString(self,obj):
        raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')
