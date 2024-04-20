class Movie:
    def __init__(self):
        self._movieId=0       
        self._title=""
        self._rating=0
        self._released_date=""
        self._released_place=""
        self._length=0
        self._genres=""
        self._number_of_rates=0
        self._number_of_reviews=0
        self._review_url=""

    @property
    def movieId(self):
        return self._movieId

    @movieId.setter
    def movieId(self, value):
        self._movieId = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value

    @property
    def released_date(self):
        return self._released_date

    @released_date.setter
    def released_date(self, value):
        self._released_date = value

    @property
    def released_place(self):
        return self._released_place

    @released_place.setter
    def released_place(self, value):
        self._released_place = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def genres(self):
        return self._genres

    @genres.setter
    def genres(self, value):
        self._genres = value

    @property
    def number_of_rates(self):
        return self._number_of_rates

    @number_of_rates.setter
    def number_of_rates(self, value):
        self._number_of_rates = value

    @property
    def number_of_reviews(self):
        return self._number_of_reviews

    @number_of_reviews.setter
    def number_of_reviews(self, value):
        self._number_of_reviews = value

    @property
    def review_url(self):
        return self._review_url

    @review_url.setter
    def review_url(self, value):
        self._review_url = value

        