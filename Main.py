from Services.ImportService import ImportService
from Services.UsersService import UsersService
from Services.ClusterService import ClusterService
from JaccardMetric.JaccardDistance import JaccardSimilar
from Context.Context import Context
# from AI.TrainModel import TrainModel
from AI.ClusterModelTrainer import ClusterModelTrainer

from Logger.Logger import Logger



import sys
import io
import csv
import os
import numpy as np

current_repo_path = os.path.dirname(os.path.abspath(__file__))
logger = Logger(current_repo_path)


def getArray():
    R = np.array([
        [3,10,4,0,4,1,6,1,4,4,2,0,8,8,10],
        [9,9,10,5,5,8,9,2,8,3,5,9,3,4,5],
        [10,0,8,2,5,7,7,4,6,10,2,3,5,3,6],
        [7,10,4,7,5,3,5,0,7,5,10,2,1,10,7],
        [5,10,7,0,4,3,2,7,2,6,8,3,5,6,5],
        [1,9,1,7,6,0,10,1,6,8,6,7,0,0,3],
        [0,4,8,7,6,3,6,8,1,6,6,1,6,5,8],
        [5,7,10,9,1,6,10,7,3,2,8,7,4,4,8],
        [10,0,3,4,1,2,9,2,8,9,2,8,1,5,5],
        [7,5,8,9,10,7,7,1,0,4,7,7,8,3,3],
        [6,9,5,0,1,0,10,4,7,10,0,1,3,0,0],
        [1,6,7,5,3,5,0,8,10,2,9,5,1,3,6],
            
            
    ])
    return R



def main():
    # ratingsReal = initData()
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
    usersService=UsersService(context,logger)
    usersService.writeReviewDataToUsers()
    context = usersService.context
    
    usersService.printData()
    # printMovieTitles(context)

    #get ratings as numpy array (rows=number of users,cols=ratings to all movies)
    #if a user didn't rate a movie, rating=0, also the order sequence is right because we use as index the movie.Id
    usersService.exractRatings()    
    usersService.showDatesGraph()
    ratingsFiltered=usersService.filterRatings(2,3)
    printPart1(ratingsFiltered)
    # ratingsFiltered = usersService._ratings
    # print(ratingsFiltered)
    return ratingsFiltered

def printPart1(ratingsFiltered):
    num_of_users,num_of_movies = ratingsFiltered.shape
    print("Σύνολο χρηστών που θα ελεγχθούν",num_of_users)
    print("Σύνολο ταινιών που θα ελεγχθούν",num_of_movies)
    print("Σύνολο ratings",num_of_users*num_of_movies)
    pass

#part 2
def kMeans(ratings):
    clusterService=ClusterService(logger)
    clusterService._R=ratings
    clusterService.initMetric(clusterService.calculateEuclideanDistance) #or cosinedistance
    clusterService.applyKmeans(4)
    clusterService.showGraph()
    
    

def printMovieTitles(context=Context):
    movies = context.moviesRepository.Movies
    for movie in movies:
        print(movie.Title)

#last part-->b,c,d
def jaccard_similar(ratings):
    jaccardSimilar=JaccardSimilar()
    jaccardSimilar.R=ratings
    distance_matrix = jaccardSimilar.vectorized_jaccard_distance()    
    logger.appendToFile("jaccard.txt")    
    logger.writeObject("jaccard",distance_matrix.tolist(),4)
    logger.close()
    
    return distance_matrix
     # trainModel=TrainModel(distance_matrix,jaccard.R.shape[0],4,jaccard.binary_R)
    # ratings = get_ratings()
   
    
def trainModel(distance_matrix,ratings):
    trainModel=ClusterModelTrainer(distance_matrix,ratings,logger)
    trainModel.calculate_k_neighbors(k=5)
    trainModel.split_data()
    history  = trainModel.train_model(epochs=10)
    logger.appendToFile("lastPart.txt")
    logger.writeObject("Μέσο Απόλυτο Σφάλμα (Εκπαίδευση):",history.history['mean_absolute_error'],4)
    logger.writeObject("Μέσο Απόλυτο Σφάλμα (Έλεγχος):",history.history['val_mean_absolute_error'],4)
    logger.close()
    print("Μέσο Απόλυτο Σφάλμα (Εκπαίδευση):", history.history['mean_absolute_error'])
    print("Μέσο Απόλυτο Σφάλμα (Έλεγχος):", history.history['val_mean_absolute_error'])

def get_ratings():
    
    ratings = getArray()
    return ratings

def beginAppWithRealData(ratings):

    kMeans(ratings)
    distance_matrix=jaccard_similar(ratings)
    trainModel(distance_matrix,ratings)
    pass


def beginAppWithFakeData():
    # testArray = TestArray()
    ratings = getArray()
    kMeans(ratings)
    distance_matrix=jaccard_similar(ratings)
    trainModel(distance_matrix,ratings)
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
    
   
   

    