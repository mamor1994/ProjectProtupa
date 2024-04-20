class MovieImporter:
    def __init__(self,folderName):
        self._folderName = folderName
        self._files =[]

    def readFolder(self,folderName):
        for file in folderName:
            self._files.append(file)
    
    def parseFileToMovieDTO(self):
        return
