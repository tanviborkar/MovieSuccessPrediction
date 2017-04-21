'''
Created on Apr 20, 2017

@author: Tanvi Borkar
'''
from __future__ import division
import csv
from src.rating.PredictRatingUsingActor import PredictRatingUsingActor
from src.rating.PredictRatingUsingDirector import PredictRatingUsingDirector
from src.rating.PedictRatingUsingGenre import PredictRatingUsingGenre

class PredictRatingUsingIMDBScore(object):
    actorRating = PredictRatingUsingActor()
    directorRating = PredictRatingUsingDirector()
    genreRating = PredictRatingUsingGenre()
    correctPrediction = 0
    incorrectPrediction = 0
    
    def readMovieDataFromFile(self):
        with open('rating/movie_summary.csv', 'rt') as csvfile:
            columnNames = ['movie_title', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name', 'genres', 'earnings', 'budget', 'imdb_score']
            reader = csv.DictReader(csvfile, columnNames)
            for row in reader:
                if(row['movie_title'] != 'movie_title'):
                    actorIMDBScore = self.actorRating.calculateRating(row['actor_1_name'], row['actor_2_name'], row['actor_3_name'])
                    directorIMDBScore = self.directorRating.calculateRating(row['director_name'])
                    genreIMDBScore = self.genreRating.calculateRating(row['genres'].split('|'))
                    combinedIMDBScore = ((4 * directorIMDBScore) + (3 * actorIMDBScore) + (3 * genreIMDBScore)) / 10
                    actualIMDBScore = float(row['imdb_score'])
                    if(((actualIMDBScore - 0.5) <= combinedIMDBScore) and (combinedIMDBScore <= (actualIMDBScore + 0.5))):
                        self.correctPrediction = self.correctPrediction + 1
                    else:
                        self.incorrectPrediction = self.incorrectPrediction + 1
                        
        percCorrect = (self.correctPrediction / (self.correctPrediction + self.incorrectPrediction)) * 100
        percIncorrect = (self.incorrectPrediction / (self.correctPrediction + self.incorrectPrediction)) * 100
        print('Correct Predictions %: '+str(percCorrect))
        print('Incorrect Predictions %:' +str(percIncorrect))
        
    def computeForUpcomingMovies(self, movieName, actor1Name, actor2Name, actor3Name, directorName, genreList):
            actorIMDBScore = self.actorRating.calculateRating(actor1Name, actor2Name, actor3Name)
            directorIMDBScore = self.directorRating.calculateRating(directorName)
            genreIMDBScore = self.genreRating.calculateRating(genreList)
            combinedIMDBScore = ((4 * directorIMDBScore) + (3 * actorIMDBScore) + (3 * genreIMDBScore)) / 10
            print('Predicted rating for movie '+movieName+' is '+str(combinedIMDBScore))    