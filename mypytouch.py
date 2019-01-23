#!/usr/bin/python2
import sys
print sys.argv[0]
print sys.argv[1]
'''
name=sys.argv[1]
f=open(name,'w')
f.close()


#for multiple file create
list_name=sys.argv[1:]
for i in list_name:
        f=open(i,'w')
        f.close()
'''
#repition file not alow and data also save
name=sys.argv[1:]
for i in name:
        f=open(i,'a+')
        f.close()

