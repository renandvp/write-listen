#IMPORTS
from tkinter import *
from gtts import gTTS
from playsound import playsound



#STYLE

root = Tk()
root.geometry('450x200')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('ESCREVE QUE EU TE ESCUTO')
Label(root, text = 'ESCREVE QUE EU TE ESCUTO' , font='arial 20 bold' , bg ='white smoke').pack()


#MESSAGE
msg = StringVar()


#Entry
entry_field = Entry(root,textvariable = msg, width ='50')
entry_field.place(x=20 , y=60)


#FUNCTIONS
def writeListen():
    message = entry_field.get()
    if message :
        textVoice = gTTS(text = message, lang='pt')
        textVoice.save('audio.mp3')
        playsound('audio.mp3')

def close():
    root.destroy()

def reset():
    msg.set("")

#BUTTONS
Button(root, text = "PLAY" , font = 'arial 15 bold', command = writeListen, width =4).place(x=25, y=140)
Button(root,text = 'SAIR',font = 'arial 15 bold' , command = close, bg = 'OrangeRed1').place(x=100,y=140)
Button(root, text = 'APAGAR', font='arial 15 bold', command = reset).place(x=175 , y =140)


#RUN
root.mainloop()
