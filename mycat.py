#!/usr/bin/python
import sys
name=sys.argv[1]
f=open(name,'r+')
print f.read()
f.close()  


#for multiple files views
name=sys.argv[1:]
for i in name:
        f=open(i,'r+')
        print f.read()
        f.close()
        
