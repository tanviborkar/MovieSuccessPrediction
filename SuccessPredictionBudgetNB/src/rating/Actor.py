'''
Created on Apr 20, 2017

@author: Tanvi Borkar
'''

class Actor(object):
    actorName = ''
    actorFbLikes = 0.0
    actorTotalProfits = 0.0
    actorIMDBScore = 0.0
    
    def getActorName(self):
        return self.actorName
    
    def setActorName(self, actorName):
        self.actorName = actorName
        
    def getActorFbLikes(self):
        return self.actorFbLikes
    
    def setActorFbLikes(self, actorFbLikes):
        self.actorFbLikes = actorFbLikes
        
    def getActorTotalProfits(self):
        return self.actorTotalProfits
    
    def setActorTotalProfits(self, actorTotalProfits):
        self.actorTotalProfits = actorTotalProfits
        
    def getActorIMDBScore(self):
        return self.actorIMDBScore
    
    def setActorIMDBScore(self, actorIMDBScore):
        self.actorIMDBScore = actorIMDBScore