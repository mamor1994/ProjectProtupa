from Tests.TestArray import TestArray

try:
    from pyclustering.cluster.kmeans import kmeans
    from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
    from pyclustering.utils.metric import distance_metric, type_metric
except ImportError as e:
    print(e)
import math

class ClusterService:
    def __init__(self):
        testArray = TestArray()
        self._R=testArray.getArray()
       
    def calculateCosineDistance(self,Ru,Rv):
        return
    
    def calculateEuclideanDistance(self,R1,R2,lu,lv):
        lu=lv=1
        if Ru==0:
            lu=0
        if Rv==0:
            lv=0
        return math.sqrt(sum(abs((Ru-Rv))**2*lu*lv for Ru,Rv in zip(R1,R2)))
    #(p1 - p2)**2 for p1, p2 in zip(point1, point2)
    
    def applyKmeans(self):
        R=self._R
        # Create instance of distance metric with your custom function
        metric = distance_metric(type_metric.USER_DEFINED, func=self.calculateEuclideanDistance)

        # Prepare initial centers using K-Means++ method
        initial_centers = kmeans_plusplus_initializer(R, self.calculateEuclideanDistance).initialize()

        # Create instance of K-Means algorithm with prepared centers
        kmeans_instance = kmeans(R, initial_centers, metric=metric)

        # Run cluster analysis and obtain results
        kmeans_instance.process()
        clusters = kmeans_instance.get_clusters()
        final_centers = kmeans_instance.get_centers()

        # Display results
        print("Clusters:", clusters)
        print("Centers:", final_centers)