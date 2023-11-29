from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def search():
    data=json.load(open("data.json"))
    word=enterwordEntry.get()
    word=word.lower()
    if word in data:
        meaning=data[word]
        print(meaning)
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END,u'\u2022'+item+'\n\n')
    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        res = messagebox.askyesno("Confirm",f'Did you mean {close_match} instead?')
        if res == True:
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(END,close_match)
            meaning=data[close_match]
            textarea.delete(1.0,END)
            for item in meaning:
                textarea.insert(END,u'\u2022'+item+'\n\n')
        else:
            messagebox.showinfo('Error','The word doesnot exist,Please double check it.')
            enterwordEntry.delete(1.0,END)       
    else:
        messagebox.showinfo('Information','The word does not exist') 
        enterwordEntry.delete(0,END)  
        textarea.delete(1.0,END)         
        

def clear():
    enterwordEntry.delete(0,END)
    textarea.delete(1.0,END)

def iexit():
    res=messagebox.askyesno('Confirm','Do yoy want to exit?')
    if res== True:
        root.destroy()

    else:
        pass    

def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()

def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()

root=Tk()

root.geometry("1000x626+100+30")
root.title("Talking Dictionary")
root.resizable(False,False)

bgimage=PhotoImage(file='bg.png')
bgLabel=Label(root,image=bgimage)
bgLabel.place(x=0,y=0)

enterwordlabel=Label(root,text="ENTER WORD",font=("castellar",29,"bold"),fg="red3",bg="whitesmoke")
enterwordlabel.place(x=530,y=20)

enterwordEntry=Entry(root,font=("arial",23,"bold"),justify=CENTER,bd=8,relief=GROOVE)
enterwordEntry.place(x=510,y=80)

searchimage=PhotoImage(file="search.png")
searchButton=Button(root,image=searchimage,bd=0,bg="whitesmoke",cursor="hand2",activebackground="whitesmoke",command=search)
searchButton.place(x=600,y=150)

micimage=PhotoImage(file="mic.png")
micButton=Button(root,image=micimage,bd=0,bg="whitesmoke",cursor="hand2",activebackground="whitesmoke",command=wordaudio)
micButton.place(x=700,y=153)

meaninglabel=Label(root,text="MEANING",font=("castellar",29,"bold"),fg="red3",bg="whitesmoke")
meaninglabel.place(x=570,y=225)

textarea = Text(root,width=34,height=8,font=("arial",18,"bold"),bd=8,relief=GROOVE)
textarea.place(x=460,y=285)

microphoneimage=PhotoImage(file="microphone.png")
microphoneButton=Button(root,image=microphoneimage,bd=0,bg="whitesmoke",cursor="hand2",activebackground="whitesmoke",command=meaningaudio)
microphoneButton.place(x=530,y=545)

clearimage=PhotoImage(file="clear.png")
clearButton=Button(root,image=clearimage,bd=0,bg="whitesmoke",cursor="hand2",activebackground="whitesmoke",command=clear)
clearButton.place(x=660,y=545)

exitimage=PhotoImage(file="exit.png")
exitButton=Button(root,image=exitimage,bd=0,bg="whitesmoke",cursor="hand2",activebackground="whitesmoke",command=iexit)
exitButton.place(x=790,y=545)

def enter_function(event):
    searchButton.invoke()

root.bind('<Return>',enter_function)

root.mainloop()