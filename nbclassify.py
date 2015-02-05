import json
import os
import sys
import math
import ast
files=sys.argv

class Classifier:
    def __init__(self):
        pass
        
    def readmodelfile(self):
        i=1
        f=open(files[1],"r")
        for line in f:
            worddicp=json.loads(line)
            if i==1:
                classp=worddicp
                i+=1
        return worddicp,classp
        
                
    def calcprob(self):
        prob={}
        for line in open(str(files[2]),"r",errors='ignore'): 
            words=line.split()
            for key in learndic:
                prob[key]=0
                prob[key]+=math.log(classprob[key])
                for word in words:
                    try:
                        prob[key]+=math.log(learndic[key][word])
                    except KeyError:
                        continue
            maxx=-1000000
            for key in prob:
                if prob[key]>maxx:
                    maxx=prob[key]
                    out=key
            
            print(out)
        
if __name__== '__main__':
    c=Classifier()
    learndic,classprob=c.readmodelfile()
    c.calcprob()
        
            


