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
    context = Context()  
    importService = ImportService()
    importService.importFromFolder2()
    importService.importFromFolder1()
    context = importService.writeToContext()
    usersService=UsersService(context)
    usersService.writeReviewDataToUsers()
    context = usersService.context
    
    usersService.printData()
    printMovieTitles(context)
    

def kMeans():
    # clusterService=ClusterService()
    # clusterService.initMetric(clusterService.calculateEuclideanDistance)
    # clusterService.applyKmeans(2)
    # clusterService.showGraph()
    pass

def printMovieTitles(context=Context):
    movies = context.moviesRepository.Movies
    for movie in movies:
        print(movie.Title)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')   
    
    # testUtils.testHashMap()
    # testUtils.testBinarySearchByName()
    # testUtils.testBinarySearchByNumber()
    # testUtils.testRegex()
    # main()
    
    
  
    testArray = TestArray()
    ratings = testArray.getArray()
    jaccardSimilar=JaccardSimilar()
    distance_matrix = jaccardSimilar.vectorized_jaccard_distance()
    print("jaccard=",distance_matrix)
    # trainModel=TrainModel(distance_matrix,jaccard.R.shape[0],4,jaccard.binary_R)
    trainModel=ClusterModelTrainer(distance_matrix,ratings)
    trainModel.calculate_k_neighbors(k=5)
    trainModel.split_data()
    history  = trainModel.train_model(epochs=10)
    
    print("Μέσο Απόλυτο Σφάλμα (Εκπαίδευση):", history.history['mean_absolute_error'])
    print("Μέσο Απόλυτο Σφάλμα (Έλεγχος):", history.history['val_mean_absolute_error'])

    