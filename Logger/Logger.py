from Logger.Encoder import Encoder
import sys
import json

class Logger:
    def __init__(self):        
        self._stdout = sys.stdout
        pass

    def appendToFile(self,filename):
        self._stdout=open(filename,'a')
        
    
    def writeLine(self,line):
        self._stdout.write(line+'\n')

    def writeObject(self,line,object,indent):
        encoder = Encoder()
        serializedObject=encoder.encode_obj(object)
        #serializedObject = json.dumps(object,indent=indent)
        self._stdout.write(line+'\n')
        self._stdout.write(json.dumps(serializedObject,indent=indent))
    
    def close(self):
        self._stdout.close()