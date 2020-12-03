def hexToList(number):
    number = int(number, 0)
    key = []
    i = 0
    while(30**i<number):
        i += 1
    for j in range(i):
        i = 0
        while(30**i<number):
            i += 1
        value = number//(30**(i-1))
        number -= value*(30**(i-1))
        key.append(int(value))
    print("key lenght is: "+str(len(key)))
    return key

def listToHex(list):
    total = 0
    for i in range(len(list)):
        total += list[i]*(30**(29-i))
    total  = hex(total)
    print(total)
    return total


print(hexToList("0x2beef32e662c4afc9ccfdbe66f1adfaecb4d8"))