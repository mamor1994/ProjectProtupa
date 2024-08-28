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
    def flatArray(R):
        # Flatten the array to work with it easily
        R_flat = R.flatten()

        # Find the indices of non-zero elements
        non_zero_indices = np.nonzero(R_flat)[0]

        # Determine the number of elements to set to zero (e.g., 50% of non-zero elements)
        num_to_zero = int(len(non_zero_indices) * 0.5)

        # Randomly choose indices to set to zero
        zero_indices = np.random.choice(non_zero_indices, size=num_to_zero, replace=False)

        # Set the chosen indices to zero
        R_flat[zero_indices] = 0

        # Reshape the array back to its original shape
        R_majority_zeros = R_flat.reshape(R.shape)
        return R_majority_zeros
    
    R=flatArray(R)
    
    return R



def main():
   
    beginAppWithRealData()
    # beginAppWithFakeData()
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
    usersService.filterData(100,500)
    usersService.exractRatings()    
    usersService.showDatesGraph()
    usersService.showRatingsCounterGraph()
    # ratingsFiltered=usersService.filterRatings(2,3)
    ratingsFiltered=usersService.Ratings
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
    clusterService.applyKmeans(3)
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
    
   
    
def trainModel(distance_matrix,ratings):
    trainModel=ClusterModelTrainer(distance_matrix,ratings,logger)
    trainModel.calculate_k_neighbors(k=5)
    trainModel.split_data()
    history  = trainModel.train_model(epochs=10)
    logger.appendToFile("lastPart.txt")
    logger.writeObject("Μέσο Απόλυτο Σφάλμα (Εκπαίδευση):",history.history['mean_absolute_error'],4)
    logger.writeObject("Μέσο Απόλυτο Σφάλμα (Έλεγχος):",history.history['val_mean_absolute_error'],4)
    logger.close()
    mean_absolute_error=history.history['mean_absolute_error']
    val_mean_absolute_error=history.history['val_mean_absolute_error']
    return (mean_absolute_error,val_mean_absolute_error)

def calculateErrorRate(mean_absolute_error,val_mean_absolute_error):
    index = 0
    mean_dt=[]
    val_dt=[]
    val_mean_dt=[]
    for m_error in mean_absolute_error:
        if index+1<len(mean_absolute_error):
            mean_dt.append(mean_absolute_error[index+1]-m_error)
            val_dt.append(val_mean_absolute_error[index+1]-val_mean_absolute_error[index])
        val_mean_dt.append(val_mean_absolute_error[index]-mean_absolute_error[index])
        index+=1
    mean_dt_avg=sum(mean_dt)/len(mean_dt)
    val_dt_avg=sum(val_dt)/len(val_dt)

    print("Ρυθμός μεταβολής του Μέσου Απολύτου Σφάλματος(Εκπαίδευση):",mean_dt_avg)
    print("Ρυθμός μεταβολής του Μέσου Απολύτου Σφάλματος(Έλεγχος):",val_dt_avg)
    if abs(val_dt_avg - mean_dt_avg)<=0.01:
        print("Το μοντέλο αποδίδει παρόμοια στα δεδομένα εκπαίδευσης και επικύρωσης, υποδεικνύοντας καλή γενίκευση.")
    elif val_dt_avg>mean_dt_avg:
        print("Το μοντέλο μπορεί να υπερπροσαρμόζεται. Αποδίδει καλά στα δεδομένα εκπαίδευσης αλλά χειρότερα στα δεδομένα επικύρωσης.")
    elif val_dt_avg<mean_dt_avg:
        print("Αυτό είναι λιγότερο συχνό αλλά μπορεί να συμβεί αν το σύνολο επικύρωσης είναι ευκολότερο στην πρόβλεψη ή αν η κανονικοποίηση λειτουργεί αποτελεσματικά στο σύνολο επικύρωσης.")
    pass

def beginAppWithRealData():
    ratings=initData()
    beginApp(ratings)
    pass


def beginAppWithFakeData():
    # testArray = TestArray()
    ratings = getArray()    
    beginApp(ratings)
    pass

def beginApp(ratings):
    kMeans(ratings)
    distance_matrix=jaccard_similar(ratings)
    (mean_absolute_error,val_mean_absolute_error) = trainModel(distance_matrix,ratings)
    calculateErrorRate(mean_absolute_error,val_mean_absolute_error)

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')   
    main()
    # testUtils.testHashMap()
    # testUtils.testBinarySearchByName()
    # testUtils.testBinarySearchByNumber()
    # testUtils.testRegex()
    # main()
    
    
    # jaccard_similar()
    
   
   

    