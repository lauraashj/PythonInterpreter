'''
Created on Nov 13, 2012

@author: Laura
'''

class LTExpressions(object):
    '''
    classdocs
    '''


    def __init__(self, op1, op2):
        '''
        Constructor
        '''
        self.op1 = op1
        self.op2 = op2
        
    def getBool(self):
        return self.op1.getValue() < self.op2.getValue()