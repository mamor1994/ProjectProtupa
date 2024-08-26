# from Tests2.TestArray2 import TestArray2
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning, message='All-NaN (slice|axis) encountered')

from joblib import Parallel, delayed
from Logger.Logger import Logger
try:
    from pyclustering.cluster.kmeans import kmeans
    from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
    from pyclustering.utils.metric import distance_metric, type_metric
    from sklearn.decomposition import PCA
    import numpy as np
    # Suppress all runtime warnings
    np.seterr(all='ignore')
    warnings.simplefilter(action='ignore', category=RuntimeWarning)
    import matplotlib.pyplot as plt
    
except ImportError as e:
    print(e)
import math

class ClusterService:
    def __init__(self,logger=Logger):
        
        self._R=None
        self._clusters=None
        self._centers=None
        self._metric = None
        self._logger=logger

    @property
    def Clusters(self):
        return self._clusters

    @Clusters.setter
    def Clusters(self, value):
        self._clusters = value

    @property
    def Centers(self):
        return self._centers

    @Centers.setter
    def Centers(self, value):
        self._centers = value

       
    def calculateCosineDistance(self,R1,R2):
        dot_product = sum(ru * rv * self.Lx(ru) * self.Lx(rv) for ru, rv in zip(R1, R2))
        magnitude_R1 = math.sqrt(sum(ru**2 * self.Lx(ru)*self.Lx(rv) for ru, rv in zip(R1, R2)))
        magnitude_R2 = math.sqrt(sum(rv**2 * self.Lx(ru)*self.Lx(rv) for ru, rv in zip(R1, R2)))
        if magnitude_R1 == 0 or magnitude_R2 == 0:
            return 1  # If either vector is all zeros after applying Lx, return max distance of 1
        cosine_similarity = dot_product / (magnitude_R1 * magnitude_R2)
        return 1 - cosine_similarity

        #return 1 - abs((sum(ru*rv*self.Lx(ru)*self.Lx(rv)) )/(math.sqrt(ru**2*self.Lx(ru)*self.Lx(rv))*math.sqrt(rv**2*self.Lx(rv)*self.Lx(rv))) for ru,rv in zip(R1,R2))
        
    
    def calculateEuclideanDistance(self,R1,R2):     
        return math.sqrt(sum(abs((ru-rv))**2*self.Lx(ru)*self.Lx(rv) for ru,rv in zip(R1,R2)))
    
    

    #binary λ
    def Lx(self,Rx):
        if Rx==0:
            return 0
        return 1
    
    def initMetric(self,func):
        self._metric=func

    def applyKmeans(self,numOfClusters):
        self._R = np.nan_to_num(self._R)  # Replace NaNs with 0
        R=self._R
        

        # Create instance of distance metric with your custom function
        metric = distance_metric(type_metric.USER_DEFINED, func=self._metric)

        # Prepare initial centers using K-Means++ method
        # initial_centers = kmeans_plusplus_initializer(R, numOfClusters).initialize()
        initial_centers = self.kmeans_plus_plus(R,numOfClusters)

        # Create instance of K-Means algorithm with prepared centers
        kmeans_instance = kmeans(R, initial_centers, metric=metric)

        # Run cluster analysis and obtain results
        kmeans_instance.process()
        clusters = kmeans_instance.get_clusters()
        final_centers = kmeans_instance.get_centers()
        self._clusters=clusters
        self._centers=final_centers
        
        # Display results
        self._logger.appendToFile("clusters.txt")
        self._logger.writeLine(("Number of Clusters:"+ str(len(clusters))))
        self._logger.writeObject("clusters:",final_centers,4)
        self._logger.close()
        # print("Number of Clusters:", len(clusters))
        # print("Centers:", final_centers)


    def showGraph(self):
        clusters = self._clusters
        centers = self._centers
        R=self._R


        if R.shape[1] > 2:
            pca = PCA(n_components=2)
            reduced_data = pca.fit_transform(R)

        # pca = PCA(n_components=2)
        # reduced_data = pca.fit_transform(R)

        # Generate a color palette
        colors = plt.get_cmap('viridis', len(clusters))

        # Plot each cluster
        for idx, cluster in enumerate(clusters):
            points = reduced_data[cluster, :]
            plt.scatter(points[:, 0], points[:, 1], s=30, c=[colors(idx)], label=f'Cluster {idx+1}')

        # Reduce dimensions of centers and plot
        if centers:
            centers_reduced = pca.transform(centers)
            plt.scatter(centers_reduced[:, 0], centers_reduced[:, 1], s=100, c='red', marker='x', label='Centers')

        plt.title('Cluster Visualization with PCA')
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.legend()
        plt.show()

    def create_distance_matrix(self,ratings):
        R = ratings
        num_users = R.shape[0]
        distance_matrix = np.zeros((num_users, num_users))

        # Use the custom metric function
        metric_func = self._metric

        def compute_distance(i, j):
            distance = metric_func(R[i], R[j])
            return i, j, distance

        # Parallel computation of the distance matrix
        results = Parallel(n_jobs=-1)(delayed(compute_distance)(i, j) for i in range(num_users) for j in range(i + 1, num_users))

        # Populate the distance matrix
        for i, j, distance in results:
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance  # Symmetric matrix

        return distance_matrix
    

    def kmeans_plus_plus(self,R, numOfClusters):
        np.random.seed(42)  # for reproducibility
        n_samples, _ = R.shape
        centers = []
        
        # Choose the first center randomly
        first_center_idx = np.random.choice(n_samples)
        centers.append(R[first_center_idx])
        
        for _ in range(1, numOfClusters):
            distances = np.min([np.sum((R - center)**2, axis=1) for center in centers], axis=0)
            probs = distances / distances.sum()
            cumulative_probs = np.cumsum(probs)
            r = np.random.rand()
            
            for j, p in enumerate(cumulative_probs):
                if r < p:
                    i = j
                    break
            centers.append(R[i])
        
        return np.array(centers)

    