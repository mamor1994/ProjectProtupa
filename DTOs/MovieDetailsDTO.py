class MovieDetailsDTO:
    def __init__(self) -> None:
        self._name = ''
        self._year=''
        self._movie_rated=''
        self._run_length=''
        self._genres=''
        self._release_date=''
        self._rating=''
        self._num_raters=''
        self._num_reviews=''
        self._reviews_url=''
        self._movieGenreFileName=''

    @property
    def movieGenreFileName(self):
        return self._movieGenreFileName

    @movieGenreFileName.setter
    def movieGenreFileName(self, value):
        self._movieGenreFileName = value


   

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def movie_rated(self):
        return self._movie_rated

    @movie_rated.setter
    def movie_rated(self, value):
        self._movie_rated = value

    @property
    def run_length(self):
        return self._run_length

    @run_length.setter
    def run_length(self, value):
        self._run_length = value

    @property
    def genres(self):
        return self._genres

    @genres.setter
    def genres(self, value):
        self._genres = value

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        self._release_date = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value

    @property
    def num_raters(self):
        return self._num_raters

    @num_raters.setter
    def num_raters(self, value):
        self._num_raters = value

    @property
    def num_reviews(self):
        return self._num_reviews

    @num_reviews.setter
    def num_reviews(self, value):
        self._num_reviews = value

    @property
    def reviews_url(self):
        return self._reviews_url

    @reviews_url.setter
    def reviews_url(self, value):
        self._reviews_url = value

        

    