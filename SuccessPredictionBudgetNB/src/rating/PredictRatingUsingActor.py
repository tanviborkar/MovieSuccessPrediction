'''
Created on Apr 2, 2017

@author: Tanvi Borkar
'''
from __future__ import division
import csv
from src.rating.Actor import Actor

class PredictRatingUsingActor(object):
    maxFbLikes = 0.0
    maxProfit = 0.0
    maxIMDBScore = 0.0
    actorList = None
    
    def calculateRating(self, actor1Name, actor2Name, actor3Name):
        print('Actor 1: '+actor1Name+' Actor 2: '+actor2Name+' Actor 3: '+actor3Name)
        self.actorList = []
        self.loadActorData(actor1Name, actor2Name, actor3Name)
        count = 1
        #sumFbLikes = 0.0
        #sumProfit = 0.0
        sumIMDBScore = 0.0
        for actor in self.actorList:
            if count == 1:
                #sumFbLikes = sumFbLikes + (0.6 *(actor.getActorFbLikes() / self.maxFbLikes))
                #sumProfit = sumProfit + (0.6 * (actor.getActorTotalProfits() / self.maxProfit))
                #sumIMDBScore = sumIMDBScore + (0.6 * (actor.getActorIMDBScore() / self.maxIMDBScore))
                sumIMDBScore = sumIMDBScore + (6 * actor.getActorIMDBScore())
                count = count + 1
            elif count == 2:
                #sumFbLikes = sumFbLikes + (0.3 *(actor.getActorFbLikes() / self.maxFbLikes))
                #sumProfit = sumProfit + (0.3 * (actor.getActorTotalProfits() / self.maxProfit))
                #sumIMDBScore = sumIMDBScore + (0.3 * (actor.getActorIMDBScore() / self.maxIMDBScore))
                sumIMDBScore = sumIMDBScore + (3 * actor.getActorIMDBScore())
                count = count + 1
            elif count == 3:
                #sumFbLikes = sumFbLikes + (0.1 *(actor.getActorFbLikes() / self.maxFbLikes))
                #sumProfit = sumProfit + (0.1 * (actor.getActorTotalProfits() / self.maxProfit))
                #sumIMDBScore = sumIMDBScore + (0.1 * (actor.getActorIMDBScore() / self.maxIMDBScore))
                sumIMDBScore = sumIMDBScore + actor.getActorIMDBScore()
                count = count + 1
        #sumFbLikes = sumFbLikes / 3
        #sumProfit = sumProfit / 3
        #sumIMDBScore = sumIMDBScore / 3
        sumIMDBScore = sumIMDBScore / 10
        print('Computed Score: '+ str(sumIMDBScore))
        return sumIMDBScore
        #computedScore = (0.3 * sumFbLikes) + (0.7 * sumIMDBScore)
        #print('Computed Score: '+ str(computedScore))
        #computedScore = (0.25 * sumFbLikes) + (0.35 * sumProfit) + (0.4 * sumIMDBScore)
        #print('Computed Score: '+ str(computedScore))
          
    def loadActorData(self, actorName1, actorName2, actorName3):
        with open('rating/actors_summary.csv', 'rt') as csvfile:
            columnNames = ['actor_name', 'no_of_fb_likes', 'total_profit', 'total_imdb_score']
            reader = csv.DictReader(csvfile, columnNames)
            for row in reader:
                if(row['actor_name'] != 'actor_name'):
                    if((row['actor_name'] == actorName1) or (row['actor_name'] == actorName2) or (row['actor_name'] == actorName3)):
                        actorObj = Actor()
                        actorObj.setActorName(row['actor_name'])
                        actorObj.setActorFbLikes(float(row['no_of_fb_likes']))
                        actorObj.setActorTotalProfits(float(row['total_profit']))
                        actorObj.setActorIMDBScore(float(row['total_imdb_score']))
                        self.actorList.append(actorObj)
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