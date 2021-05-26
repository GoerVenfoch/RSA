from tkinter import *
import RSA
from tkinter import messagebox as mb
import random

backgroundColor = "White"
root = Tk()
root.title("Cipher RSA")
root.geometry('750x600')
root.configure(background=backgroundColor)
PubKeyLbl = Label(text="Public key", font="Times 14", background=backgroundColor)
PubKeyLbl.place(x=60, y=10)
PrivKeyLbl = Label(text="Private key", font="Times 14", background=backgroundColor)
PrivKeyLbl.place(x=65, y=110)
NLbl = Label(text="N:", font="Times 14", background=backgroundColor)
NLbl.place(x=40, y=40)
NEntry = Entry(width="60")
NEntry.place(x=70, y=40)
SLbl = Label(text="S:", font="Times 14", background=backgroundColor)
SLbl.place(x=40, y=80)
SEntry = Entry(width="60")
SEntry.place(x=70, y=80)
ELbl = Label(text="E:", font="Times 14", background=backgroundColor)
ELbl.place(x=40, y=140)
EEntry = Entry(width="60")
EEntry.place(x=70, y=140)
InLbl = Label(text="Message", font="Times 14", background=backgroundColor)
InLbl.place(x=65, y=170)
InText = Text(width="50", height="10")
InText.place(x=40, y=200)
OutLbl = Label(text="Results", font="Times 14", background=backgroundColor)
OutLbl.place(x=65, y=380)
OutText = Text(width="50", height="10")
OutText.place(x=40, y=410)
GenerKeysBtn = Button(text="Generate keys", font="Times 14", width="20")
GenerKeysBtn.place(x=500, y=150)
EncryptBtn = Button(text="Encrypt", font="Times 14", width="20")
EncryptBtn.place(x=500, y=200)
DecryptBtn = Button(text="Decrypt", font="Times 14", width="20")
DecryptBtn.place(x=500, y=250)

def generate_keys_clicked(event):
    NEntry.configure(state='normal')
    SEntry.configure(state='normal')
    EEntry.configure(state='normal')
    NEntry.delete(0, END)
    SEntry.delete(0, END)
    EEntry.delete(0, END)
    array_keys = RSA.generate_keys()
    n = array_keys[0]
    s = array_keys[1]
    e = array_keys[2]
    NEntry.insert(0, n)
    SEntry.insert(0, s)
    EEntry.insert(0, e)
    NEntry.configure(state='readonly')
    SEntry.configure(state='readonly')
    EEntry.configure(state='readonly')
    EncryptBtn.config(state='normal')
    DecryptBtn.config(state='normal')

def encrypt_clicked(event):
    OutText.delete(1.0, END)
    key_n = int(NEntry.get())
    key_s = int(SEntry.get())
    message = InText.get(1.0, END)
    if message == '\n':
        mb.showerror("Error", "The message is missing! Enter the text and try again!")
        return
    numbers = ""
    bloсks = []
    tableSymbols = RSA.create_char_table()
    for letter in message.lower():
        numbers += str(tableSymbols[letter])
    while len(numbers) > 13:
        block_length = random.randint(2, 13)
        while numbers[block_length] == '0':
            block_length += 1
        bloсks.append(numbers[:block_length])
        numbers = numbers[block_length:]
    if numbers:
        bloсks.append(numbers)
    result = ""
    for i in range(len(bloсks)):
        result = result + str(pow(int(bloсks[i]), key_s, key_n)) + " "
    OutText.insert(1.0, result)
    

def decrypt_clicked(event):
    OutText.delete(1.0, END)
    key_n = int(NEntry.get())
    key_e = int(EEntry.get())
    message = InText.get(1.0, END)
    tableSymbols = RSA.create_char_table()
    reverseTable = {value: key for key, value in tableSymbols.items()}
    if message == '\n':
        mb.showerror("Error", "The message is missing! Enter the text and try again!")
        return
    numbers = message.split()
    decryptedMessage = ""
    result = ""
    for i in range(len(numbers)):
        decryptedMessage = decryptedMessage + str(pow(int(numbers[i]), key_e, key_n))
    while len(decryptedMessage) != 0:
        symbol = int(decryptedMessage[:4])
        decryptedMessage = decryptedMessage[4:]
        if str(reverseTable.get(symbol)) == "None":
            mb.showerror("Error", "Operation is not possible")
            return
        result = result + str(reverseTable.get(symbol))
    OutText.insert(1.0, result)

def paste(event):
    InText.delete(1.0, END)
    out = OutText.get(1.0, END)
    InText.insert(1.0, out)

GenerKeysBtn.bind('<Button-1>', generate_keys_clicked)
InText.bind('<Button-3>', paste)
EncryptBtn.bind('<Button-1>', encrypt_clicked)
DecryptBtn.bind('<Button-1>', decrypt_clicked)
root.mainloop()