from Models.User import User
from Utils.ListUtils import ListUtils
from Utils.DictUtils import DictUtils
class UsersRepository:
    def __init__(self):
        self._users=[]
        self._usersDict={}
        self._userIds={}

    @property
    def UsersDict(self):
        return self._usersDict

    @UsersDict.setter
    def UsersDict(self, value):
        self._usersDict = value

    @property
    def UserIds(self):
        return self._userIds
    
    @UserIds.setter
    def UserIds(self,value):
        self._userIds=value


        

    @property
    def Users(self):
        return self._users

    @Users.setter
    def Users(self, value):
        self._users = value

    def addUser(self,user=User):
        if not self._users:
            user.Id=1
        else:
            user.Id=self._users[-1].Id+1
        self._users.append(user)
        self.writeUserToDicts(user)

    def updateUser(self,index,user=User):
        if index==-1 or index>=len(self._users):
            print(f"No user found at index {index} to update.")
            return
        userToChange = self._users[index]
        user.Id=userToChange.Id
        self._usersDict.pop(userToChange.Username)
        self._userIds.pop(userToChange.Id)        
        self._users[index]=user
        self.writeUserToDicts(user)
        pass

    def save(self,user=User):                
        tempUser = self.findUserByUsername(user.Username)
        if tempUser is None:
            self.addUser(user)
            return                        
        index = self.findById(tempUser.Id)
        self.updateUser(index,user)            
        
        

    def findById(self,id):
        listUtils = ListUtils()
        index = listUtils.binarySearchByKeyFunc(self._users,id)        
        return index  

    def findUserByUsername(self,username):
        return self._usersDict.get(username,None)
        
        

    def saveAll(self,users=[]):
        dictUtils = DictUtils()
        self._usersDict.clear()
        self._users.clear()
        self._usersDict=dictUtils.mapListToDictByUsername(users)
        self._users=users

    def writeUserToDicts(self,user=User):
        self._usersDict[user.Username]=user
        self._userIds[user.Id]=user
    
