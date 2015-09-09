'''
Created on Nov 10, 2012

@author: Laura
'''
from Operand import Operands
from Memory import MemoryS

class IdS(Operands):
    '''
    classdocs
    '''

    def __init__(self, ch):
        '''
        Constructor
        '''
        self.ch= ch
        
    def getValue(self):
        #return MemoryS.fetch(self.ch,self.ch)
        return int(MemoryS.fetch(self, self.ch))
        
    def getChar(self):
        return self.ch