import numpy as np
from Tests.TestArray import TestArray
class JaccardSimilar:
    def __init__(self):
        testArray = TestArray()
        self._R=testArray.getArray()
        self._binary_R=None

    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, value):
        self._R = value


    @property
    def binary_R(self):
        return self._binary_R

    @binary_R.setter
    def binary_R(self, value):
        self._binary_R = value


    
    
    def calculate_jaccard_distance(self):
        R=self._R
        # Convert ratings matrix to binary (1 if rated, 0 otherwise)
        binary_ratings = (R > 0).astype(int)
        self._binary_R=binary_ratings
        # Initialize a matrix to store distances
        num_users = R.shape[0] #υπολογίζουμε το σύνολο των χρηστών
        distance_matrix = np.zeros((num_users, num_users))
        
        for i in range(num_users):
            for j in range(i + 1, num_users):
                # Calculate intersection and union for users i and j
                intersection = np.sum(np.logical_and(binary_ratings[i], binary_ratings[j])) #τομή συνόλου στη σχέση 5
                union = np.sum(np.logical_or(binary_ratings[i], binary_ratings[j])) #ένωση συνόλου στη σχέση 5
                
                # Calculate Jaccard index and then distance
                if union == 0:
                    # Avoid division by zero; implies both users have rated no items
                    jaccard_index = 1
                else:
                    jaccard_index = intersection / union
                
                # Jaccard distance
                distance = 1 - jaccard_index
                
                # Fill symmetric distance matrix
                distance_matrix[i, j] = distance_matrix[j, i] = distance
                
        return distance_matrix
    
    def vectorized_jaccard_distance(self):
        R = self._R
        binary_R = (R > 0).astype(int)
        self._binary_R=binary_R
        intersection = np.dot(binary_R, binary_R.T)
        row_sums = binary_R.sum(axis=1)
        union = row_sums[:, None] + row_sums - intersection

        # Avoid division by zero and compute Jaccard index
        np.fill_diagonal(union, 1)  # Prevent division by zero on diagonal
        jaccard_index = intersection / union
        distance_matrix = 1 - jaccard_index

        return distance_matrix