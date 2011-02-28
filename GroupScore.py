'''
Created on Jun 29, 2010

@author: Frank Yang
'''

import random 

class Team(object):
    '''
    classdocs
    '''
    
    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.opponents = []
        self.score = 0
        
    def play(self, t):
        if (t==self): return
        if (t in self.opponents):
            return
        self.opponents.append(t)
        t.opponents.append(self)
        r = random.randint(1, 3)
        if (r==1):
            #win
            #print "%c win %c" % (self.name, t.name)
            self.score+=3
        elif (r==2):
            #even
            #print "%c even %c" % (self.name, t.name)
            self.score+=1
            t.score+=1
        elif (r==3):
            #lose
            #print "%c lose %c" % (self.name, t.name)
            t.score+=3
        else:
            raise "Not defined"
            
            
def groupGame():
    g = []
    groupsize = 4 
    for i in range(groupsize):
        g.append(Team(i+ord("A")))
    for a in g:
        for b in g:
            a.play(b)
    s = []            
    for a in g:
        #print "%c : %i" % (a.name, a.score)        
        s.append(a.score)
    s.sort(None, None, True)
    return s
        
if __name__=="__main__":
    all = []
    frequency = {}
    test = 100000
    for i in range(test):
        s = groupGame()
        if s not in all:
            frequency[str(s)] = 0
            all.append(s)
        else:
            frequency[str(s)]+=1 
            
    all.sort(None, None, True)
    print len(all)
    for x in all:
        print str(x) + " " + str(sum(x)) + " " + str(frequency[str(x)]*100.0/test)+"%"

    totals = set()
    for x in all:
         totals.add(sum(x))
    print totals
    