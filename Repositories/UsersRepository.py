class UsersRepository:
    def __init__(self):
        self._users=[]
        

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        self._users = value

    
