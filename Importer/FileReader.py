import os
from pathlib import Path
import csv

class FileReader:
    def __init__(self,folderName):
        self._folderName = folderName
        self._path = self.initPath(self._folderName)
        self._rowsDict={}
    
    def retrieveData(self): 
        os.environ["PYTHONUTF8"]="1"
        print("here")   
        print(self._path)
        
        for filename in os.listdir(self._path):
            try:
                file_path = os.path.join(self._path,os.fsdecode(os.fsencode(filename)))
                if os.path.isfile(file_path.encode('utf8').decode('utf8')):
                    self._rowsDict[filename]=self.readCSV(file_path)                                                            
            except Exception as e:
                error_message = f"Exception in reading this file: {filename}, Error stack trace: {str(e)}"
                print(error_message.encode('utf-8', errors='replace').decode('utf-8'))
                #print("Exception in reading this file:",filename.encode('utf8').decode('utf8'),"\n","error stackTrace:",e)
        return self._rowsDict    

    def initPath(self,folderName):
        currentDir = os.path.dirname(__file__)
        currentDir = Path(currentDir)
        parentDir = currentDir.parent.absolute()
        dataDir = Path(parentDir,"Data_to_import",folderName)
        return dataDir
    
    def readCSV(self,file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows=[]                        
            for row in csv_reader:
                rows.append(row)
            return rows