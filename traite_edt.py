#!/usr/bin/python3

import csv
cpt=0
module=[]
grp=[]
staff=[]
salle=[]
#with open('essai.txt', newline='') as csvfile:
with open('edt.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if cpt==0:
            if len(row)>14:
                if row[0]!='' and row[13]=="T_GEII T25":
                    print(row)
                    cpt+=1
        elif cpt==1:
            print(row[21])
            module.append(row[21])
            cpt+=1
        elif cpt==2:
            print(row[21])
            grp.append(row[21])
            cpt+=1
        elif cpt==3:
            print(row[21])
            staff.append(row[21])
            cpt+=1
        elif cpt==4:
            salle.append(row[21])
            print(row[21])
            cpt=0

for i in range(len(module)):
    print(module[i],grp[i])
            
       # print(type(row))
##        for w in row:
###        if row[1]=="215688":
##            print (w)
##        print(' / '.join(row))
##        print("_____")
        #print( row.reverse() )
##        for w in row:
##            print(w)
