class Review:
    def __init__(self) -> None:
        self._reviewId=0
        self._userId=0
        self._username=""        
        self._rating=0        
        self._date=""        
        self._movieTitle=""    

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, value):
        self._userId = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def movieTitle(self):
        return self._movieTitle

    @movieTitle.setter
    def movieTitle(self, value):
        self._movieTitle = value

        
    @property
    def Id(self):
        return self._reviewId

    @Id.setter
    def Id(self, value):
        self._reviewId = value



   
