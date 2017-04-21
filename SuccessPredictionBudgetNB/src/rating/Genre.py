'''
Created on Apr 20, 2017

@author: Tanvi Borkar
'''

class Genre(object):
    genreName = ''
    genreFbLikes = 0.0
    genreTotalProfits = 0.0
    genreIMDBScore = 0.0
    
    def getGenre(self):
        return self.genreName
    
    def setGenre(self, genreName):
        self.genreName = genreName
        
    def getGenreFbLikes(self):
        return self.genreFbLikes
    
    def setGenreFbLikes(self, genreFbLikes):
        self.genreFbLikes = genreFbLikes
        
    def getGenreTotalProfits(self):
        return self.genreTotalProfits
    
    def setGenreTotalProfits(self, genreTotalProfits):
        self.genreTotalProfits = genreTotalProfits
        
    def getGenreIMDBScore(self):
        return self.genreIMDBScore
    
    def setGenreIMDBScore(self, genreIMDBScore):
        self.genreIMDBScore = genreIMDBScore