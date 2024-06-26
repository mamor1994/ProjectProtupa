from Services.ImportService import ImportService
from Services.UsersService import UsersService
from Services.ClusterService import ClusterService
from JaccardMetric.JaccardDistance import JaccardSimilar
from Context.Context import Context
# from AI.TrainModel import TrainModel
from AI.ClusterModelTrainer import ClusterModelTrainer
from Tests.TestArray import TestArray


import sys
import io
import csv



def main():
    ratingsReal = initData()
    # beginAppWithRealData(ratingsReal)
    beginAppWithFakeData()
    pass

#part 1    
def initData():
    context = Context()  
    importService = ImportService()
    importService.importFromFolder2()
    importService.importFromFolder1()
    context = importService.writeToContext()
    usersService=UsersService(context)
    usersService.writeReviewDataToUsers()
    context = usersService.context
    
    # usersService.printData()
    # printMovieTitles(context)

    #get ratings as numpy array (rows=number of users,cols=ratings to all movies)
    #if a user didn't rate a movie, rating=0, also the order sequence is right because we use as index the movie.Id
    ratings = usersService.exractRatings()
    ratingsFiltered=usersService.filterRatings(5,8)
    return ratingsFiltered

#part 2
def kMeans(ratings):
    clusterService=ClusterService()
    clusterService._R=ratings
    clusterService.initMetric(clusterService.calculateEuclideanDistance) #or cosinedistance
    clusterService.applyKmeans(2)
    clusterService.showGraph()
    pass

def printMovieTitles(context=Context):
    movies = context.moviesRepository.Movies
    for movie in movies:
        print(movie.Title)

#last part-->b,c,d
def jaccard_similar(ratings):
    jaccardSimilar=JaccardSimilar()
    jaccardSimilar.R=ratings
    distance_matrix = jaccardSimilar.vectorized_jaccard_distance()    
    print("jaccard=",distance_matrix)
     # trainModel=TrainModel(distance_matrix,jaccard.R.shape[0],4,jaccard.binary_R)
    ratings = get_ratings()
    trainModel=ClusterModelTrainer(distance_matrix,ratings)
    trainModel.calculate_k_neighbors(k=5)
    trainModel.split_data()
    history  = trainModel.train_model(epochs=10)
    
    print("Μέσο Απόλυτο Σφάλμα (Εκπαίδευση):", history.history['mean_absolute_error'])
    print("Μέσο Απόλυτο Σφάλμα (Έλεγχος):", history.history['val_mean_absolute_error'])
    

def get_ratings():
    testArray = TestArray()
    ratings = testArray.getArray()
    return ratings

def beginAppWithRealData(ratings):

    kMeans(ratings)
    pass


def beginAppWithFakeData():
    testArray = TestArray()
    ratings = testArray.getArray()
    kMeans(ratings)
    pass

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')   
    main()
    # testUtils.testHashMap()
    # testUtils.testBinarySearchByName()
    # testUtils.testBinarySearchByNumber()
    # testUtils.testRegex()
    # main()
    
    
    # jaccard_similar()
    
   
   

    