'''
Created on Apr 18, 2017

@author: Tanvi Borkar
'''
from array import *
import MySQLdb

class PredictMovieBudgetNB(object):
    actorFreqMap = dict(); 
    directorFreqMap = dict();
    genreFreqMap = dict();
    budgetFreq = array('d', [0.0, 0.0, 0.0])
    scoreBudget = array('d', [0.0, 0.0, 0.0])
    
    def __init__(self):
        self.extractBudgetFreq()
        
    def calculateRating(self, actor1Name, actor2Name, actor3Name, directorName, genres):
        print('Actor 1: '+actor1Name+' Actor 2: '+actor2Name+' Actor 3: '+actor3Name)
        self.extractActorBudget(actor1Name, actor2Name, actor3Name)
        
        if(directorName!=''):
            directorName = directorName.replace("'","")
            self.extractDirectorBudget(directorName)
        
        if(genres != ''):
            genreNameList = genres.split('|') 
            self.extractGenreBudget(genreNameList)
            
        self.computeScoreForRating()
        predictedLabel = self.computeMaxScore()
        print('Predicted label is '+str(predictedLabel))
        self.reinitializeGlobalValues()
        return predictedLabel
        
    def extractActorBudget(self, actor1Name, actor2Name, actor3Name):
        # Open database connection
        dbConn = MySQLdb.connect("localhost","root","test123","projectdb" )

        # prepare a cursor object using cursor() method
        cursor = dbConn.cursor()

        # Prepare SQL query to INSERT a record into the database.
        if(actor1Name!=''):
            actor1Name = actor1Name.replace("'","")
            sql1 = "SELECT * FROM actor_budget \
            WHERE actor_name = '%s'" % (actor1Name)
            try:
                # Execute the SQL command
                cursor.execute(sql1)
                # Fetch all the rows in a list of lists.
                result = cursor.fetchone()
                if result!=None:
                    actorArray = array('d', [0.0, 0.0, 0.0])
                    actorArray[0] = result[1]
                    actorArray[1] = result[2]
                    actorArray[2] = result[3]
                    self.actorFreqMap[result[0]] = actorArray
                    # Now print fetched result
                    #print('Actor Name '+result[0])
            except:
                print "Error: unable to fecth data"
    
        if(actor2Name!=''):
            actor2Name = actor2Name.replace("'","")
            sql2 = "SELECT * FROM actor_budget \
            WHERE actor_name = '%s'" % (actor2Name)
            try:
                # Execute the SQL command
                cursor.execute(sql2)
                # Fetch all the rows in a list of lists.
                result = cursor.fetchone()
                if result!=None:
                    actorArray = array('d', [0.0, 0.0, 0.0])
                    actorArray[0] = result[1]
                    actorArray[1] = result[2]
                    actorArray[2] = result[3]
                    self.actorFreqMap[result[0]] = actorArray
                    # Now print fetched result
                    print('Actor Name '+result[0])
            
            except:
                print "Error: unable to fecth data"
              
        if(actor3Name!=''):
            actor3Name = actor3Name.replace("'","")
            sql3 = "SELECT * FROM actor_budget \
            WHERE actor_name = '%s'" % (actor3Name)
            try:
                # Execute the SQL command
                cursor.execute(sql3)
                # Fetch all the rows in a list of lists.
                result = cursor.fetchone()
                if result!=None:
                    actorArray = array('d', [0.0, 0.0, 0.0])
                    actorArray[0] = result[1]
                    actorArray[1] = result[2]
                    actorArray[2] = result[3]
                    self.actorFreqMap[result[0]] = actorArray
                    # Now print fetched result
                    print('Actor Name '+result[0])
            except:
                print "Error: unable to fecth data"

        # disconnect from server
        dbConn.close()
        
    def extractDirectorBudget(self, directorName):
        # Open database connection
        dbConn = MySQLdb.connect("localhost","root","test123","projectdb" )

        # prepare a cursor object using cursor() method
        cursor = dbConn.cursor()

        # Prepare SQL query to INSERT a record into the database.
        if(directorName!=''):
            sql1 = "SELECT * FROM director_budget \
            WHERE director_name = '%s'" % (directorName)
            try:
                # Execute the SQL command
                cursor.execute(sql1)
                # Fetch all the rows in a list of lists.
                result = cursor.fetchone()
                if result!=None:
                    directorArray = array('d', [0.0, 0.0, 0.0])
                    directorArray[0] = result[1]
                    directorArray[1] = result[2]
                    directorArray[2] = result[3]
                    self.directorFreqMap[result[0]] = directorArray
                    # Now print fetched result
                    #print('Actor Name '+result[0])
            except:
                print "Error: unable to fecth data"

        # disconnect from server
        dbConn.close()
        
    def extractGenreBudget(self, genresList):
        # Open database connection
        dbConn = MySQLdb.connect("localhost","root","test123","projectdb" )

        # prepare a cursor object using cursor() method
        cursor = dbConn.cursor()

        # Prepare SQL query to INSERT a record into the database.
        for genre in genresList:
            sql1 = "SELECT * FROM genre_budget \
            WHERE genre_name = '%s'" % (genre)
            try:
                # Execute the SQL command
                cursor.execute(sql1)
                # Fetch all the rows in a list of lists.
                result = cursor.fetchone()
                if result!=None:
                    genreArray = array('d', [0.0, 0.0, 0.0])
                    genreArray[0] = result[1]
                    genreArray[1] = result[2]
                    genreArray[2] = result[3]
                    self.genreFreqMap[result[0]] = genreArray
                    # Now print fetched result
                    #print('Actor Name '+result[0])
            except:
                print "Error: unable to fecth data"

        # disconnect from server
        dbConn.close()
        
    def extractBudgetFreq(self):
        # Open database connection
        dbConn = MySQLdb.connect("localhost","root","test123","projectdb" )

        # prepare a cursor object using cursor() method
        cursor = dbConn.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql1 = "SELECT * FROM budget"
        try:
            # Execute the SQL command
            cursor.execute(sql1)
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                self.budgetFreq[row[0]] = row[1]
                #print(row[1])
        except:
            print "Error: unable to fetch data"
            
        # disconnect from server
        dbConn.close()
        
    def computeScoreForRating(self):
        for actor in self.actorFreqMap.keys():
            valueMap = self.actorFreqMap.get(actor)
            for i in range(0, 3):
                self.scoreBudget[i] = valueMap[i] + self.scoreBudget[i]
        
        for director in self.directorFreqMap.keys():
            valueMap = self.directorFreqMap.get(director)
            for i in range(0, 3):
                self.scoreBudget[i] = valueMap[i] + self.scoreBudget[i]
                
        for genre in self.genreFreqMap.keys():
            valueMap = self.genreFreqMap.get(genre)
            for i in range(0, 3):
                self.scoreBudget[i] = valueMap[i] + self.scoreBudget[i]
            
        for i in range(0, 3):
            self.scoreBudget[i] = self.scoreBudget[i] + self.budgetFreq[i]

    def computeMaxScore(self):
        max = self.scoreBudget[0]
        indexList = []
        #maxIndex = 0
        for i in range(1,3):
            #print('Max Value '+str(max))
            #print('Score Rating '+str(i)+ ' is '+str(self.scoreBudget[i]))
            if(max<self.scoreBudget[i]):
                max = self.scoreBudget[i]
                #maxIndex = i
        for i in range(0,3):
            if(max == self.scoreBudget[i]):
                indexList.append(i) 
                
        return indexList
    
    def reinitializeGlobalValues(self):
        self.actorFreqMap.clear()
        self.directorFreqMap.clear()
        self.genreFreqMap.clear()
        for i in range(0, 3):
            self.scoreBudget[i] = 0.0