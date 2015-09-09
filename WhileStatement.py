'''
Created on Nov 10, 2012

@author: Laura
'''
from Statement import Statements

class WhileStatements(Statements):
    '''
    classdocs
    '''
    def __init__(self, expr, statementList):
        self.expr = expr
        self.statementList = statementList
        
    def getStatement(self):
        while self.expr.getBool():
            self.statementList.getStatementLists()