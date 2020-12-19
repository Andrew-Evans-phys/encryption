########################################################
# This awful program was created by Andrew M Evans 
# with help from a good programmer Leo Jazznuts
#
# This program encrypts text and decrypts with keys 
#
# Works on all OS's that can run python 3.9
#
# Contanct info - 
# 
# Email: evansa@sonoma.edu 
#               or 
# Discord Andrew Evans#4366
########################################################

import random

global identitykey
identitykey = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".",",","?"]
class Encrypter:

    def encrypt(self,phrase):
        newstring = ""
        number = int(self.key, 0)
        key = []
        i = 0
        while(len(identitykey)**i<number):
            i += 1
        for j in range(i):
            i = 0
            while(len(identitykey)**i<number):
                i += 1
            value = number//(len(identitykey)**(i-1))
            number -= value*(len(identitykey)**(i-1))
            key.append(int(value))
        self.key = key
        phrase = phrase.lower()
        for i in phrase:
            newstring += identitykey[self.key[identitykey.index(i)]-1]
        self.phrase = newstring
        #print("phrase: "+str(self.phrase)+'\n')
        return self.phrase

    def showPhrase(self):
        return self.phrase

    def showKey(self):
        return self.key

    def decrypt(self,keyin,phrase):
        if keyin == "null":
            pass
        else:
            self.key =  keyin
        if phrase == "null":
            phrase = self.phrase
        else:
            pass
        newstring = ""
        #print("The length of the weirdlist (cc pending) is:",len(self.key))
        #print("THIS IS THE ERROR",self.key)
        try:
            for i in phrase:
                print("THIS IS THE ERROR")
                print(self.key)
                print(identitykey[self.key.index(identitykey.index(i)+1)])
                newstring += identitykey[self.key.index(identitykey.index(i)+1)]
        except TypeError:
            number = int(self.key, 0)
            key = []
            i = 0
            while(len(identitykey)**i<number):
                i += 1
            for j in range(i):
                i = 0
                while(len(identitykey)**i<number):
                    i += 1
                value = number//(len(identitykey)**(i-1))
                number -= value*(len(identitykey)**(i-1))
                key.append(int(value))
            self.key = key
        for i in phrase:
                print("THIS IS THE ERROR")
                print(self.key)
                print(identitykey[self.key.index(identitykey.index(i)+1)])
                newstring += identitykey[self.key.index(identitykey.index(i)+1)]
        self.phrase = newstring
        #print("phrase: "+str(newstring)+'\n')
        return self.phrase

    def keycreate(self):
        n = 0
        key =  []
        while(n < len(identitykey)-1):
            randinput = random.randint(1, len(identitykey)-1)
            if n !=0:
                add = True
                for i in range(len(key)):
                    if key[i] == randinput:
                        add = False
                if add == True:
                    key.append(randinput)
                    n += 1
            else:
                key.append(randinput)
                n += 1
        #print(key,"key length:",len(key)) 
        self.key = key
        total = 0
        for i in range(len(key)):
            total += key[i]*(len(identitykey)**(29-i))
        self.key  = hex(total)
        #print(self.key)
        return self.key

#test = Encrypter() #class creation
#test.keycreate() #create a random key
#test.encrypt("fuck yea") #Put text to encrypt here
#test.decrypt("null","null") #put "null" for auto key use, and enter the key for specific key use. The second "null" is the arguement for the text paste in text there for message decryption
