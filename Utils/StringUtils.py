import re
class StringUtils:
    def __init__(self) -> None:
        pass

    def removeFirstPortion(self,string=str,portion=str):        
        if string.endswith(portion):
            return string.replace(portion,"")
        return string
    
    def convertTimeToMinutes(self,time):
        return
    
    def findIndexRegex(self,string,regex):
        return re.search(rf"{regex}",string).span()[0]
    
    def retrieveStringBeforeRegex(self,string,regex):
        index = self.findIndexRegex(string,regex)        
        cuttedString = string[0:index]
        return cuttedString
    
    def convertDateStringToDate(self,string):
        return
    
    def convertStringRatingToNumber(self,string):
        if string == 'Null':
            return 0
        else:
            return int(string)
    