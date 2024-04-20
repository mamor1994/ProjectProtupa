class ReviewsPerMovieMapper:
    def __init__(self):
        self._rowData = []
        pass
    
    def parseRowToRowData(self,row,filename):
        username = row[0]
        rating = row[1]
        helpful = row[2]
        total = row[3]
        date = row[4]
        title = row[5]
        review = row[6]
        movieTitle = filename


        