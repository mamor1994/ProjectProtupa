from Services.ImportService import ImportService
from Services.UsersService import UsersService
from Services.ClusterService import ClusterService
from Context.Context import Context



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
    clusterService=ClusterService()
    clusterService.applyKmeans(2)
    clusterService.showGraph()
    

    