class StringUtils:
    def __init__(self) -> None:
        pass

    def removeFirstPortion(self,string=str,portion=str):        
        if string.endswith(portion):
            return string.replace(portion,"")
        return string
    
    def convertTimeToMinutes(self,time):
        return