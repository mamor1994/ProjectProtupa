# import numpy as np
# from sklearn.model_selection import train_test_split
# import tensorflow as tf

# class TrainModel:
#     def __init__(self, user_data, k_neighbors, ratings):
#         self.user_data = user_data  # Το σύνολο των διανυσμάτων χαρακτηριστικών των χρηστών
#         self.k_neighbors = k_neighbors  # Αριθμός πλησιέστερων γειτόνων
#         self.ratings = ratings  # Οι αξιολογήσεις των χρηστών

#     def calculateKNeighbors(self):
#             k=self._k_neighbors
#             self._k_nearest_neighbors = np.argsort(self._distance_matrix, axis=1)[:, 1:k+1]

#     def split_data(self, test_size=0.2):
#         # Διαχωρισμός των δεδομένων σε εκπαιδευτικό και δοκιμαστικό σετ
#         self.train_data, self.test_data, self.train_labels, self.test_labels = train_test_split(
#             self.user_data, self.ratings, test_size=test_size, random_state=42
#         )

#     def build_model(self, input_dim):
#         # Δημιουργία του νευρωνικού δικτύου
#         model = tf.keras.Sequential([
#             tf.keras.layers.Dense(128, activation='relu', input_dim=input_dim),
#             tf.keras.layers.Dense(64, activation='relu'),
#             tf.keras.layers.Dense(1)  # Υποθέτοντας ότι προβλέπουμε μία συνεχή τιμή αξιολόγησης
#         ])
#         model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])
#         return model

#     def train_and_evaluate(self):
#         model = self.build_model(self.train_data.shape[1])
#         history = model.fit(self.train_data, self.train_labels, epochs=10, validation_data=(self.test_data, self.test_labels), verbose=0)
#         return history

# # Παράδειγμα δεδομένων
# num_users = 100
# features_per_user = 20  # Αριθμός χαρακτηριστικών ανά χρήστη
# k_neighbors = 5
# user_data = np.random.rand(num_users, features_per_user * k_neighbors)  # Παράδειγμα συγκεντρωτικών δεδομένων γειτόνων
# ratings = np.random.rand(num_users, 1)  # Παράδειγμα αξιολογήσεων χρηστών

# # Δημιουργία και εκπαίδευση του μοντέλου
# trainer = TrainModel(user_data, k_neighbors, ratings)
# trainer.split_data()
# history = trainer.train_and_evaluate()

# # Εκτύπωση αποτελεσμάτων
# print("Μέσο Απόλυτο Σφάλμα (Εκπαίδευση):", history.history['mean_absolute_error'])
# print("Μέσο Απόλυτο Σφάλμα (Έλεγχος):", history.history['val_mean_absolute_error'])
