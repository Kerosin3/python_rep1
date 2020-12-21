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
print('appstore counts:',len(readed_file1[1:]))
print('Appstore',len(a))
print('Appstore,english:',len(b))
print('Android:',len(c))
print('Android,english:',len(d))
#print(explore_data(readed_file1,1,3,True))