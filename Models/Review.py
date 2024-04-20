class Review:
    def __init__(self) -> None:
        self._reviewId=0
        self._userId=0
        self._number_of_helpful=0
        self._date=""
        self._title=""
        self._description=""

    @property
    def Id(self):
        return self._reviewId

    @Id.setter
    def Id(self, value):
        self._reviewId = value

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, value):
        self._userId = value

    @property
    def number_of_helpful(self):
        return self._number_of_helpful

    @number_of_helpful.setter
    def number_of_helpful(self, value):
        self._number_of_helpful = value

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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
