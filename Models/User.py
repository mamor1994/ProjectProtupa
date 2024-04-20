class User:
    def __init__(self) -> None:
        self._userId=0
        self._username=""
        self._total_reviews=0
        self._reviews=[]

    @property
    def Id(self):
        return self._userId

    @Id.setter
    def Id(self, value):
        self._userId = value

    @property
    def Name(self):
        return self._username

    @Name.setter
    def Name(self, value):
        self._username = value

    @property
    def total_reviews(self):
        return self._total_reviews

    @total_reviews.setter
    def total_reviews(self, value):
        self._total_reviews = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        self._reviews = value
