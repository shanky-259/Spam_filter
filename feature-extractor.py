#!/usr/bin/env python
import os
import sys
files=sys.argv
def arrangewords():
        f=open(str(files[2]),"w+")
        for file in sorted(os.listdir(files[1])):
            if file!=".DS_Store":     
                f.write(file[:-10]+" ")
                f1=open(files[1]+"/"+file,"r",errors='ignore')
                content=f1.read()
                oneline=content.replace("\n","")
                f.write(oneline+"\n")
                
arrangewords()

