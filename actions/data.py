d_data = {
    'prajwal':{'account':'0123456A', 'number':'9876543210', 'balance': '750.0'},
    'pranaya':{'account':'1234567A', 'number':'9876543210', 'balance': '800.0'},
    'kriti':{'account':'2345678A', 'number':'9876543210', 'balance': '900.0'},
}

trans_hist = {
    'prajwal':{'2022-05-20':'600.0',
               '2022-05-22':'650.0',
               '2022-05-23':'780.0',
               '2022-05-25':'750.0',},
    'pranaya':{'2022-05-20':'700.0',
               '2022-05-21':'650.0',
               '2022-05-22':'710.0',
               '2022-05-25':'800.0',},
    'kriti':{'2022-05-20':'700.0',
             '2022-05-21':'800.0',
             '2022-05-23':'950.0',
             '2022-05-25':'900.0',},
}

def check_avilable(name, account, number, d_data):
    if name not in d_data.keys():
        return 0
    else:
        if d_data[name]['account'] == account and d_data[name]['number'] == number:
            return 1
        else:
            return 0
        
# print(check_avilable('kritim','2345678N','9876543210',d_data))