'''
Created on Apr 2, 2017

@author: Tanvi Borkar
'''
from __future__ import division
import csv
from src.rating.Genre import Genre

class PredictRatingUsingGenre(object):
    maxFbLikes = 0.0
    maxProfit = 0.0
    maxIMDBScore = 0.0
    genreList = None
    
    def calculateRating(self, movieGenreList):
        self.genreList = []
        self.loadGenreData(movieGenreList)
        sumIMDBScore = 0.0
        for genre in self.genreList:
            sumIMDBScore = sumIMDBScore + genre.getGenreIMDBScore()
        return sumIMDBScore / len(self.genreList)
    
        '''
        count = 1
        sumFbLikes = 0.0
        sumProfit = 0.0
        sumIMDBScore = 0.0
        for actor in self.actorList:
            if count == 1:
                sumFbLikes = sumFbLikes + (0.6 *(actor.getActorFbLikes() / self.maxFbLikes))
                sumProfit = sumProfit + (0.6 * (actor.getActorTotalProfits() / self.maxProfit))
                sumIMDBScore = sumIMDBScore + (0.6 * (actor.getActorIMDBScore() / self.maxIMDBScore))
                count = count + 1
            elif count == 2:
                sumFbLikes = sumFbLikes + (0.3 *(actor.getActorFbLikes() / self.maxFbLikes))
                sumProfit = sumProfit + (0.3 * (actor.getActorTotalProfits() / self.maxProfit))
                sumIMDBScore = sumIMDBScore + (0.3 * (actor.getActorIMDBScore() / self.maxIMDBScore))
                count = count + 1
            elif count == 3:
                sumFbLikes = sumFbLikes + (0.1 *(actor.getActorFbLikes() / self.maxFbLikes))
                sumProfit = sumProfit + (0.1 * (actor.getActorTotalProfits() / self.maxProfit))
                sumIMDBScore = sumIMDBScore + (0.1 * (actor.getActorIMDBScore() / self.maxIMDBScore))
                count = count + 1
        sumFbLikes = sumFbLikes / 3
        sumProfit = sumProfit / 3
        sumIMDBScore = sumIMDBScore / 3
        print('Computed Score: '+ str(sumIMDBScore))
        #computedScore = (0.3 * sumFbLikes) + (0.7 * sumIMDBScore)
        #print('Computed Score: '+ str(computedScore))
        #computedScore = (0.25 * sumFbLikes) + (0.35 * sumProfit) + (0.4 * sumIMDBScore)
        #print('Computed Score: '+ str(computedScore))
        '''
        
    def loadGenreData(self, genreList):
        with open('rating/genre_summary.csv', 'rt') as csvfile:
            columnNames = ['genre_name', 'no_of_fb_likes', 'total_profit', 'total_imdb_score']
            reader = csv.DictReader(csvfile, columnNames)
            for row in reader:
                if(row['genre_name'] != 'genre_name'):
                    if(row['genre_name'] in genreList):
                        genreObj = Genre()
                        genreObj.setGenre(row['genre_name'])
                        genreObj.setGenreFbLikes(float(row['no_of_fb_likes']))
                        genreObj.setGenreTotalProfits(float(row['total_profit']))
                        genreObj.setGenreIMDBScore(float(row['total_imdb_score']))
                        self.genreList.append(genreObj)
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