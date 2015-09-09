'''
Created on Nov 10, 2012

@author: Laura
'''
from Lexical_Analyzer import Lexical_Analyzers 
from ParserException import ParserExceptions
from StatementList import StatementLists
from AssignmentStatement import AssignmentStatements
from ifStatement import ifStatements
from WhileStatement import WhileStatements
from Id import IdS
from DisplayStatement import DisplayStatements
from LiteralInteger import LiteralIntegers
from NEExpression import NEExpressions
from EQExpression import EQExpressions
from AddExpression import AddExpressions
from SubExpression import SubExpressions
from MulExpression import MulExpressions
from DivExpression import DivExpressions
from LTExpression import LTExpressions
from LEExpression import LEExpressions
from GTExpression import GTExpressions
from GEExpression import GEExpressions
from UnaryExpression import UnaryExpressions
from Program import Programs

class Parsers(object):    

    def __init__(self, filename):
        self.lex = Lexical_Analyzers(filename)
        
    def parse(self):         
        self.match('main')
        self.match ('(')
        self.match (')')    
        statementList = self.getStatementList()
        return Programs(statementList)
    
    def match(self, expected):
        token = self.lex.getToken()
        if token != expected:         
            raise ParserExceptions ("Match Error")
        
    def getStatementList(self):
        statementList = StatementLists()
        statement = self.getStatement()
        statementList.add(statement)
        token = self.lex.lookAhead()
        while token == ";" :
            self.match(";")
            statement = self.getStatement()
            statementList.add(statement)
            token = self.lex.lookAhead()
        return statementList
            
    def getStatement(self):
        token = self.lex.lookAhead()
        if token == "if":
            stmt = self.getIfStatement()
        elif token == "while":
            stmt = self.getWhileStatement()
        elif token == "display":
            stmt = self.getDisplayStatement()
        else:
            stmt = self.getAssignmentStatement()
            
        return stmt
    
    def getIfStatement(self):
        self.match ('if')
        expr = self.getBooleanExpression()
        self.match('then')
        stmt1 = self.getStatementList()
        self.match('else')
        stmt2 = self.getStatementList()
        self.match('end')
        return ifStatements(expr, stmt1, stmt2)
    
    def getWhileStatement(self):
        
        self.match('while')
        expr = self.getBooleanExpression()
        self.match('do')
        stmt = self.getStatementList()
        self.match('end')
        return WhileStatements(expr,stmt)
        

    def getId(self):
        token = self.lex.getToken()
        if len(token)!= 1:
            raise ParserExceptions ("id expected")
        return IdS (token)
    
    
    def getDisplayStatement(self):
        self.match('display')
        self.match('(')
        var = self.getId()
        self.match(')')
        return DisplayStatements(var)
        
    def getAssignmentStatement(self):
        var = self.getId()
        self.match('<-')
        expr = self.getArithmeticExpression()
        return AssignmentStatements(var, expr)
    
    def getArithmeticExpression (self):
        token = self.lex.lookAhead()
        if self.isValidArithmeticOp(token):
            op = self.getArithmeticOperator()
            op1 = self.getOperand()
            op2 = self.getOperand()
            expr = self.createArithmeticExpression(op, op1, op2)
        else:
            op3 = self.getOperand()
            expr = UnaryExpressions(op3)
            
        return expr
    
    def isValidArithmeticOp(self, token):
        
        return token == '+' or token =='-' or token == '*' or token == '/'
    
        
    def createArithmeticExpression(self,op, op1, op2):
        if op == 'AddExpressions':            
            expr = AddExpressions(op1, op2)
        elif op == 'SubExpressions':
            expr = SubExpressions(op1,op2)
        elif op == 'MulExpressions':
            expr = MulExpressions(op1,op2)
        elif op == 'DivExpressions':
            expr = DivExpressions(op1, op2)
        else:
            raise ParserExceptions ("operator expected")
        return expr
            
    def getArithmeticOperator(self):
        token = self.lex.getToken()
        if token == "+":            
            op = 'AddExpressions'
        elif token == "-":
            op = 'SubExpressions'
        elif token == "*":
            op = 'MulExpressions'
        elif token == "/":
            op = 'DivExpressions'
        else:
            raise ParserExceptions ("operator expected")
        return op
    
    def getBooleanExpression (self):
        op = self.getRelativeOp()
        op1 = self.getOperand()
        op2 = self.getOperand()
        return self.createBooleanExpression(op, op1, op2)
    
    def getRelativeOp(self):
        token = self.lex.getToken()
        if token == "<":            
            op = 'LTExpressions'
        elif token == "<=":
            op = 'LEExpressions'
        elif token == ">":            
            op = 'GTExpressions'
        elif token == ">=":
            op = 'GEExpressions'
        elif token == "=":
            op = 'EQExpressions'
        elif token == "/=":            
            op = 'NEExpressions'
        return op

    def createBooleanExpression(self, op, op1, op2):
        if op == 'LTExpressions':            
            expr = LTExpressions(op1, op2)
        elif op == 'LEExpressions':
            expr = LEExpressions(op1, op2)
        elif op == 'GTExpressions':            
            expr = GTExpressions(op1, op2)
        elif op == 'GEExpressions':
            expr = GEExpressions(op1, op2)
        elif op == 'EQExpressions':
            expr = EQExpressions(op1, op2)
        elif op == 'NEExpressions':            
            expr = NEExpressions(op1, op2)
        else:
            raise ParserExceptions ("relative operator expected")
        return expr
    
    def getOperand(self):
            token = self.lex.lookAhead()
            if token.isdigit():
                op = self.getLiteralInteger()
            elif len(token)== 0:
                
                # needs to be exactly 1
                
                raise ParserExceptions ("operand Expected")
            else:
                op = self.getId()
            return op
        
    def getLiteralInteger(self):
        token = self.lex.getToken() 
        return LiteralIntegers(token)
                
    
