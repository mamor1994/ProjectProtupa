from Services.ImportService import ImportService

import sys
import io
import csv


def main():    
    print(sys.stdout.encoding)    
    importService = ImportService()
    importService.importFromFolder1()
    





if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')   
    
    main()

    