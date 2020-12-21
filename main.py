# INITIAL CODE
import os
from csv import reader
entries = os.listdir('.')
#print(entries)
def open_dataset(file_name='AppleStore.csv',has_row=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    if  has_row: #true
        return data[0],data[1:]
    #data = data[1:]
    return data[1:]
def extractCol(data,numb):
    summ=0
    n=0
    for item in data:
        summ+=float(item[numb])
        n+=1
    return numb/n    

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
def checkData(dataset):
    collomn = 0
    list_names_uniques = []
    list_names_dublicates = []
    for piece in dataset:
        if piece[collomn] in list_names_uniques:
            list_names_dublicates.append(piece[collomn])
        else:
            list_names_uniques.append(piece[collomn])
    return list_names_dublicates
def fix1(dataset,header=True):
    if header:
        dataset = dataset[1:]
    list_b = {}
    review_rating = 0
    for app in dataset:
        review_rating = float(app[3])
        name = app[0]
        if name in dataset and review_rating > list_b[name]:
            list_b[name] = review_rating
        elif name not in dataset:
            list_b[name]=review_rating
    return list_b
def fix2(dataset,header=True):
    base = fix1(dataset,header=True)
    final_list= []
    english_list=[]
    added_list = []
    if header:
        dataset=dataset[1:]
    for app in dataset:
        name = app[0]
        #print('here is name:',name)
        cur_rew = float(app[3])
        if name in base and (cur_rew == base[name]) and (name not in added_list):
            added_list.append(name)
            final_list.append(app)
    #print(added_list)
    for apps in final_list:
        if if_english(apps[0]):
            english_list.append(apps)
    return final_list,english_list


def if_english(string):
    count = 0
    for char in string:
        if ord(char)> 127:
            count += 1
    if count > 3: 
        return False  
    else:
        return True
        
opened_file1 = open('./PYH.csv')
opened_file2 = open('./googleplaystore.csv')
readed_file1 = list(reader(opened_file1))
readed_file2 = list(reader(opened_file2))
a,c= fix2(readed_file2,True)
b = fix1(readed_file2,True)
#print(a)
print(len(a))
print(len(b))
print(len(c))
#print(explore_data(readed_file1,1,3,True))