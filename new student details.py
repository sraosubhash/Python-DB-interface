# New student details
from tkinter import *
from tkinter import messagebox as msgb
import mysql.connector
con = mysql.connector.connect(user='root', password='ani_2002', host='localhost', database='credentials')
cursor = con.cursor()
ns = Tk()
ns.title('Add new student details')
nsc = Canvas(width=700, height=500)


# Saving
def _sav():
    _name = en_name.get()
    _roll = en_roll.get()
    _dob = en_dob.get()
    _admn = en_admission.get()
    _class = en_class.get()
    print(_name, _roll, _dob, _admn)
    try:
        cursor.execute('insert into '+_class+"(roll,StudentName,AdmissionNo,dob) VALUES('{0}','{1}','{2}','{3}')"
                       .format(_roll, _name, _admn, _dob))
        con.commit()
        msgb.showinfo('Alert', 'Data saved successfully!')
    except mysql.connector.Error:
        msgb.showinfo('Alert!', 'Error occurred!')
# Image


bgns = PhotoImage(file='D:\\Project SDBMS\\img4.png')
nsc.create_image(0, 0, image=bgns, anchor=NW)
# Text
nsc.create_text(260, 70, text='STUDENT DATA CREATION', font=('Calibri', 30), fill='cyan')
nsc.create_text(230, 140, text='Enter name of student:', font=('Calibri', 25), fill='white')
nsc.create_text(256, 210, text='Enter Roll number:', font=('Calibri', 25), fill='white')
nsc.create_text(255, 280, text='Enter date of birth:', font=('Calibri', 25), fill='white')
nsc.create_text(252, 350, text='Admission number:', font=('Calibri', 25), fill='white')
# Entry boxes
en_name = Entry(ns, width=25, bd=4)
en_roll = Entry(ns, width=25, bd=4)
en_admission = Entry(ns, width=25, bd=4)
en_dob = Entry(ns, width=25, bd=4)
# Entry box position
en_name.place(x=450, y=129)
en_roll.place(x=450, y=199)
en_dob.place(x=450, y=269)
en_admission.place(x=450, y=339)
# Button
button_save = Button(nsc, text='SAVE!', font='Calibri', width=12, height=1, activebackground='light green', command=_sav
                     )
button_save.place(x=320, y=400)
def sav():
    _name = en_name.get()
    _roll = en_roll.get()
    _dob = en_dob.get()
    _admn = en_admission.get()
    _class = en_class.get()
    print(_name,_roll,_dob,_admn)
    cursor.execute('select roll from ' + _class)
    ad = cursor.fetchall()
    m = 0
    for i in ad:
        for a in i:
            print(_roll, a)

            if a == _roll:
                m += 1
            else:
                pass
    if m == 0:
        try:
            cursor.execute(
                'insert into ' + _class + "(roll,StudentName,AdmissionNo,dob) VALUES('{0}','{1}','{2}','{3}')"
                .format(_roll, _name, _admn, _dob))
            con.commit()
            msgb.showinfo('Alert', 'Data saved successfully!')
            ns.destroy()
        except mysql.connector.Error:
            msgb.showinfo('Alert!', 'Error occurred!, Please contact system administrator')
    else:
        msgb.showinfo('Oops!', 'Roll number already exists!')
ns.resizable(0, 0)
nsc.pack()

ns.mainloop()
