'''
Created on Nov 13, 2012

@author: Laura
'''

class Programs(object):
    '''
    classdocs
    '''


    def __init__(self, statementList):
        '''
        Constructor
        '''
        self.statementList = statementList
    
    def start_program(self):
        self.statementList.getStatementLists()
        