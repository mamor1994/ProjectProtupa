class ReviewsRepository:
    def __init__(self):
        self._reviews=[]
        

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        self._reviews = value
