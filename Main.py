from Services.ImportService import ImportService
from Tests.TestUtils import TestUtils
import sys
import io
import csv


def main():        
    importService = ImportService()
    importService.importFromFolder2()
    





if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')   
    testUtils = TestUtils()
    # testUtils.testHashMap()
    # testUtils.testBinarySearchByName()
    # testUtils.testBinarySearchByNumber()

    main()

    