# Program for sign-up user interface
from tkinter import *
su=Tk()
su.title("Sign-up!")
# Structure
# Canvas and background
cansgu=Canvas(su,width=800,height=600)
bgsu=PhotoImage(file="D:\\Project SDBMS\\signupbg.png")
cansgu.create_image(0,0,image=bgsu,anchor=NW)
# Canvas text
txthead=cansgu.create_text(220,130,text="SIGN-UP!",font=("Open Sans",50),fill='white')
txtins=cansgu.create_text(330,200,text="PLEASE FILL UP THE FOLLOWING CREDENTIALS:",font=("Calibri",20),fill='white')
txtname=cansgu.create_text(250,260,text="NAME:",font=("Calibri",20),fill='white')
txtusn=cansgu.create_text(222,320,text="USERNAME:",font=("Calibri",20),fill='white')
txtpass=cansgu.create_text(222,380,text="PASSWORD:",font=("Calibri",20),fill='white')
txtclass= cansgu.create_text(255,440,text='CLASS:', font=("Calibri", 20), fill='white')
# Entry Boxes
enname=Entry(su,bd=5,width=30)
ensgusn=Entry(su,bd=5,width=30)
ensgpas=Entry(su,bd=5,width=30)
engsclass=Entry(su,bd=5,width=30)
# Entry Position
enname.place(x=320,y=250)
ensgusn.place(x=320,y=310)
ensgpas.place(x=320,y=370)
engsclass.place(x=320,y=430)
# Buttons
sb=Button(su,text="Create account!",height=1,width=15,activebackground='sky blue',font="Calibri")
# Button position
sb.place(x=340,y=480)
su.resizable(0,0)
cansgu.pack()
su.mainloop()