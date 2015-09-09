'''
Created on Nov 10, 2012

@author: Laura
'''

class Lexical_Analyzers(object):
    '''
    classdocs
    '''
    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.count = 0
        self.array = []
        self.file = open(fileName, 'r')
        file_content = self.file.read()
        for token in file_content.split():
            self.array.append(token)
        self.file.close       
    
    def lookAhead(self):
        if self.count < len(self.array):
            return self.array[self.count]
        

    def getToken(self):
        token = self.array[self.count]
        self.count += 1
        return token
