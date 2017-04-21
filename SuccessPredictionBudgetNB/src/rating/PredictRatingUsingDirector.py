'''
Created on Apr 2, 2017

@author: Tanvi Borkar
'''
from __future__ import division
import csv 
from src.rating.Director import Director

class PredictRatingUsingDirector(object):
    maxFbLikes = 0.0
    maxProfit = 0.0
    maxIMDBScore = 0.0
    
    def calculateRating(self, directorName):
        directorObj =  self.loadDirectorData(directorName)
        if(directorObj != None):
            return directorObj.getDirectorIMDBScore()
        else:
            return 0.0
        #sumFbLikes = sumFbLikes + (0.6 *(actor.getActorFbLikes() / self.maxFbLikes))
        #sumProfit = sumProfit + (0.6 * (actor.getActorTotalProfits() / self.maxProfit))
        #sumIMDBScore = sumIMDBScore + (0.6 * (actor.getActorIMDBScore() / self.maxIMDBScore))
            
        #print('Computed Score: '+ str(sumIMDBScore))
        #computedScore = (0.3 * sumFbLikes) + (0.7 * sumIMDBScore)
        #print('Computed Score: '+ str(computedScore))
        #computedScore = (0.25 * sumFbLikes) + (0.35 * sumProfit) + (0.4 * sumIMDBScore)
        #print('Computed Score: '+ str(computedScore))
          
    def loadDirectorData(self, directorName):
        with open('rating/directors_summary.csv', 'rt') as csvfile:
            columnNames = ['director_name', 'no_of_fb_likes', 'total_profit', 'total_imdb_score']
            reader = csv.DictReader(csvfile, columnNames)
            for row in reader:
                if(row['director_name'] != 'director_name'):
                    if(row['director_name'] == directorName):
                        directorObj = Director()
                        directorObj.setDirectorName(row['director_name'])
                        directorObj.setDirectorFbLikes(float(row['no_of_fb_likes']))
                        directorObj.setDirectorTotalProfits(float(row['total_profit']))
                        directorObj.setDirectorIMDBScore(float(row['total_imdb_score']))
                        return directorObj
        return None
        
    '''
                    if(self.maxFbLikes<float(row['no_of_fb_likes'])):
                        self.maxFbLikes = float(row['no_of_fb_likes'])
                    
                    if(float(row['total_profit'])<0.0):
                        if(self.maxProfit< (float(row['total_profit']) * -1)):
                            self.maxProfit = float(row['total_profit']) * -1
                    else:
                        if(self.maxProfit< float(row['total_profit'])):
                            self.maxProfit = float(row['total_profit'])
                            
                    if(self.maxIMDBScore<float(row['total_imdb_score'])):
                        self.maxIMDBScore = float(row['total_imdb_score'])
                    '''