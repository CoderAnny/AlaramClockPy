from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox as msg
from pygame import mixer
import time


root = Tk()
root.title("------- ALARAM CLOCK BY ANIKET -------")
root.state("zoomed")
root.resizable(0,0)
iconimg = ImageTk.PhotoImage(file="images/images.jpg")
root.iconphoto(False,iconimg) # Icon Image set for this Software


h = StringVar()
m = StringVar()
f = StringVar()


def setalaram():
    a = h.get()
    b = m.get()
    c = f.get()
    if (a == "Select hour.." or b == "Select minute.." or c == "Select day format.."):
        msg.showerror("----- WRONG -----","INPUT GIVEN IS WRONG!!")
    else:
        a1 = a
        a2 = b
        a = int(a)
        b = int(b)
        if(c == "PM"):
            a += 12
        else:
            a += 0
        h.set("")
        m.set("")
        f.set("")
        msg.showinfo("ALARAM IS SET!!",f"ALARAM IS SET FOR {a1} : {a2} : {c} SUCESSFULLY..")
        alaramtime = f"{a}:{b}"
        current_time = time.strftime("%H:%M")
        while current_time != alaramtime:
            current_time = time.strftime("%H:%M")
            time.sleep(1)
        if current_time == alaramtime:
            mixer.init()
            mixer.music.load("songs/alaramMusic.wav")
            mixer.music.set_volume(1)
            mixer.music.play()
            mg = msg.showinfo("Alaram Time","Alaram is Ringing.....")
            if mg == "ok":
                mixer.music.stop()





style = ttk.Style()

style.theme_create('mytheme',settings={
    "TCombobox":{
        "configure":{
            "selectbackground": '#1C1A21',"fieldbackground": '#1C1A21',"background": '#fff',"foreground":"#fff","padding":(10,5),"borderwidth":2,"relief":"solid"
        }
    }
})
style.theme_use('mytheme')


MainImg = ImageTk.PhotoImage(Image.open("images/download.jpg").resize((root.winfo_width()//2,root.winfo_height()),Image.ANTIALIAS))
photoFrame = Frame(root)
photo_lbl = Label(photoFrame,image=MainImg).pack()
photoFrame.pack(side=LEFT,fill=X)

mainFrame = Frame(root,bg="#1C1A21")



mainFrame.pack(side=LEFT,fill=BOTH,expand=1)

hourInput = ttk.Combobox(mainFrame,values=[i for i in range(1,13)],textvariable=h)
hourInput.set("Select hour..")
hourInput.place(x=30,y=150)

minuteInput = ttk.Combobox(mainFrame,values=[i for i in range(0,60)],textvariable=m)
minuteInput.set("Select minute..")
minuteInput.place(x=260,y=150)

secondInput = ttk.Combobox(mainFrame,values=["AM","PM"],textvariable=f)
secondInput.set("Select day format..")
secondInput.place(x=480,y=150)

for i in (hourInput,minuteInput,secondInput):
    i.config(font=('system',12,'bold'),cursor="hand2",justify=CENTER,state="readonly")


setbtn = Button(mainFrame,text="Set-Alaram",command=lambda:setalaram())
setbtn.place(x=50,y=350)

exitbtn = Button(mainFrame,text="Exit",command=root.destroy)
exitbtn.place(x=510,y=350)

for i in(setbtn,exitbtn):
    i.config(bg="blue",fg="#fff",font=('Vernda',12,'bold'),bd=0,height=2,width=15,cursor="hand2")

root.config(bg="black")
root.mainloop()