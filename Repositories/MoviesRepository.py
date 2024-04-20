class MoviesRepository:
    def __init__(self):
        self._Movies=[]
        

    @property
    def Movies(self):
        return self._Movies

    @Movies.setter
    def Movies(self, value):
        self._Movies = value
