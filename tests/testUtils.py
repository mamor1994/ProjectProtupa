from Utils.ListUtils import ListUtils
class MyObject:
    def __init__(self, id, name):
        self.Id = id
        self.Name = name

objects = [MyObject(1, "Alice"), MyObject(2, "Bob"), MyObject(3, "Charlie")]






class TestUtils:
    def __init__(self):
        self._objects = objects
        # Sort the list by the `id` attribute if not already sorted
        self._objects.sort(key=lambda x: x.id)
        

    def testBinarySearchByNumber(self):
        listUtils = ListUtils()
        index = listUtils.binarySearchByNumber(self._objects,1)
        print(index)
