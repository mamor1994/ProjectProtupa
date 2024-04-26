from sklearn.metrics import pairwise_distances
import tensorflow as tf
import numpy as np

class TrainModel:
    def __init__(self,distance_matrix,num_users,k_neighbors,binary_R) -> None:
        self._distance_matrix=distance_matrix
        self._k_nearest_neighbors=None
        self._k_neighbors=k_neighbors
        self._binary_R=binary_R
        self._num_users=num_users
        self.calculateKNeighbors()


    def calculateKNeighbors(self):
        k=self._k_neighbors
        self._k_nearest_neighbors = np.argsort(self._distance_matrix, axis=1)[:, 1:k+1]

    

    def build_model(input_dim, output_dim):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation='relu', input_dim=input_dim),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(output_dim)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model
    
    def train_model(self):
        k_nearest_neighbors = self._k_nearest_neighbors
        num_users=self._num_users
        binary_R=self._binary_R
        # Για κάθε χρήστη
        for user_idx in range(num_users):
            # Αξιολογήσεις των πλησιέστερων γειτόνων
            neighbors_idx = k_nearest_neighbors[user_idx]
            input_features = binary_R[neighbors_idx].mean(axis=0)  # Μέση τιμή αξιολογήσεων των γειτόνων
            target_ratings = binary_R[user_idx]
            
            # Δημιουργία και εκπαίδευση μοντέλου
            model = self.build_model(input_features.shape[0], target_ratings.shape[0])
            model.fit(input_features.reshape(1, -1), target_ratings.reshape(1, -1), epochs=10)
