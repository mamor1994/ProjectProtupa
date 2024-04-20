class ReviewsPerMovieDTO:
    def __init__(self) -> None:
        self._username=""
        self._rating=0
        self._helpful=0
        self._total=0
        self._date=""
        self._title=""
        self._review=""
        self._movieTitle=""

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
    def helpful(self):
        return self._helpful

    @helpful.setter
    def helpful(self, value):
        self._helpful = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def review(self):
        return self._review

    @review.setter
    def review(self, value):
        self._review = value

    @property
    def movieTitle(self):
        return self._movieTitle

    @movieTitle.setter
    def movieTitle(self, value):
        self._movieTitle = value

        

    