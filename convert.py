import sys
args=sys.argv
if(len(args)<3 or len(args)>3):
    print("Invalid argument list")
else:
    convertTo=args[1]
    val=args[2]
    hexVals=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    binVals=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
    res=""
    if(convertTo=="--bin"):
        temp=""
        for i in val:
            if(i!=":"):
                temp+=i
        tlen=len(temp)
        for i in range(12-tlen):
            temp="0"+temp
        try:
            for i in temp:
                ind=hexVals.index(i.upper())
                res+=binVals[ind]
        except:
            print("Invalid Mac Aaddress")
        else:
            print(res)
    elif(convertTo=="--mac"):
        temp=val
        tlen=len(temp)
        for i in range(48-tlen):
            temp="0"+temp
        try:
            for i in range(12):
                ind=binVals.index(temp[i*4:(i+1)*4])                
                res+=hexVals[ind]
                if(i<11 and i%2!=0):
                    res+=":"
        except:
            print("Invalid Binary Aaddress")
        else:
            print(res)
    else:
        print("Invalid Command")
