import numpy as np
import warnings
np.warnings=warnings
class TestArray:
    def __init__(self) -> None:
        pass

    def getArray(self):
         R = np.array([
             [10, 0 , 3 , 4 , 0 , 2 , 1 , 1],
             [8 , 7 , 3 , 0 , 9 , 4 , 6 , 2],
             [2 , 10, 3 , 0 , 0 , 2 , 5 , 3],
             [3 , 1 , 6 , 0 , 4 , 4 , 4 , 0],
             [4 , 7 , 4 , 5 , 6 , 7 , 0 , 1],
             [9 , 10, 3 , 0 , 0 , 4 , 6 , 9],
             [0 , 8 , 4 , 0 , 0 , 4 , 6 , 9],
             [9 , 10, 6 , 0 , 0 , 4 , 6 , 9],
             [5 , 1 , 0 , 0 , 0 , 4 , 6 , 9],
             [2 , 1 , 1 , 0 , 0 , 3 , 5 , 4],
             [9 , 4 , 8 , 0 , 0 , 1 , 6 , 9],
             
         ])
         return R
    

 
