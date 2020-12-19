# !/usr/bin/python3
from tkinter import *
from Cipher import *
from tkinter import messagebox


Encry = Encrypter()

top = Tk()
top.title("GKrypt")

L1 = Label(top, text="Text")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = LEFT)

L2 = Label(top, text="Key")
L2.pack( side = LEFT)
E2 = Entry(top, bd =5)
E2.pack(side = LEFT)

top.geometry("500x500")

def encryptionCallBack():
    key = Encry.keycreate()
    Encry.encrypt(E1.get())
    msg = messagebox.showinfo( "Encryption", str(Encry.showPhrase())+"\n"+"Key: "+str(key))

def decryptionCallBack():
    Encry.decrypt(hex(int(E2.get(),16)),E1.get())
    msg = messagebox.showinfo( "Decryption", str(Encry.showPhrase()))

B1 = Button(top, text = "Encrypt", command = encryptionCallBack)
B1.place(x = 50,y = 50)
B2 = Button(top, text = "Decrypt", command = decryptionCallBack)
B2.place(x = 50,y = 100)
top.mainloop()