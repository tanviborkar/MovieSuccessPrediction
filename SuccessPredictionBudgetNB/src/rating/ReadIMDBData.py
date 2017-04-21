'''
Created on Apr 20, 2017

@author: Tanvi Borkar
'''
from __future__ import division
import csv

class ReadIMDBData(object):
    actorMap = dict()
    actorMapFinal = dict()
    
    directorMap = dict()
    directorMapFinal = dict()

    genresMap = dict()
    genresMapFinal = dict()
    
    moviesMap = dict()
     
    def readDataCsv(self):
        with open('rating/movie_metadata.csv', 'rt') as csvfile:
            columnNames = ['color', 'director_name', 'num_critic_for_reviews', 'duration', 'director_facebook_likes', 'actor_3_facebook_likes', 'actor_2_name', 'actor_1_facebook_likes', 'gross', 'genres', 'actor_1_name', 'movie_title', 'num_voted_users', 'cast_total_facebook_likes', 'actor_3_name', 'facenumber_in_poster', 'plot_keywords', 'movie_imdb_link', 'num_user_for_reviews', 'language', 'country', 'content_rating', 'budget', 'title_year', 'actor_2_facebook_likes', 'imdb_score', 'aspect_ratio', 'movie_facebook_likes']
            reader = csv.DictReader(csvfile, columnNames)
            for row in reader:
                #code for processing actor data
                if(row['actor_1_name'] != 'actor_1_name'):
                    if(row['actor_1_name'] != ''):
                        self.processActorData(row['actor_1_name'], row['actor_1_facebook_likes'], row['gross'], row['budget'], row['imdb_score'])
                    if(row['actor_2_name'] != ''):
                        self.processActorData(row['actor_2_name'], row['actor_2_facebook_likes'], row['gross'], row['budget'], row['imdb_score'])
                    if(row['actor_3_name'] != ''):
                        self.processActorData(row['actor_3_name'], row['actor_3_facebook_likes'], row['gross'], row['budget'], row['imdb_score'])
                    
                    if(row['director_name'] != ''):
                        self.processDirectorData(row['director_name'], row['director_facebook_likes'], row['gross'], row['budget'], row['imdb_score']);
                    
                    if(row['genres'] != ''):
                        self.processGenresData(row['genres'], row['movie_facebook_likes'], row['gross'], row['budget'], row['imdb_score'])
                        
                    if(row['movie_title'] != ''):
                        self.processMovieData(row['movie_title'], row['actor_1_name'], row['actor_2_name'], row['actor_3_name'], row['director_name'], row['genres'], row['gross'], row['budget'], row['imdb_score'])
            
            self.processActorMap()
            self.writeActorDataToFile()
             
            self.processDirectorMap()
            self.writeDirectorDataToFile()
            
            self.processGenreMap()
            self.writeGenreDataToFile()
            
            self.writeMovieDataToFile()            
            
    def processActorData(self, actorName, actorFbLikes, movieEarnings, movieBudget, imdbScore):
        if(self.actorMap.__contains__(actorName)):
            valueMap = self.actorMap.get(actorName)
            #print(actorFbLikes)
            if(actorFbLikes != ''):
                valueMap.get('fbLikes').append(float(actorFbLikes))
            else:
                valueMap.get('fbLikes').append(0.0)
            #floatValue = float(actorFbLikes)
            #print(floatValue)
            if((movieEarnings != '') and (movieBudget != '')):
                profit = (float(movieEarnings))/float(movieBudget)
            else:
                profit = 0.0
            valueMap.get('profitValues').append(profit)
            if(imdbScore != ''):
                valueMap.get('imdbScore').append(float(imdbScore))
            else:
                valueMap.get('imdbScore').append(0.0)
        else:
            valueMap = dict()
            #print(actorFbLikes)
            if(actorFbLikes != ''):
                valueMap['fbLikes'] = [float(actorFbLikes)]
            else:
                valueMap['fbLikes'] = 0.0
            #floatValue = float(actorFbLikes)
            #print(floatValue)
            if((movieEarnings != '') and (movieBudget != '')):
                profit = (float(movieEarnings))/float(movieBudget)
            else:
                profit = 0.0
            valueMap['profitValues'] = [profit]
            if(imdbScore != ''):
                valueMap['imdbScore'] = [float(imdbScore)]
            else:
                valueMap['imdbScore'] = 0.0
            self.actorMap[actorName] = valueMap
         
    def processActorMap(self):
        for actor in self.actorMap.keys():
            valueMap = self.actorMap.get(actor)
            noOfFbLikes = self.getTotal(valueMap.get('fbLikes'))
            totalProfit = self.getTotal(valueMap.get('profitValues'))
            totalScore = self.getTotal(valueMap.get('imdbScore'))
            valueMapFinal = dict()
            valueMapFinal['fbLikes'] = noOfFbLikes
            valueMapFinal['totalProfit'] = totalProfit
            valueMapFinal['totalScore'] = totalScore
            self.actorMapFinal[actor] = valueMapFinal
                   
    def getTotal(self, objList):
        sum = 0.0
        for obj in objList:
            sum = sum + obj
        return sum/len(objList)
    
    def writeActorDataToFile(self):
        with open('rating/actors_summary.csv', 'w') as csvfile:
            fieldnames = ['actor_name', 'no_of_fb_likes', 'total_profit', 'total_imdb_score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for actor in self.actorMapFinal.keys():
                valueMap = self.actorMapFinal.get(actor)
                writer.writerow({'actor_name': actor, 'no_of_fb_likes': valueMap.get('fbLikes'), 'total_profit': valueMap.get('totalProfit'), 'total_imdb_score': valueMap.get('totalScore')})
    
    def printActor(self):
        for actor in self.actorMap.keys():
            print('Actor Name: '+ actor)
            valueForActor = self.actorMap.get(actor)
            print(valueForActor.get('fbLikes'))
            print(valueForActor.get('profitValues'))
            print(valueForActor.get('imdbScore'))
            
           
    def processDirectorData(self, directorName, directorFbLikes, movieEarnings, movieBudget, imdbScore):
        if(self.directorMap.__contains__(directorName)):
            valueMap = self.directorMap.get(directorName)
            if(directorFbLikes != ''):
                print(directorName)
                valueMap.get('fbLikes').append(float(directorFbLikes))
            else:
                valueMap.get('fbLikes').append(0.0)
            if((movieEarnings != '') and (movieBudget != '')):
                profit = (float(movieEarnings))/float(movieBudget)
            else:
                profit = 0.0
            valueMap.get('profitValues').append(profit)
            if(imdbScore != ''):
                valueMap.get('imdbScore').append(float(imdbScore))
            else:
                valueMap.get('imdbScore').append(0.0)
        else:
            valueMap = dict()
            #print(actorFbLikes)
            if(directorFbLikes != ''):
                valueMap['fbLikes'] = [float(directorFbLikes)]
            else:
                valueMap['fbLikes'] = 0.0
            if((movieEarnings != '') and (movieBudget != '')):
                profit = (float(movieEarnings))/float(movieBudget)
            else:
                profit = 0.0
            valueMap['profitValues'] = [profit]
            if(imdbScore != ''):
                valueMap['imdbScore'] = [float(imdbScore)]
            else:
                valueMap['imdbScore'] = 0.0
            self.directorMap[directorName] = valueMap
            
    def processDirectorMap(self):
        for director in self.directorMap.keys():
            valueMap = self.directorMap.get(director)
            noOfFbLikes = self.getTotal(valueMap.get('fbLikes'))
            totalProfit = self.getTotal(valueMap.get('profitValues'))
            totalScore = self.getTotal(valueMap.get('imdbScore'))
            valueMapFinal = dict()
            valueMapFinal['fbLikes'] = noOfFbLikes
            valueMapFinal['totalProfit'] = totalProfit
            valueMapFinal['totalScore'] = totalScore
            self.directorMapFinal[director] = valueMapFinal
            
    def writeDirectorDataToFile(self):
        with open('rating/directors_summary.csv', 'w') as csvfile:
            fieldnames = ['director_name', 'no_of_fb_likes', 'total_profit', 'total_imdb_score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for director in self.directorMapFinal.keys():
                valueMap = self.directorMapFinal.get(director)
                writer.writerow({'director_name': director, 'no_of_fb_likes': valueMap.get('fbLikes'), 'total_profit': valueMap.get('totalProfit'), 'total_imdb_score': valueMap.get('totalScore')})
                
    def processGenresData(self, genreName, movieFbLikes, movieEarnings, movieBudget, imdbScore):
        if(genreName != ''):
            genreArray = genreName.split('|')
            for genre in genreArray:
                if(self.genresMap.__contains__(genre)):
                    valueMap = self.genresMap.get(genre)
                    if(movieFbLikes != ''):
                        valueMap.get('fbLikes').append(float(movieFbLikes))
                    else:
                        valueMap.get('fbLikes').append(0.0)
                    if((movieEarnings != '') and (movieBudget != '')):
                        profit = (float(movieEarnings))/float(movieBudget)
                    else:
                        profit = 0.0
                    valueMap.get('profitValues').append(profit)
                    if(imdbScore != ''):
                        valueMap.get('imdbScore').append(float(imdbScore))
                    else:
                        valueMap.get('imdbScore').append(0.0)
                else:
                    valueMap = dict()
                    if(movieFbLikes != ''):
                        valueMap['fbLikes'] = [float(movieFbLikes)]
                    else:
                        valueMap['fbLikes'] = 0.0
                    if((movieEarnings != '') and (movieBudget != '')):
                        profit = (float(movieEarnings))/float(movieBudget)
                    else:
                        profit = 0.0
                    valueMap['profitValues'] = [profit]
                    if(imdbScore != ''):
                        valueMap['imdbScore'] = [float(imdbScore)]
                    else:
                        valueMap['imdbScore'] = 0.0
                    self.genresMap[genre] = valueMap
                    
    def processGenreMap(self):
        for genre in self.genresMap.keys():
            valueMap = self.genresMap.get(genre)
            noOfFbLikes = self.getTotal(valueMap.get('fbLikes'))
            totalProfit = self.getTotal(valueMap.get('profitValues'))
            totalScore = self.getTotal(valueMap.get('imdbScore'))
            valueMapFinal = dict()
            valueMapFinal['fbLikes'] = noOfFbLikes
            valueMapFinal['totalProfit'] = totalProfit
            valueMapFinal['totalScore'] = totalScore
            self.genresMapFinal[genre] = valueMapFinal
            
    def writeGenreDataToFile(self):
        with open('rating/genre_summary.csv', 'w') as csvfile:
            fieldnames = ['genre_name', 'no_of_fb_likes', 'total_profit', 'total_imdb_score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for genre in self.genresMapFinal.keys():
                valueMap = self.genresMapFinal.get(genre)
                writer.writerow({'genre_name': genre, 'no_of_fb_likes': valueMap.get('fbLikes'), 'total_profit': valueMap.get('totalProfit'), 'total_imdb_score': valueMap.get('totalScore')})
                
    def processMovieData(self, movieTitle, actorName1, actorName2, actorName3, directorName, genres, movieEarnings, movieBudget, imdbScore):
        if(movieTitle != ''):
            valueMap = dict()
            valueMap['actorName1'] = actorName1
            valueMap['actorName2'] = actorName2
            valueMap['actorName3'] = actorName3
            valueMap['directorName'] = directorName
            valueMap['genres'] = genres
            valueMap['movieEarnings'] = movieEarnings
            valueMap['movieBudget'] = movieBudget
            valueMap['imdbScore'] = imdbScore
            self.moviesMap[movieTitle] = valueMap
                    
    def writeMovieDataToFile(self):
        with open('rating/movie_summary.csv', 'w') as csvfile:
            fieldnames = ['movie_title', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name', 'genres', 'earnings', 'budget', 'imdb_score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for movie in self.moviesMap.keys():
                valueMap = self.moviesMap.get(movie)
                writer.writerow({'movie_title': movie, 'actor_1_name': valueMap.get('actorName1'), 'actor_2_name': valueMap.get('actorName2'), 'actor_3_name': valueMap.get('actorName3'), 'director_name': valueMap.get('directorName'), 'genres':valueMap.get('genres'), 'earnings': valueMap.get('movieEarnings'), 'budget': valueMap.get('movieBudget'),'imdb_score': valueMap.get('imdbScore')})
            