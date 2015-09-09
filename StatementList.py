'''
Created on Nov 10, 2012

@author: Laura
'''

class StatementLists(object):
    '''
    classdocs
        '''
    


    def __init__(self):
        '''
        Constructor
        '''
        self.list = []
        
    def add(self, statement):
        self.list.append(statement)
            
    def getStatementLists(self):
        for self.i in range (0, len(self.list)):
            self.list[self.i].getStatement()
            
            