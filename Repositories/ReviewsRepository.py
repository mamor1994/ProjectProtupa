from Models.Review import Review
from Utils.ListUtils import ListUtils
from Utils.DictUtils import DictUtils
class ReviewsRepository:
    def __init__(self):
        self._reviews=[]
        self._reviewsDict={}

    @property
    def ReviewsDict(self):
        return self._reviewsDict

    @ReviewsDict.setter
    def ReviewsDict(self, value):
        self._reviewsDict = value


        

    @property
    def Reviews(self):
        return self._reviews

    @Reviews.setter
    def Reviews(self, value):
        self._reviews = value

    def addReview(self,review=Review):
        if len(self._reviews)==0:
            review.Id=1
        elif review.Id==0:
            review.Id=self._reviews[len(self._reviews)-1].Id+1
        self._reviews.append(review)
        self._reviewsDict[review.Id]=review

    def updateReview(self,index,review=Review):
        reviewToChange = self._reviews[index]
        self._reviewsDict.pop(reviewToChange.Id)        
        self._reviews[index]=review
        self._reviewsDict[review.Id]=review
        pass

    def save(self,review=Review):                
        tempReview = self.findReviewById(review.Id)
        if tempReview is None:
            self.addReview(review)
            return                        
        index = self.findById(tempReview.Id)
        self.updateReview(index,review)            
        
        

    def findById(self,id):
        listUtils = ListUtils()
        index = listUtils.binarySearchByKeyFunc(self._reviews,id)
        if index==-1:
            return None
        return self._reviews[index]   

    #hashmap
    def findReviewById(self,title):
        return self._reviewsDict.get(title,None)
        
        

    def saveAll(self,reviews=[]):
        dictUtils = DictUtils()
        self._reviewsDict.clear()
        self._reviews.clear()
        self._reviewsDict=dictUtils.mapListToDictByReviewId(reviews)
        self._reviews=reviews
