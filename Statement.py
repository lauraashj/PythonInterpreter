'''
Created on Nov 13, 2012

@author: Laura
'''
import abc

class Statements(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    
    @abc.abstractmethod
    def getStatement(self):
        return