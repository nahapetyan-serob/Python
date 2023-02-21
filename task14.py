print ('Enter your US or Can phone number')
phone = input()
if len(phone) == 14:
    temp1 = str(phone [2:5])
    temp2 = str(phone [6:9])
    temp3 = str(phone [10:])
    if phone [0] != '1':
        print ('Invalid')
        exit()
    elif phone [1] != '-':
        print ('Invalid')
        exit()
    elif phone [5] != '-':
        print ('Invalid')
        exit()
    elif phone [9] != '-':
        print ('Invalid')
        exit()
    elif not str(phone [2:5]).isdigit():
        print ('Invalid')
        exit()
    elif not str(phone [6:9]).isdigit():
        print ('Invalid')
        exit()
    elif not str(phone [10:]).isdigit():
        print ('Invalid')
        exit()
    else: 
        print ('Valid')
elif len(phone) == 12:
    if phone [3] != '-':
        print ('Invalid')
        exit()
    elif phone [7] != '-':
        print ('Invalid')
        exit()
    elif not str(phone [:3]).isdigit() :
        print ('Invalid')
        exit()
    elif not str(phone [4:7]).isdigit() :
        print ('Invalid')
        exit()
    elif not str(phone [8:]).isdigit():
        print ('Invalid')
        exit()
    else: 
        print ('Valid')
else:
    print ('Invalid')

