from tkinter import *

window = Tk()
window.title("Crypto")
window.geometry("720x480")
window.minsize(720, 480)
window.iconbitmap("cesar.ico")
window.config(background='#41b77f')

frame = Frame(window,bg = '#41b77f')
left_frame = Frame(frame,bg = '#41b77f')
right_frame = Frame(frame,bg = '#41b77f')

Encryptag = Label(left_frame,text = "ENCRYPTAGE",font = ("Neuropol",30),bg = "#41b77f", fg = "white")
Encryptag.pack()
#partie gauche
width = 300
height = 300
image = PhotoImage(file="Crypter.png").zoom(10).subsample(30)
canvas = Canvas(left_frame, width=width, height= height,bg='#41b77f',bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(side = LEFT)

#partie droite

def crypt():
    text_result.delete(0, END)
    text = text_entry.get()
    clef = int(key_entry.get())
    message = []
    message_decode = []
    for i in text:
        message.append(ord(i) + clef)
    for i in message:
        message_decode.append(chr(i))
    final = "".join(message_decode)
    text_result.insert(0,final)
    text_result.pack()


#interface cryptage
lblt = Label(right_frame,text='taper le texte :',bg = '#41b77f',font = ("Neuropol",15),fg = "white").pack(pady = 2)
text_entry = Entry(right_frame,font = ('Aerial',15), bg = 'white', fg= 'black',width = '20')
text_entry.pack(fill = X)
lblc = Label(right_frame, text = 'Donner la clé :',bg = '#41b77f',font = ("Neuropol",15),fg = "white").pack(pady = 2)
key_entry = Entry(right_frame,font = ('Aerial',15), bg = 'white', fg= 'black',width = '20')
key_entry.pack(fill = X)
crypt_button = Button(right_frame,text = 'Crypter', bg='black',fg='white',command = crypt,font = "Neuropol")
crypt_button.pack(fill = X, pady = 10)
lbls = Label(right_frame,text = 'voici les données encryptées :',bg = '#41b77f',font = ("Adelia",15),fg = "white").pack(pady = 2)
text_result = Entry(right_frame,font = ('Aerial',15), bg = 'white', fg= 'black',width = '20')
text_result.pack(fill = X)

#appel des frames utilisé
frame.pack(expand=YES)
left_frame.grid(row = 0, column =0)
right_frame.grid(row = 0, column = 1)
window.mainloop()



