'''
Created on Apr 20, 2017

@author: Tanvi Borkar
'''

class Director(object):
    directorName = ''
    directorFbLikes = 0.0
    directorTotalProfits = 0.0
    directorIMDBScore = 0.0
    
    def getDirectorName(self):
        return self.directorName
    
    def setDirectorName(self, directorName):
        self.directorName = directorName
        
    def getDirectorFbLikes(self):
        return self.directorFbLikes
    
    def setDirectorFbLikes(self, directorFbLikes):
        self.directorFbLikes = directorFbLikes
        
    def getDirectorTotalProfits(self):
        return self.directorTotalProfits
    
    def setDirectorTotalProfits(self, directorTotalProfits):
        self.directorTotalProfits = directorTotalProfits
        
    def getDirectorIMDBScore(self):
        return self.directorIMDBScore
    
    def setDirectorIMDBScore(self, directorIMDBScore):
        self.directorIMDBScore = directorIMDBScore