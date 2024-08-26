import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from Logger.Logger import Logger

class ClusterModelTrainer:
    def __init__(self, distance_matrix, ratings,logger=Logger):
        self._distance_matrix = distance_matrix  # Προϋπολογισμένος πίνακας αποστάσεων
        self.ratings = ratings  # Ο πίνακας αξιολογήσεων χρστών (με τα μηδενικά)
        self._k_nearest_neighbors = None  # Θα υπολογιστεί στη συνέχεια
        self._num_users = ratings.shape[0]  # Αριθμός χρηστών βάσει των αξιολογήσεων
        self._logger=logger

    def calculate_k_neighbors(self, k):
        # Ενημερώνουμε τον αριθμό των γειτόνων που θέλουμε να εξετάσουμε
        self._k_nearest_neighbors = np.argsort(self._distance_matrix, axis=1)[:, 1:k+1]

    def split_data(self, test_size=0.2):
        # Διαχωρισμός των δεδομένων σε εκπαιδευτικό και δοκιμαστικό σετ
        self.train_data, self.test_data, self.train_labels, self.test_labels = train_test_split(
            self.ratings, self.ratings, test_size=test_size, random_state=42
        )

    def build_model(self, input_dim): #input_dim is number of features,δηλαδή στήλες στον πίνακα με τις αξιολογήσεις
        # Δημιουργία του νευρωνικού δικτύου
        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(input_dim,)),  # Specify the input shape explicitly
            tf.keras.layers.Dense(128, activation='relu', input_dim=input_dim),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1)  # Προβλέπουμε μία συνεχή τιμή αξιολόγησης
        ])
        model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])
        return model

    def train_model(self, epochs=10): #το epochs είναι συντελεστής, όσο πιο μεγάλος είναι τόσο πιο overfitting μπορεί να γίνουν τα αποτελέσματα
        model = self.build_model(len(self.ratings[0]))  # Χρησιμοποιούμε τον αριθμό ταινιών ως input_dim
        print(self.train_data.shape)
        history = model.fit(self.train_data, self.train_labels, epochs=epochs, 
                            validation_data=(self.test_data, self.test_labels), verbose=1)
        return history

# # Χρήση της κλάσης με προϋπολογισμένο distance_matrix και ratings
# num_users = 100
# features_per_user = 20  # Υποθετικά, αν κάθε χρήστης έχει 20 χαρακτηριστικά
# distance_matrix = np.random.rand(num_users, num_users)  # Παράδειγμα πίνακα αποστάσεων
# ratings = np.random.rand(num_users, 1)  # Παράδειγμα αξιολογήσεων χρηστών

# trainer = ClusterModelTrainer(distance_matrix, ratings)
# trainer.calculate_k_neighbors(k=5)
# trainer.split_data()
# history = trainer.train_model(epochs=10)
