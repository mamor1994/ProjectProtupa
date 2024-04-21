from Models.User import User
from Utils.ListUtils import ListUtils
from Utils.DictUtils import DictUtils
class UsersRepository:
    def __init__(self):
        self._users=[]
        self._usersDict={}

    @property
    def UsersDict(self):
        return self._usersDict

    @UsersDict.setter
    def UsersDict(self, value):
        self._usersDict = value


        

    @property
    def Users(self):
        return self._users

    @Users.setter
    def Users(self, value):
        self._users = value

    def addUser(self,user=User):
        if len(self._users)==0:
            user.Id=1
        elif user.Id==0:
            user.Id=self._users[len(self._users)-1].Id+1
        self._users.append(user)
        self._usersDict[user.Username]=user

    def updateUser(self,index,user=User):
        userToChange = self._users[index]
        self._usersDict.pop(userToChange.Username)        
        self._users[index]=user
        self._usersDict[user.Username]=user
        pass

    def save(self,user=User):                
        tempUser = self.findUserByTitle(user.Username)
        if tempUser is None:
            self.addUser(user)
            return                        
        index = self.findById(tempUser.Id)
        self.updateUser(index,user)            
        
        

    def findById(self,id):
        listUtils = ListUtils()
        index = listUtils.binarySearchByKeyFunc(self._users,id)
        if index==-1:
            return None
        return self._users[index]   

    def findUserByTitle(self,title):
        return self._usersDict.get(title,None)
        
        

    def saveAll(self,users=[]):
        dictUtils = DictUtils()
        self._usersDict.clear()
        self._users.clear()
        self._usersDict=dictUtils.mapListToDictByUsername(users)
        self._users=users
    
