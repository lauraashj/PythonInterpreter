'''
Created on Nov 13, 2012

@author: Laura
'''


class MemoryS(object):
    '''
    classdocs
    '''
    mem = [0]*26
    
    def __init__(self):
        '''
        Constructor
        '''
    def fetch(self, ch):
        #return MemoryS.mem[ord(self) - 97]
        #return self.mem[ord(ch)-97]
        return MemoryS.mem[ord(ch)-97]
    
    # should use self
        
    def store(self, ch, value):
        #a is 97, z is 122        
        MemoryS.mem[ord(ch)-97] = value   
    
