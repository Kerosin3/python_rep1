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
print('Android net amount of unique apps:',len(c))
print('Android,english:',len(d))
free_apps_adnroid = (library.findingFreeApps(c,False,True))
free_apps_ios = (library.findingFreeApps(a,False,False))
print('net amount of free apps in GooglePlay',len(free_apps_adnroid))
print('net amount of free apps is Appstore',len(free_apps_ios))
(x,y,z)=library.getColomn(free_apps_adnroid,9,False,True) # 9 - number of genre's colomn
#(_,_,e)=library.getColomn(free_apps_ios,11,False,isAndroid=False) # 
#print(z[1])
table_sortedAndroid = sorted(z, reverse = True)
#print(table_sortedAndroid)
#table_sortediOs = sorted(e, reverse = True)
#library.GenreInstallationsFrequences(readed_file2)
#print(table_sortedAndroid)
#print(table_sortediOs)
#t0 = library.installsFreq(free_apps_adnroid)
#print(sorted(t0, reverse = True))
#t1 = table_sortedAndroid = sorted(t0, reverse = True)
#print(t0)
#print(table_sorted)
#print(x['FR Tides'])
#print('non-free apps in Android:', free_apps_adnroid)
#print('non-free apps in iOs:', free_apps_ios)
#print(explore_data(readed_file1,1,3,True))
#here I am testing githubing
#puhttp://www.deanbodenham.com/learn/using-git-to-sync-different-computers.html