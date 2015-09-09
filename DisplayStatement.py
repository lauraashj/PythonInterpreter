'''
Created on Nov 13, 2012

@author: Laura
'''

from Statement import Statements

class DisplayStatements(Statements):
    '''
    classdocs
    '''

    def __init__(self, var):
        '''
        Constructor
        '''
        self.var = var
    def getStatement(self):
        print (repr(self.var.getValue()))