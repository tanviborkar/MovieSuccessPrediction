'''
Created on Mar 31, 2017

@author: Tanvi Borkar
'''
from src.budget.ReadCreateData import ReadCreateData
from src.budget.PredictTrainingSetAccuracy import PredictTrainingSetAccuracy
from src.rating.PredictRatingUsingIMDBScore import PredictRatingUsingIMDBScore
from src.rating.ReadIMDBData import ReadIMDBData

#obj = ReadCreateData()
#obj.readData()

#obj1 = PredictTrainingSetAccuracy()
#obj1.readTraingData()

obj2 = ReadIMDBData()
obj2.readDataCsv()

obj3 = PredictRatingUsingIMDBScore()
obj3.readMovieDataFromFile()