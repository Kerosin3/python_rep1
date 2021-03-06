from operator import itemgetter, attrgetter
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
        colomn_num = 4 #iOS
    for apps in dataset:
        if ifAndroid:
            if apps[colomn_num] == '0': #free apss
                apps_list.append(apps)
        elif (apps[colomn_num]) == '0.0': # free apps
            apps_list.append(apps)
    return apps_list
def getColomn(dataset,column_num,isHeader=True,isAndroid=True):
    list_out = {}
    table = {}
    total = 0
    out_table = []
    name_c= 1 # iOs
    installations_freq=[]
    installation_raw={}
    tota_installs=0
    #instal_dict= {'1000+':0,'100000+':0,'100000+':0,'1000000':0}
    if isHeader:
        dataset = dataset[1:]
    if isAndroid:
        name_c = 0
        installs = 5
    for apps in dataset:
        list_out[apps[name_c]] = apps[column_num]
        #installs = app[5]
        #installs = installs.replace('+','')
        #installs = installs.replace(',','')
        genre = apps[1]
        installs = apps[5] #installations
        installs = installs.replace('+','')
        installs = float(installs.replace(',',''))
        tota_installs+=installs
        if genre not in installation_raw:
            installation_raw[genre]=(1,1)
        elif genre in installation_raw:
            (a,b) = installation_raw[genre]
            a+=1
            b+=installs
            installation_raw[genre]=(a,b)
    for app in installation_raw:
        _,installations=installation_raw[app]
        percenatage=round((installations / tota_installs )* 100,2)
        installations_freq.append((app,percenatage))
    installations_freq = sorted(installations_freq,key=itemgetter(1), reverse = True)

    print(installations_freq)    
    #frequences
    for item in list_out:
        total+=1
        #print(item,list_out[item])
        #counting apps number
        if list_out[item] not in table:
            table[list_out[item]] =1
        else:
            table[list_out[item]] += 1

    #c=0
    for item in table:
        #c+=1
        percentage = round((table[item] / total) * 100,2)
        d=(percentage,table[item],item)
        #print(d)
        out_table.append(d)

    #print('counted total:',c)
    return (list_out,table,out_table)

def installsFreq(dataset,is_header=True):
    list_out = {}
    out_table = []
    if is_header:
        dataset=dataset[1:]
    for app in dataset:
        name= app[0]
        installs = app[5]
        installs = installs.replace('+','')
        installs = installs.replace(',','')
        list_out[name] = float(installs)
    total = 0
    for item in list_out:
        total+=1
        percentage = round((list_out[item] / total) * 100,2)
        d=(percentage,list_out[item],item)
        #print(d)
        out_table.append(d)
        out_table = sorted(out_table, reverse = True)
    return out_table
