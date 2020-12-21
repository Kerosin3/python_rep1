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
def fix1(dataset,header=True,isAndroid=True):
    if header:
        dataset = dataset[1:]
    list_b = {}
    review_rating = 0
    rating = 3
    name_c=0
    if not isAndroid:
        rating=5
        name_c=1
    for app in dataset:
        review_rating = float(app[rating])
        name = app[name_c]
        if name in dataset and review_rating > list_b[name]:
            list_b[name] = review_rating
        elif name not in dataset:
            list_b[name]=review_rating
    return list_b
def fix2(dataset,header=True,isAndroid=True):
    a=isAndroid
    base = fix1(dataset,header=True,isAndroid=a)
    final_list= []
    english_list=[]
    added_list = []
    if header:
        dataset=dataset[1:]
    rating = 3
    name_c=0
    store= 'Android'
    if not isAndroid:
        rating=5
        name_c=1
        store = 'AppStore'
    for app in dataset:
        name = app[name_c]
        #print('here is name:',name)
        cur_rew = float(app[rating])
        if name in base and (cur_rew == base[name]) and (name not in added_list):
            added_list.append(name)
            final_list.append(app)
    #print(added_list)
    english_count =0
    for apps in final_list:
        if if_english(apps[name_c]):
            english_list.append(apps)
            english_count+=1
    print('total not english apps that have been rejected in %s is %d:' % (store,len(dataset)-english_count))
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

def findingFreeApps(dataset,consistHeader=False,ifAndroid=True):
    colomn_num=7 #android
    apps_list=[]
    if not ifAndroid:
        colomn_num = 4
    for apps in dataset:
        if float(apps[colomn_num]) != 0.0:
            apps_list.append(apps)
    return apps_list

