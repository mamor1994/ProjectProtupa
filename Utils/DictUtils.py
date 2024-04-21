class DictUtils:
    def __init__(self) -> None:
        pass

    def mapListToDictByTitle(self,movies):
        return {movie.Name: movie for movie in movies}
    
    def mapListToDictByUsername(self,users):
        return {user.Username: user for user in users}
    
