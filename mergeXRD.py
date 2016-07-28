import re
import os

def mystyle(x,y):
    if x=='ocv.txt':
        return -1
    elif not x[1] in ['1','2','3','4','5','6','7','8','9','0']:
            if x[0]<y[0]:
                return -1
            elif (x[0]>y[0]):
                return 1
    else:
        if x[:2]<y[:2]:
            return -1
        elif x[:2]>y[:2]:
            return 1
    return 0

def fuc(x):
    if x[:3]>'99':
        return 0
    else:
        try:
            return int(x[:2])
        except:
            return int(x[0])
            
def delFirstLine(fileList):
    for i in fileList:
        line=i.readline()
        if len(line)>20:
            

tag=1
fn=open("all",'w')
fo=[]
f=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.txt']
print(f)
fx=sorted(f,key=lambda a: fuc(a))

for t in fx:
    print(t)
    fo.append(open(t,'r'))
    
    
while tag:
    for i in fo:
        #i.readline()
        #for line in i.readline():
        line=i.readline()
        if line:
            fn.write('\t'.join(line.split())+'\t')
        else:
            tag=0
    fn.write('\n')

for i in fo:
    i.close()
fn.close()