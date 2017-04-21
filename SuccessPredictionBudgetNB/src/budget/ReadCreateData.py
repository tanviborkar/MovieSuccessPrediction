'''
Created on Apr 17, 2017

@author: Tanvi Borkar
'''
from __future__ import division
from math import log
from array import *
import csv
import MySQLdb

class ReadCreateData(object):
    actorCountMap = dict()
    directorCountMap = dict()
    genreCountMap = dict()
    totalActorCount = array('d', [0.0, 0.0, 0.0])
    totalDirectorCount = array('d', [0.0, 0.0, 0.0])
    totalGenreCount = array('d', [0.0, 0.0, 0.0])
    totalClassProb = array('d', [0.0, 0.0, 0.0])
    
    def readData(self):
        #self.initializeTotalCountMap() 
        with open('budget/movie_metadata.csv', 'rt') as csvfile:
            columnNames = ['color', 'director_name', 'num_critic_for_reviews', 'duration', 'director_facebook_likes', 'actor_3_facebook_likes', 'actor_2_name', 'actor_1_facebook_likes', 'gross', 'genres', 'actor_1_name', 'movie_title', 'num_voted_users', 'cast_total_facebook_likes', 'actor_3_name', 'facenumber_in_poster', 'plot_keywords', 'movie_imdb_link', 'num_user_for_reviews', 'language', 'country', 'content_rating', 'budget', 'title_year', 'actor_2_facebook_likes', 'imdb_score', 'aspect_ratio', 'movie_facebook_likes']
            #columnNames = ['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name', 'genres', 'gross', 'budget', 'imdb_score']
            reader = csv.DictReader(csvfile, columnNames)
            for row in reader:
                #code for processing actor data
                if((row['actor_1_name'] != 'actor_1_name') & (row['gross']!='') & (row['budget']!='')):
                    label = self.classifyBudgetRatio(float(row['gross']), float(row['budget']))
                    if(row['actor_1_name']!=''):
                        self.processActorData(row['actor_1_name'], label)
                    if(row['actor_2_name']!=''):
                        self.processActorData(row['actor_2_name'], label)
                    if(row['actor_3_name']!=''):
                        self.processActorData(row['actor_3_name'], label)
                    if(row['director_name']!=''):
                        self.processDirectorData(row['director_name'], label)
                    if(row['genres']!=''):
                        self.processGenreData(row['genres'], label)
                        
                    self.totalClassProb[label] = self.totalClassProb[label] + 1
             
            self.findTotal()    
            self.findFrequency()  
            self.calculateLabelTotal()
            self.performDatabaseOperations()
            #print('Before total')
            #for total in self.totalCountMap.keys():
                #print('Key='+str(total)+' value='+str(self.totalCountMap.get(total)))
    
    def classifyBudgetRatio(self, earnings, budget):
        budgetRatio = earnings/budget
        if((budgetRatio>=0.0) & (budgetRatio<1.0)):
            return 0
        elif((budgetRatio>=1.0) & (budgetRatio<2.0)):
            return 1
        elif(budgetRatio>=2.0) :
            return 2
        else:
            return None
        
    def processActorData(self, actorName, label):
        if "'" in actorName:
            actorName = actorName.replace("'","")
            print(actorName)
        if(actorName in self.actorCountMap.keys()):
            actorValueMap = self.actorCountMap.get(actorName)
            ratingCount = actorValueMap.get(label);
            actorValueMap[label] = ratingCount + 1
        else:
            actorValueMap = dict()
            for i in range(0, 3):
                if i==label:
                    actorValueMap[label] = 1
                else:
                    actorValueMap[i] = 0
            self.actorCountMap[actorName] = actorValueMap
            
    def processDirectorData(self, directorName, label):
        if "'" in directorName:
            directorName = directorName.replace("'","")
            print(directorName)
        if(directorName in self.directorCountMap.keys()):
            directorValueMap = self.directorCountMap.get(directorName)
            ratingCount = directorValueMap.get(label);
            directorValueMap[label] = ratingCount + 1
        else:
            directorValueMap = dict()
            for i in range(0, 3):
                if i==label:
                    directorValueMap[label] = 1
                else:
                    directorValueMap[i] = 0
            self.directorCountMap[directorName] = directorValueMap
     
    def processGenreData(self, genreName, label):
        genreList = genreName.split('|')
        for genre in genreList:
            print(genre)
            if(genre in self.genreCountMap.keys()):
                genreValueMap = self.genreCountMap.get(genre)
                ratingCount = genreValueMap.get(label);
                genreValueMap[label] = ratingCount + 1
        else:
            genreValueMap = dict()
            for i in range(0, 3):
                if i==label:
                    genreValueMap[label] = 1
                else:
                    genreValueMap[i] = 0
            self.genreCountMap[genre] = genreValueMap
            
    def initializeTotalCountMap(self):
        for i in range(0, 3):
            self.totalCountMap[i] = 0
            self.totalActorCountMap[i] = 0
             
    def findTotal(self):
        for actor in self.actorCountMap.keys():
            actorValueMap = self.actorCountMap.get(actor)
            keyList = actorValueMap.keys()
            for key in keyList:
                sumCount = self.totalActorCount[key]
                sumCount = sumCount + actorValueMap.get(key)
                self.totalActorCount[key] = sumCount
                
        for director in self.directorCountMap.keys():
            directorValueMap = self.directorCountMap.get(director)
            keyList = directorValueMap.keys()
            for key in keyList:
                sumCount = self.totalDirectorCount[key]
                sumCount = sumCount + directorValueMap.get(key)
                self.totalDirectorCount[key] = sumCount
                
        for genre in self.genreCountMap.keys():
            genreValueMap = self.genreCountMap.get(genre)
            keyList = genreValueMap.keys()
            for key in keyList:
                sumCount = self.totalGenreCount[key]
                sumCount = sumCount + genreValueMap.get(key)
                self.totalGenreCount[key] = sumCount
    
    def findFrequency(self):
        for actor in self.actorCountMap.keys():
            actorValueMap = self.actorCountMap.get(actor)
            keyList = actorValueMap.keys()
            for key in keyList:    
                frequency = (log(actorValueMap.get(key) + 1))- (log((self.totalActorCount[key] + 3)))
                actorValueMap[key] = frequency
                
        for director in self.directorCountMap.keys():
            directorValueMap = self.directorCountMap.get(director)
            keyList = directorValueMap.keys()
            for key in keyList:    
                frequency = (log(directorValueMap.get(key) + 1))- (log((self.totalDirectorCount[key] + 3)))
                directorValueMap[key] = frequency
                
        for genre in self.genreCountMap.keys():
            genreValueMap = self.genreCountMap.get(genre)
            keyList = genreValueMap.keys()
            for key in keyList:    
                frequency = (log(genreValueMap.get(key) + 1))- (log((self.totalGenreCount[key] + 3)))
                genreValueMap[key] = frequency
                
    def calculateLabelTotal(self): 
        sumTotal = 0;
        for i in range(0, 3):
            sumTotal = sumTotal + self.totalClassProb[i]
        #print('Total Ratings '+str(sumTotal))
            
        for i in range(0, 3):
            frequency = (log(self.totalClassProb[i] + 1))- (log((sumTotal + 3)))
            self.totalClassProb[i] = frequency
            #print('Key '+str(keyRating)+' value= '+str(frequency))            
            
    def performDatabaseOperations(self):
        self.createDatabaseTables()
        self.insertActorBudgetFreq()
        self.insertDirectorBudgetFreq()
        self.insertGenreBudgetFreq()
        self.insertBudgetFreqData()
        
    def createDatabaseTables(self):
        # Open database connection
        dbConn = MySQLdb.connect("localhost","root","test123","projectdb" )

        # prepare a cursor object using cursor() method
        cursor = dbConn.cursor()

        # Drop table if it already exist using execute() method.
        cursor.execute("DROP TABLE IF EXISTS actor_budget")
        cursor.execute("DROP TABLE IF EXISTS director_budget")
        cursor.execute("DROP TABLE IF EXISTS genre_budget")
        cursor.execute("DROP TABLE IF EXISTS budget")

        # Create table as per requirement
        sqlQuery = """CREATE TABLE actor_budget (
         actor_name  CHAR(50) NOT NULL,
         budget_0 DECIMAL(25,20),  
         budget_1 DECIMAL(25,20),
         budget_2 DECIMAL(25,20))"""
         
        sqlQuery1 = """CREATE TABLE director_budget (
         director_name  CHAR(50) NOT NULL,
         budget_0 DECIMAL(25,20),  
         budget_1 DECIMAL(25,20),
         budget_2 DECIMAL(25,20))"""
         
        sqlQuery2 = """CREATE TABLE genre_budget (
         genre_name  CHAR(50) NOT NULL,
         budget_0 DECIMAL(25,20),  
         budget_1 DECIMAL(25,20),
         budget_2 DECIMAL(25,20))"""
         
        sqlQuery3 = """CREATE TABLE budget (
         budget_label INT NOT NULL,
         budget_freq DECIMAL(25,20))"""

        cursor.execute(sqlQuery)
        cursor.execute(sqlQuery1)
        cursor.execute(sqlQuery2)
        cursor.execute(sqlQuery3)

        # disconnect from server
        dbConn.close()
    
    def insertActorBudgetFreq(self):
        # Open database connection
        dbConn = MySQLdb.connect("localhost","root","test123","projectdb" )

        # prepare a cursor object using cursor() method
        cursor = dbConn.cursor()

        # Prepare SQL query to INSERT a record into the database.
        print('Inserting actor data')
        for actor in self.actorCountMap.keys():
            actorValueMap = self.actorCountMap.get(actor)
            #print('Rating 0 '+str(actorValueMap.get(0)))
            sql2 = "INSERT INTO actor_budget(actor_name, budget_0, budget_1, budget_2) \
            VALUES ('%s', '%s', '%s', '%s')" % \
            (actor, actorValueMap.get(0), actorValueMap.get(1), actorValueMap.get(2))
            try:
                # Execute the SQL command
                cursor.execute(sql2)
                print('Data Inserted')
                # Commit your changes in the database
                dbConn.commit()
            except:
                # Rollback in case there is any error
                print('Exception occurred')
                dbConn.rollback()
            
        # disconnect from server
        dbConn.close()
        
    def insertDirectorBudgetFreq(self):
        # Open database connection
        dbConn = MySQLdb.connect("localhost","root","test123","projectdb" )

        # prepare a cursor object using cursor() method
        cursor = dbConn.cursor()

        # Prepare SQL query to INSERT a record into the database.
        print('Inserting actor data')
        for director in self.directorCountMap.keys():
            directorValueMap = self.directorCountMap.get(director)
            #print('Rating 0 '+str(actorValueMap.get(0)))
            sql3 = "INSERT INTO director_budget(director_name, budget_0, budget_1, budget_2) \
            VALUES ('%s', '%s', '%s', '%s')" % \
            (director, directorValueMap.get(0), directorValueMap.get(1), directorValueMap.get(2))
            try:
                # Execute the SQL command
                cursor.execute(sql3)
                print('Data Inserted')
                # Commit your changes in the database
                dbConn.commit()
            except:
                # Rollback in case there is any error
                print('Exception occurred')
                dbConn.rollback()
            
        # disconnect from server
        dbConn.close()
        
    def insertGenreBudgetFreq(self):
        # Open database connection
        dbConn = MySQLdb.connect("localhost","root","test123","projectdb" )

        # prepare a cursor object using cursor() method
        cursor = dbConn.cursor()

        # Prepare SQL query to INSERT a record into the database.
        print('Inserting actor data')
        for genre in self.genreCountMap.keys():
            genreValueMap = self.genreCountMap.get(genre)
            #print('Rating 0 '+str(actorValueMap.get(0)))
            sql4 = "INSERT INTO genre_budget(genre_name, budget_0, budget_1, budget_2) \
            VALUES ('%s', '%s', '%s', '%s')" % \
            (genre, genreValueMap.get(0), genreValueMap.get(1), genreValueMap.get(2))
            try:
                # Execute the SQL command
                cursor.execute(sql4)
                print('Data Inserted')
                # Commit your changes in the database
                dbConn.commit()
            except:
                # Rollback in case there is any error
                print('Exception occurred')
                dbConn.rollback()
            
        # disconnect from server
        dbConn.close()
        
    def insertBudgetFreqData(self):
        # Open database connection
        dbConn = MySQLdb.connect("localhost","root","test123","projectdb" )

        # prepare a cursor object using cursor() method
        cursor = dbConn.cursor()

        for i in range(0, 3):
            print(self.totalClassProb[i])
            sql1 = "INSERT INTO budget(budget_label, \
            budget_freq) \
            VALUES ('%d', '%s')" % \
            (i, self.totalClassProb[i])
        
            try:
                # Execute the SQL command
                cursor.execute(sql1)
                # Commit your changes in the database
                dbConn.commit()
            except:
                # Rollback in case there is any error
                print('Exception occurred')
                dbConn.rollback()

        # disconnect from server
        dbConn.close()
        