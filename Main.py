from Importer.FileReader import FileReader
import sys
import io
import csv


def main():    
    print(sys.stdout.encoding)
    filereader = FileReader("2_reviews_per_movie_raw")
    filereader.retrieveMovies()
    # currentDir = __file__
    # print(currentDir)



if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')   
    
    # main()

    