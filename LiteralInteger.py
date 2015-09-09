'''
Created on Nov 13, 2012

@author: Laura
'''
from Operand import Operands

class LiteralIntegers(Operands):
    '''
    classdocs
    '''


    def __init__(self, value):
        '''
        Constructor
        '''
        self.value = value
        
    def getValue(self):
        return int(self.value)
        