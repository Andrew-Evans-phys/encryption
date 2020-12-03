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

identitykey = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".",",","?"]
class Encrypter:

    def encrypt(self,phrase):
        newstring = ""
        phrase = phrase.lower()
        for i in phrase:
            newstring += identitykey[self.key[identitykey.index(i)]-1]
        self.phrase = newstring
        print("phrase: "+str(self.phrase)+'\n')
        return self.phrase

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
        for i in phrase:
            newstring += identitykey[self.key.index(identitykey.index(i)+1)]
        self.phrase = newstring
        print("phrase: "+str(newstring)+'\n')
        return self.phrase

    def keycreate(self):
        n = 0
        key =  []
        while(n < 30):
            randinput = random.randint(1, 30)
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
        print(key,"key length:",len(key)) 
        self.key = key
        return self.key


   #def decrypt(self,phrase,key):

       #print("test")

test = Encrypter() #class creation
#test.keycreate() #create a random key
#test.encrypt("we can now speak in code") #Put text to encrypt here
test.decrypt([8, 29, 9, 10, 13, 30, 2, 7, 27, 26, 6, 21, 16, 3, 28, 23, 19, 4, 18, 15, 14, 17, 5, 12, 11, 25, 24, 20, 1, 22],"k.ndxp.p") #put "null" for auto key use, and enter the key for specific key use. The second "null" is the arguement for the text paste in text there for message decryption
