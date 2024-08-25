from Logger.Encoder import Encoder
import sys
import json
from pathlib import Path

class Logger:
    def __init__(self,repo_path):        
        self._stdout = sys.stdout
        self._repo_path=repo_path
        self._outputPath = Path(repo_path,"Output")
        pass

    def appendToFile(self,filename):
        self._stdout=open(Path(self._outputPath,filename),'a', encoding='utf-8')
        
    
    def writeLine(self,line):
        self._stdout.write(line+'\n')

    def writeObject(self,line,object,indent):
        # encoder = Encoder()
        # serializedObject=encoder.encode_obj(object)
        #serializedObject = json.dumps(object,indent=indent)
        self._stdout.write(line+'\n')
        self._stdout.write(json.dumps(object,indent=indent))
    
    def close(self):
        self._stdout.close()