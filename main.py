# INITIAL CODE
import os
from csv import reader
import lib1 as library

opened_file1 = open('./AppleStore.csv')
opened_file2 = open('./googleplaystore.csv')
readed_file1 = list(reader(opened_file1))
readed_file2 = list(reader(opened_file2))
a,b= library.fix2(readed_file1,True,False)
c,d= library.fix2(readed_file2,True,True)
#b = fix1(readed_file1,True)
#print(a)

#print('appstore counts:',len(readed_file1[1:]))

print('Appstore net amount of unique apps',len(a))
print('Appstore,english:',len(b))
print('net amount of free apps is Appstore',len(library.findingFreeApps(a)))
print('Android net amount of unique apps:',len(c))
print('Android,english:',len(d))
print('net amount of free apps in GooglePlay',len(library.findingFreeApps(d)))
#print(explore_data(readed_file1,1,3,True))
#here I am testing githubing