from Utils.ListUtils import ListUtils
class MyObject:
    def __init__(self, id, name):
        self.Id = id
        self.Name = name

objects = [MyObject(1, "Alice"), MyObject(2, "Bob"), MyObject(3, "Amélie 2001.csv")]






class TestUtils:
    def __init__(self):
        self._objects = objects
        # Sort the list by the `id` attribute if not already sorted
        self._objects.sort(key=lambda x: x.Id)
        

    def testBinarySearchByNumber(self):
        listUtils = ListUtils()
        index = listUtils.binarySearchByNumber(self._objects,3)
        print(index)
    
    def testBinarySearchByName(self):
        listUtils = ListUtils()
        self._objects.sort(key=lambda x:x.Name)
        index = listUtils.binarySearchByName(self._objects,"Amélie 2001.csv")
        print(index)

    def testHashMap(self):
        streetno = {
            "1": "Sachin Tendulkar",
            "2": "Dravid",
            "3": "Sehwag",
            "4": "Laxman",
            "5": "Kohli"
        }
        streetno["6"]="Hello from 6"
        
        if streetno.get("7",None) is None:
            print("Does not exist")
        print(streetno["6"])
