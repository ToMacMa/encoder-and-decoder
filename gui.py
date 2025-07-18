import os,json, urllib.request, tkinter as tk
from main import *
downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/encoder-and-decoder/refs/heads/main/createCode.py","createCode.py")
try:
    from createCode import *
except:
    print("Run this program again.")
    quit()
CHAR_LIST = []
files = os.listdir()

downloadFileIfNone("https://raw.githubusercontent.com/ToMacMa/encoder-and-decoder/refs/heads/main/defaultCode.json",'defaultCode.json')
files = os.listdir()

code = readCode()
root = tk.Tk()
root.geometry("800x600")
root.resizable(width=False,height=False)
root.config(bg="white")
root.title("GUI encryptor and decryptor.")

root.rowconfigure([0,1,2],weight=1)
root.columnconfigure([0,1,2],weight=1)


tk.Label(root,text="To encrypt",font=("Arial",int(root.winfo_screenheight()/50)),bg="white").grid(column=0,row=0)
tk.Label(root,text="To decrypt",font=("Arial",int(root.winfo_screenheight()/50)),bg="white").grid(column=2,row=0)

hid1 = tk.Entry(root,text="",font=("Arial",int(root.winfo_screenheight()/120)),bg="white",state='readonly')
hid1.grid(column=0,row=2)

hid2 = tk.Entry(root,text="",font=("Arial",int(root.winfo_screenheight()/120)),bg="white",state='readonly')
hid2.grid(column=2,row=2)

def run(event=None):
    hid1['state'] = 'normal'
    hid1.delete(0,tk.END)
    hid1.insert(0,str(encode(code,str(input1.get()))))
    hid1['state'] = 'readonly'
    hid2['state'] = 'normal'
    hid2.delete(0,tk.END)
    hid2.insert(0,str(decode(code,str(input2.get()))))
    hid2['state'] = 'readonly'
input1 = tk.Entry(root,font=("Arial",int(root.winfo_screenheight()/75)),bg="white")
input1.grid(column=0,row=1)

input2 = tk.Entry(root,font=("Arial",int(root.winfo_screenheight()/75)),bg="white")
input2.grid(column=2,row=1)

button1 = tk.Button(root,font=("Arial",int(root.winfo_screenwidth()/100)),text="Encrypt and decrypt",bg="white",command=lambda:run())
button1.grid(column=1,row=2)

button1.bind('<Key>',run)
root.mainloop()