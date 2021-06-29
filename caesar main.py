import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
root=tk.Tk()
root.title('Caeser cipher')
root.geometry("800x500")
root.resizable(width= FALSE, height=FALSE)
canvas = tk.Canvas(root,height = 800, width=800, bg="blue")
canvas.pack()
bold_font = tkfont.Font(family="Helvetica",size=20,weight="bold")
label1 = tk.Label(root,text= "PLAIN TEXT- ",width=20,bg="blue")
label1.config(font=bold_font)
label1.place(relx=1.0,rely=0.0,anchor='ne')
canvas.create_window(200,100,window=label1)
user_text = tk.Entry(root)
canvas.create_window(350,100,window=user_text)

label2=tk.Label(root,text="CIPHER TEXT-",width=20,bg="blue")
label2.config(font=bold_font)
canvas.create_window(200,200,window=label2)
label3=tk.Label(root,text="KEY USED-",width=20,bg="blue")
label3.config(font=bold_font)
canvas.create_window(200,250,window=label3)




def encryption():
    global k1
    import random
    k1 = random.randint(3, 20)
    global c
    c=""
    n=user_text.get()
    for i in n:
        if(i.isupper()):
            c_1= ord(i)
            c_2= ord(i) - 65
            c_3=(c_2 + k1)% 26 +65
            c_4= chr(c_3)
            c=c+c_4
        else:
            c_1=ord(i)
            c_2=ord(i) -97
            c_3=(c_2 + k1)% 26 +97
            c_4= chr(c_3)
            c=c+c_4

    label5 =tk.Label(root,text=c,width=12,bg="white")
    label5.config(font=bold_font)
    canvas.create_window(410,200,window=label5)
    label4=tk.Label(root,text=k1,width=12,bg="white")
    label4.config(font=bold_font)
    canvas.create_window(410,250,window=label4)

btn = Button(root, text='Encrypt', bd='10', command=encryption)
btn.place(x=300, y=130)

def decryption():
    global c
    global k1

    plain_text=""
    for i in c:
        if i.isupper():
             c_1=ord(i)
             c_2=ord(i)-65
             c_3=(c_2-k1)%26+65
             c_4=chr(c_3)
             plain_text=plain_text + c_4
        else:
             c_1=ord(i)
             c_2=ord(i)-97
             c_3=(c_2-k1)%26+97
             c_4=chr(c_3)
             plain_text=plain_text + c_4

    label6= tk.Label(root,text=plain_text,width=20,bg="white")
    label6.config(font=bold_font)
    canvas.create_window(470,370,window=label6)
btn1= Button(root,text="Decrypt",bd='10', command=decryption)
btn1.place(x=300,y=300)
root.mainloop()


