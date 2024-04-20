class ListUtils:
    def __init__(self):
        pass

    def binarySearchByNumber(self,list=[],number=0):
        key_func = lambda obj:obj.Id
        return self.binarySearchHelper(list, number, 0, len(list)-1, key_func)
    
    def binarySearchByName(self,list=[],name=""):
        key_func = lambda obj:obj.Name
        return self.binarySearchHelper(list, name, 0, len(list)-1, key_func)
         

    def binarySearchHelper(self,array, target, left, right, key_func):
        if left > right:
            return -1
        middle = (left+right) // 2
        potentialMatch = key_func(array[middle])
        if target == potentialMatch:
                return middle
        elif target < potentialMatch:
            return self.binarySearchHelper(array, target, left, middle - 1)
        else:
            return self.binarySearchHelper(array, target, middle + 1, right)