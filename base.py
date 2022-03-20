def ToBaseTen(n,b):
    global counter4,power,empty,num2,realnum,numlst,realnum,realnumls
    realnum = 0
    counter4 = 0
    numlst = []
    n = str(n)
    while True:
        num2 = n[counter4:counter4+1]
        numlst.append(num2)
        if counter4 == len(n):
            break
        if counter4 == 10:
            break
        counter4 = counter4 + 1
        
    print("numlist : " + str(numlst))
    power = len(numlst) - 2
    if int(n) > 111201100:
        print("large")
        power = len(numlst)
    counter4 = 0
    
    while True:
        num2 = numlst[counter4:counter4 + 1]
        print(num2)
        num2 = empty.join(num2)
        num2 = int(num2)
        print(power)
        num2 = num2 * pow(b,power)
        if power == 0:
            num2 = num2
        counter4 = counter4 + 1
        power = power - 1
        realnumls.append(num2)
        num2 = []
        print("num lst" + str(realnumls))
        if int(n) > 111201100 and power == 1:
            break
        if power == -1:
            break
    for ele in range(0, len(realnumls)):
        realnum = realnum + realnumls[ele]
    if int(n) > 111201100:
        realnum = int(realnum / 9)
    numlst = []
    numlst = []
    counter4 = 0 
    power = 0
    num2 = ""
    numlst = []
    realnumls = []
    return realnum
