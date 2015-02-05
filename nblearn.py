import sys
import os
import json
import time
files=sys.argv

class Nblearn:
    wordlist=[]
    def __init__(self):
        pass
                
    def countwords(self):
        totalset=set()
        global classlist
        classlist=[]
        for line in open(str(files[1]),"r"):
            words=line.split()
            for word in words:
                if words[0] not in classlist:
                    classlist.append(words[0])
                totalset.add(word)
        return len(totalset)
        
    def countclass(self,theclass):
        total=0
        totalwc=0
        for line in open(str(files[1]),"r"):
            words=line.split()
            if words[0]==theclass:
                    total+=1
            for word in words:
                if word in classlist:
                    continue
                elif words[0]==theclass:
                    totalwc+=1
                else:
                    continue
        return totalwc,total
    
    
    def totalmails(self):
        total=0
        for line in open(str(files[1]),"r"):
            total=total+1
        return total
    
    def frequency(self):
        dicword={}
        for i in range(len(classlist)):
            dicword[classlist[i]]={}
        for line in open(str(files[1]),"r"):
            words=line.split()
            for word in words:
                if word in classlist:
                    continue
                else:
                    for i in range(len(classlist)):
                        if words[0]==classlist[i]:
                            try:
                                dicword[classlist[i]][word]+=1
                            except KeyError:
                                dicword[classlist[i]][word]=1
                        else:
                            continue
                        
        for i in range(len(classlist)):
            for word in dicword[classlist[i]]:
                try:
                    if word not in dicword[classlist[i+1]]:
                        dicword[classlist[i+1]][word]=0
                    else:
                        continue
                except IndexError:
                    if word not in dicword[classlist[i-1]]:
                        dicword[classlist[i-1]][word]=0
                    else:
                        continue
        return dicword
    
    
    def probability(self):
        probdic={}
        for i in range(len(classlist)):
            probdic[classlist[i]]={}
            for word in dicword[classlist[i]].keys():
                probdic[classlist[i]][word]=(dicword[classlist[i]][word]+1)/float((wcount[classlist[i]])+vocab+1)
        return probdic
    
    def modelfile(self):
        f=open(str(files[2]),"w+")
        encode=json.dumps(classp)
        f.write(encode+"\n")
        encode=json.dumps(dicwordp)
        f.write(encode)
        f.close()
        
if __name__== '__main__':
    c=Nblearn()
    vocab=c.countwords()
    dicword=c.frequency()
    mailcount={}
    wcount={}
    classp={}
    for i in range(len(classlist)):
        wcount[classlist[i]],mailcount[classlist[i]]=c.countclass(classlist[i])
    totalmails=c.totalmails()
    dicwordp=c.probability()
    for i in range(len(classlist)):
        classp[classlist[i]]=mailcount[classlist[i]]/float(totalmails)
    c.modelfile()
    
    
    
    
    
    
