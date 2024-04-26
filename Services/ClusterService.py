from Tests.TestArray import TestArray

try:
    from pyclustering.cluster.kmeans import kmeans
    from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
    from pyclustering.utils.metric import distance_metric, type_metric
    from sklearn.decomposition import PCA
    import numpy as np
    import matplotlib.pyplot as plt
    
except ImportError as e:
    print(e)
import math

class ClusterService:
    def __init__(self):
        testArray = TestArray()
        self._R=testArray.getArray()
        self._clusters=None
        self._centers=None
        self._metric = None

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
        R=self._R
        # Create instance of distance metric with your custom function
        metric = distance_metric(type_metric.USER_DEFINED, func=self._metric)

        # Prepare initial centers using K-Means++ method
        initial_centers = kmeans_plusplus_initializer(R, numOfClusters).initialize()

        # Create instance of K-Means algorithm with prepared centers
        kmeans_instance = kmeans(R, initial_centers, metric=metric)

        # Run cluster analysis and obtain results
        kmeans_instance.process()
        clusters = kmeans_instance.get_clusters()
        final_centers = kmeans_instance.get_centers()
        self._clusters=clusters
        self._centers=final_centers
        
        # Display results
        print("Clusters:", clusters)
        print("Centers:", final_centers)

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
        colors = plt.cm.get_cmap('viridis', len(clusters))

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

    