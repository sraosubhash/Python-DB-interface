from tkinter import *
from tkinter import messagebox as msgb
import time
import mysql.connector

con = mysql.connector.connect(user='root', password='1234', host='localhost')
cursor = con.cursor()
try:
    cursor.execute('create database credentials')
    con.commit()
except mysql.connector.Error:
    pass
cursor.execute('use credentials')

try:
    d = 'create table enps(Name varchar(30),Username varchar(30),' \
        'password varchar(20),Class varchar(5))'
    cursor.execute(d)
except mysql.connector.Error:
    pass
try:
    cursor.execute('create table senps(Name varchar(30),Username varchar(30)'
                   ', Password varchar(30), Class varchar(10),roll varchar(10))')
except mysql.connector.Error:
    pass
top = Tk()
top.title("Student database management system.")


# Coding
# Teacher section
def ver():
    usn = enus.get()
    pas = enpas.get()
    squs = 'select username from enps'
    cursor.execute(squs)
    dat = cursor.fetchall()
    m = 0
    for i in dat:
        for a in i:
            if a == usn:
                m += 1
            else:
                pass
    if m == 1:
        sqps = ("select password from enps where username='{0}'".format(usn))
        cursor.execute(sqps)
        datp = cursor.fetchall()
        p = 0
        for i in datp:
            for b in i:
                if b == pas:
                    p += 1
                else:
                    pass
        if p == 1:
            cursor.execute("select name from enps where username='{0}'".format(usn))
            a = cursor.fetchone()
            name = ''
            for i in a:
                for b in i:
                    name += b
            cursor.execute("select class from enps where username='{0}'".format(usn))
            a = cursor.fetchone()
            clas = ''
            for i in a:
                for a in i:
                    clas += a
            adlg(name, clas)
            return name, clas
        else:
            msgb.showinfo('Something went wrong at ' + time.ctime(),
                          "Incorrect password")
    else:
        msgb.showinfo('Something went wrong at ' + time.ctime(),
                      "Username incorrect/Username not found!")


def sign_up():
    su = Toplevel(top)
    su.title("Sign-up!")
    # Structure
    # Canvas and background
    cansgu = Canvas(su, width=800, height=600)
    bgsu = PhotoImage(file="V:\DBMS\Project_SDBMS[1]\Project SDBMS\signupbg.png")
    cansgu.create_image(0, 0, image=bgsu, anchor=NW)

    # Data storage

    def st():
        name = enname.get()
        usn = ensgusn.get()
        passg = ensgpas.get()
        clas = engsclass.get()
        squs = 'select username from enps'
        cursor.execute(squs)
        dat = cursor.fetchall()
        m = 0
        for i in dat:
            for a in i:
                if a == usn:
                    m += 1
                else:
                    pass
        if m == 0:
            if name == '':
                msgb.showinfo('Oops!', 'Name field cannot be left blank!')
            elif usn == '':
                msgb.showinfo('Oops!', 'Username field cannot be left blank!')
            elif passg == '':
                msgb.showinfo('Oops!', 'Password field cannot be left blank!')
            elif clas == '':
                msgb.showinfo('Oops!', 'Class field cannot be left blank!')
            else:
                en = ("INSERT INTO enps VALUES('{0}','{1}','{2}','{3}')".format(name, usn, passg, clas))
                cd = 'create table ' + clas + '(Roll int,StudentName varchar(30),AdmissionNo int,DOB varchar(30))'
                try:
                    cursor.execute(cd)
                    cursor.execute(en)
                    try:
                        blank_insertion(clas)
                    except mysql.connector.Error:
                        pass
                    con.commit()
                    msgb.showinfo('Success!', 'Account created successfully at ' + time.ctime())
                except mysql.connector.Error:
                    msgb.showinfo('Something went wrong at ' + time.ctime(),
                                  'Class database already exists!, Contact system administrator')
                su.destroy()
        else:
            msgb.showinfo('Oops!', 'Username is already taken')

    # Structure
    # Canvas text
    cansgu.create_text(220, 130, text="SIGN-UP!", font=("Open Sans", 50), fill='white')
    cansgu.create_text(330, 200, text="PLEASE FILL IN THE FOLLOWING CREDENTIALS:", font=("Calibri", 20),
                       fill='white')
    cansgu.create_text(250, 260, text="NAME:", font=("Calibri", 20), fill='white')
    cansgu.create_text(222, 320, text="USERNAME:", font=("Calibri", 20), fill='white')
    cansgu.create_text(222, 380, text="PASSWORD:", font=("Calibri", 20), fill='white')
    cansgu.create_text(255, 440, text='CLASS:', font=("Calibri", 20), fill='white')
    # Entry Boxes
    enname = Entry(su, bd=5, width=30)
    ensgusn = Entry(su, bd=5, width=30)
    ensgpas = Entry(su, bd=5, width=30)
    engsclass = Entry(su, bd=5, width=30)
    # Entry Position
    enname.place(x=320, y=250)
    ensgusn.place(x=320, y=310)
    ensgpas.place(x=320, y=370)
    engsclass.place(x=320, y=430)
    # Buttons
    sb = Button(su, text="Create account!", height=1, width=15, activebackground='sky blue', font="Calibri", command=st)
    # Button position
    sb.place(x=340, y=480)
    cansgu.pack()
    su.resizable(0, 0)
    su.mainloop()


def blank_insertion(clas):
    cursor.execute('INSERT INTO ' + clas + " VALUES(0,'NIL', 0,'NIL')")
    con.commit()


# Post-Login
def adlg(name, clas):
    # Programming
    # Sub GUI-1 New student details
    def nsd():
        ns = Toplevel(admn)
        ns.title('Add new student details')
        nsc = Canvas(ns, width=700, height=500)

        # Saving
        def _sav():
            _name = en_name.get()
            _roll = en_roll.get()
            _dob = en_dob.get()
            _admn = en_admission.get()
            try:
                cursor.execute('select roll from ' + clas)
                dat = cursor.fetchall()
                _r = 0
                for i in dat:
                    for a in i:
                        if int(a) == int(_roll):
                            _r += 1
                        else:
                            pass
                if _r == 1:
                    msgb.showinfo('Something went wrong at ' + time.ctime(), 'Roll number already exists!')
                else:
                    cursor.execute(
                        'insert into ' + clas + " VALUES('{0}','{1}','{2}','{3}')".format(_roll, _name, _admn, _dob))
                    con.commit()
                    try:
                        cursor.execute('delete from ' + clas + " where StudentName='NIL'")
                        con.commit()
                    except mysql.connector.Error:
                        pass
                    data_insertion()
                    msgb.showinfo('Success', 'Data saved successfully at ' + time.ctime())
                    ns.destroy()
                    admn.destroy()
                    adlg(name, clas)
            except mysql.connector.Error:
                msgb.showinfo('Something went wrong at ' + time.ctime(),
                              'Error occurred!, Please contact system administrator')

        # Image
        bgns = PhotoImage(file='V:\DBMS\Project_SDBMS[1]\Project SDBMS\img4.png')
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
        en_dob = Entry(ns, width=25, bd=4)
        en_admission = Entry(ns, width=25, bd=4)
        # Entry box position
        en_name.place(x=450, y=129)
        en_roll.place(x=450, y=199)
        en_dob.place(x=450, y=269)
        en_admission.place(x=450, y=339)
        # Button
        button_save = Button(nsc, text='SAVE!', font='Calibri', width=12, height=1, activebackground='light green',
                             command=_sav)
        button_save.place(x=320, y=450)
        nsc.pack()
        ns.resizable(0, 0)
        ns.mainloop()

    # Sub GUI2- Update or delete data
    def up_del():
        ud = Toplevel(top)
        ud_canvas = Canvas(ud, width=900, height=450)
        ud.title(time.ctime())

        # Programming
        def delete():
            r_d = enb_roll.get()
            cursor.execute('select roll from ' + clas)
            dat = cursor.fetchall()
            r = 0
            for i in dat:
                for a in i:
                    if int(a) == int(r_d):
                        r += 1
                    else:
                        pass
            if r == 1:
                cursor.execute('delete from ' + clas + ' where roll=' + r_d)
                con.commit()
                msgb.showinfo('Success', 'Data deleted successfully at ' + time.ctime())
                cursor.execute('select roll from ' + clas)
                r_oll = cursor.fetchall()
                if r_oll == []:
                    blank_insertion(clas)
                    con.commit()
                else:
                    pass
                ud.destroy()
                admn.destroy()
                adlg(name, clas)
            else:
                msgb.showinfo('We encountered an error!', 'Roll number entered does not exist!')

        def up_date():
            _rol = enb_rollu.get()
            cursor.execute('select roll from ' + clas)
            dat = cursor.fetchall()
            r = 0
            for i in dat:
                for a in i:
                    if int(a) == int(_rol):
                        r += 1
                    else:
                        pass
            if r == 1:
                u_d = enb_update.get()
                u_v = enb_value.get()
                if u_d != 'roll' and u_d != 'studentname' and u_d != 'admissionno' and u_d != 'dob':
                    msgb.showinfo('We encountered en error!', "Entered field doesn't meet the required format!")
                else:
                    cursor.execute("update " + clas + " set " + u_d + "='{0}'".format(u_v) + ' where roll=' + _rol)
                    con.commit()
                    data_insertion()
                    msgb.showinfo('Success', 'Data updated successfully at ' + time.ctime())
            else:
                msgb.showinfo('We encountered an error!', 'Roll number entered does not exist!')

        # Body
        # Image

        ud_image = PhotoImage(file="V:\DBMS\Project_SDBMS[1]\Project SDBMS\img4.png")
        ud_canvas.create_image(0, 0, anchor=NW, image=ud_image)
        # Text
        ud_canvas.create_text(350, 30, text="UPDATE OR DELETE STUDENT DETAILS!", font=("Calibri", 30, 'bold'),
                              fill='white')
        ud_canvas.create_text(450, 100, text='DELETE DETAILS', font=("Calibri", 28), fill='white')
        ud_canvas.create_text(300, 160, text='Enter Roll No. of student to delete:', font=("Calibri", 23), fill='white')
        # Update details text
        ud_canvas.create_text(450, 200, text='UPDATE DETAILS', font=("Calibri", 28), fill='white')
        ud_canvas.create_text(189, 240, text='Enter Roll number of student:', font=("Calibri", 20), fill='white')
        ud_canvas.create_text(218, 290, text='Enter field to update:', font=("Calibri", 23), fill='white')
        ud_canvas.create_text(445, 330,
                              text='{Enter data above as per the following format: Roll- roll, Name- studentname, '
                                   'Admission No. -admissionno, Date of birth- dob}',
                              font=("Calibri", 13), fill='white')
        ud_canvas.create_text(310, 370, text='Value:', font=("Calibri", 23), fill='white')
        # Entry Box
        enb_roll = Entry(ud, width=25, bd=4)
        enb_rollu = Entry(ud, width=25, bd=4)
        enb_update = Entry(ud, width=25, bd=4)
        enb_value = Entry(ud, width=25, bd=4)
        # Entry boxes position
        enb_roll.place(x=530, y=150)
        enb_rollu.place(x=370, y=230)
        enb_update.place(x=370, y=280)
        enb_value.place(x=370, y=360)
        # Button
        b_update = Button(ud, text="UPDATE!", height=1, width=10, activebackground='skyblue', font='Calibri',
                          command=up_date)
        b_delete = Button(ud, text="DELETE!", height=1, width=10, activebackground='skyblue', font='Calibri',
                          command=delete)
        # Button Position
        b_update.place(x=400, y=405)
        b_delete.place(x=720, y=145)
        ud_canvas.pack()
        ud.resizable(0, 0)
        ud.mainloop()

    # Sub GUI-3
    def update_marks():
        u_m = Toplevel(top)
        m_canvas = Canvas(u_m, width=1200, height=650)
        u_m.title('View & Update student marks!')
        # Image
        um_image = PhotoImage(file="V:\DBMS\Project_SDBMS[1]\Project SDBMS\img4.png")
        m_canvas.create_image(0, 0, anchor=NW, image=um_image)
        # Scrollbar
        scrollbar = Scrollbar(m_canvas)

        # Programming stuff
        def show():
            s = entry_session2.get()
            try:
                dat_insertion(s)
            except mysql.connector.Error:
                msgb.showinfo('Something went wrong at ' + time.ctime(),
                              'Session does not exist!. Contact Administrator')
            return s

        def dat_insertion(s):
            lstro.delete(0, 'end')
            lstcs.delete(0, 'end')
            lstphy.delete(0, 'end')
            lstmat.delete(0, 'end')
            lstchem.delete(0, 'end')
            lsteng.delete(0, 'end')
            lstbx = [lstro, lstcs, lstphy, lstmat, lstchem, lsteng]
            cm = ['roll', 'cs', 'phy', 'math', 'chem', 'eng']
            for c in range(6):
                try:
                    cursor.execute('select ' + cm[c] + ' from ' + clas + s)
                except mysql.connector.Error:
                    pass
                cursor.fetchall()
                count = cursor.rowcount
                cursor.execute('select ' + cm[c] + ' from ' + clas + s)
                for i in range(count):
                    a = cursor.fetchone()
                    c_part = 0
                    for cp in a:
                        c_part = cp
                    lstbx[c].insert(i, '{0}'.format(c_part))

        def update():
            sesf = entry_session1.get()
            class_session = clas + sesf.replace(' ', '')

            # Table creation
            try:
                cursor.execute(
                    'create table ' + class_session + '(roll varchar(6),cs varchar(6),math varchar(6),phy varchar(6),'
                                                      'chem varchar(6),eng varchar(6))')
            except mysql.connector.Error:
                pass
            rolf = entry_roll.get()
            csf = entry_cs.get()
            phyf = entry_phy.get()
            mathf = entry_math.get()
            chemf = entry_chem.get()
            engf = entry_eng.get()
            if sesf == '':
                msgb.showinfo('Something went wrong!', 'Session field cannot be empty!')
            elif rolf == '':
                msgb.showinfo('Something went wrong!', 'Roll number field cannot be empty!')
            elif csf == '':
                msgb.showinfo('Something went wrong!', 'CN field cannot be empty!')
            elif phyf == '':
                msgb.showinfo('Something went wrong!', 'Automata field cannot be empty!')
            elif mathf == '':
                msgb.showinfo('Something went wrong!', 'Maths field cannot be empty!')
            elif chemf == '':
                msgb.showinfo('Something went wrong!', 'Web Development field cannot be empty!')
            elif engf == '':
                msgb.showinfo('Something went wrong!', 'DBMS field cannot be empty!')
            else:
                cursor.execute('select roll from ' + class_session)
                dr = cursor.fetchall()
                op = 0
                for a in dr:
                    for b in a:
                        if int(b) == int(rolf):
                            op += 1
                    else:
                        pass
                if op == 1:
                    try:
                        cursor.execute(
                            'update ' + class_session +
                            ' set roll={0},cs={1},math={2},phy={3},chem={4},eng={5} where roll={6}'
                            .format(rolf, csf, mathf, phyf, chemf, engf, rolf))
                        con.commit()
                        msgb.showinfo('Success', 'Data saved successfully at ' + time.ctime())
                    except mysql.connector.Error():
                        msgb.showinfo('We encountered an error!', 'Please contact system administrator!')
                else:
                    try:
                        cursor.execute(
                            'insert into ' + class_session + '(roll,cs,math,phy,chem,eng) values({0},{1},{2},{3},{4},'
                                                             '{5}) '
                            .format(rolf, csf, mathf, phyf, chemf, engf))
                        con.commit()
                        msgb.showinfo('Success', 'Data saved successfully at ' + time.ctime())
                    except mysql.connector.Error():
                        msgb.showinfo('We encountered an error!', 'Please contact system administrator!')

        # Canvas text
        # Misc
        m_canvas.create_text(250, 50, text='VIEW & UPDATE MARKS!', font=('Calibri', 32), fill='white')
        m_canvas.create_text(90, 130, text='SESSION:', font=('Calibri', 22), fill='white')
        m_canvas.create_text(540, 130, text='(Ex. Monthly Test1--mt1)', font=('Calibri', 16), fill='white')
        # Update
        m_canvas.create_text(990, 110, text='UPDATE MARKS!', font=('Calibri', 28), fill='white')
        m_canvas.create_text(942, 170, text='Session:', font=('Calibri', 24), fill='white')
        m_canvas.create_text(940, 230, text='Roll No.:', font=('Calibri', 24), fill='white')
        m_canvas.create_text(865, 290, text='Computer Networks:', font=('Calibri', 24), fill='white')
        m_canvas.create_text(944, 355, text='AUTOMATA:', font=('Calibri', 24), fill='white')
        m_canvas.create_text(905, 415, text='Mathematics:', font=('Calibri', 24), fill='white')
        m_canvas.create_text(925, 475, text='Web Development:', font=('Calibri', 24), fill='white')
        m_canvas.create_text(946, 545, text='DBMS:', font=('Calibri', 24), fill='white')
        # Listbox text
        m_canvas.create_text(95, 185, text='ROLL NO.', font=('Calibri', 16), fill='white')
        m_canvas.create_text(194, 185, text='CN', font=('Calibri', 16), fill='white')
        m_canvas.create_text(295, 185, text='AT', font=('Calibri', 16), fill='white')
        m_canvas.create_text(395, 185, text='Maths', font=('Calibri', 16), fill='white')
        m_canvas.create_text(495, 185, text='Web', font=('Calibri', 16), fill='white')
        m_canvas.create_text(595, 185, text='DBMS', font=('Calibri', 16), fill='white')
        # Entry Boxes
        entry_session1 = Entry(u_m, width=25, bd=4)
        entry_roll = Entry(u_m, width=25, bd=4)
        entry_cs = Entry(u_m, width=25, bd=4)
        entry_phy = Entry(u_m, width=25, bd=4)
        entry_math = Entry(u_m, width=25, bd=4)
        entry_chem = Entry(u_m, width=25, bd=4)
        entry_eng = Entry(u_m, width=25, bd=4)
        entry_session2 = Entry(u_m, width=22, bd=4)
        # Entry Position
        entry_roll.place(x=1020, y=220)
        entry_cs.place(x=1020, y=280)
        entry_phy.place(x=1020, y=345)
        entry_math.place(x=1020, y=405)
        entry_chem.place(x=1020, y=465)
        entry_eng.place(x=1020, y=535)
        entry_session1.place(x=1020, y=160)
        entry_session2.place(x=160, y=119)
        # List boxes
        lstro = Listbox(u_m)
        lstcs = Listbox(u_m)
        lstphy = Listbox(u_m)
        lstmat = Listbox(u_m)
        lstchem = Listbox(u_m)
        lsteng = Listbox(u_m)
        # Listbox configs
        lstro.config(height=14, width=7, font=('Calibri', 18), fg='black', relief='flat', yscrollcommand=scrollbar.set)
        lstcs.config(height=14, width=7, font=('Calibri', 18), fg='black', relief='flat', yscrollcommand=scrollbar.set)
        lstphy.config(height=14, width=7, font=('Calibri', 18), fg='black', relief='flat', yscrollcommand=scrollbar.set)
        lstmat.config(height=14, width=7, font=('Calibri', 18), fg='black', relief='flat', yscrollcommand=scrollbar.set)
        lstchem.config(height=14, width=7, font=('Calibri', 18), fg='black', relief='flat',
                       yscrollcommand=scrollbar.set)
        lsteng.config(height=14, width=7, font=('Calibri', 18), fg='black', relief='flat', yscrollcommand=scrollbar.set)
        # Listbox positions
        lstro.place(x=50, y=200)
        lstcs.place(x=150, y=200)
        lstphy.place(x=250, y=200)
        lstmat.place(x=350, y=200)
        lstchem.place(x=450, y=200)
        lsteng.place(x=550, y=200)

        # Button
        button_update = Button(u_m, text='UPDATE!', font='Calibri', width=12, height=1, activebackground='light green',
                               command=update)
        button_session = Button(u_m, text='SHOW!', font='Calibri', width=12, height=1, activebackground='light green',
                                command=show)
        # Button position
        button_update.place(x=975, y=580)
        button_session.place(x=320, y=115)

        # Scrollbar programming
        def ar_um(*args):
            lstro.yview(*args)
            lstcs.yview(*args)
            lstphy.yview(*args)
            lstmat.yview(*args)
            lstchem.yview(*args)
            lsteng.yview(*args)

        # Scroll bar position
        scrollbar.config(command=ar_um)
        scrollbar.place(x=650, y=201)
        u_m.resizable(0, 0)
        m_canvas.pack()
        u_m.mainloop()

    # Main structure
    admn = Toplevel(top)
    admn.title('Login Successful!')
    # Structure
    # Canvas and background
    cad = Canvas(admn, height=650, width=1300)
    adimg = PhotoImage(file="V:\DBMS\Project_SDBMS[1]\Project SDBMS\img6.png")
    cad.create_image(0, 0, image=adimg, anchor=NW)
    # Total number of students
    cursor.execute('select * from ' + clas)
    cursor.fetchall()
    cn = cursor.rowcount
    # Scrollbar
    scrollbar = Scrollbar(cad)

    def ar(*args):
        lstr.yview(*args)
        lstdob.yview(*args)
        lstad.yview(*args)
        lstn.yview(*args)

    # Text
    cad.create_text(220, 70, text="Welcome!", font=("Calibri", 65), fill='orange')
    cad.create_text(320, 130, text=name.upper(), font=("Calibri", 25, 'bold'), fill='orange')
    cad.create_text(970, 50, text='LOGGED IN AT ' + time.ctime(), font=("Calibri", 20, 'bold'), fill='green')
    cad.create_text(150, 180, text='CLASS: ' + clas, font=("Calibri", 20, 'bold'), fill='white')
    cad.create_text(245, 225, text='TOTAL CLASS STRENGTH:' + str(cn), font=("Calibri", 20, 'bold'), fill='white')
    # Text for student table
    cad.create_text(890, 110, text='Existing student details:', font=('Calibri', 22, 'bold'), fill='green')
    cad.create_text(790, 160, text='Roll No.', font=('Calibri', 17, 'bold'), fill='green')
    cad.create_text(930, 160, text='Name', font=('Calibri', 17, 'bold'), fill='green')
    cad.create_text(1090, 160, text='Admission No.', font=('Calibri', 17, 'bold'), fill='green')
    cad.create_text(1210, 160, text='DOB', font=('Calibri', 17, 'bold'), fill='green')
    # Text for edit commands
    cad.create_text(265, 300, text='To enter new student details:', font=('Calibri', 27), fill='white')
    cad.create_text(220, 360, text='To edit/delete student:', font=('Calibri', 27), fill='white')
    cad.create_text(279, 420, text='To view/update student marks:', font=('Calibri', 27), fill='white')
    # Buttons
    bsd = Button(admn, text="Click Here!", height=1, width=10, activebackground='light green', font='Calibri',
                 command=nsd)
    bdel = Button(admn, text="Click Here!", height=1, width=10, activebackground='light green', font='Calibri',
                  command=up_del)
    bup = Button(admn, text="Click Here!", height=1, width=10, activebackground='light green', font='Calibri',
                 command=update_marks)
    # Button position
    bsd.place(x=550, y=285)
    bdel.place(x=550, y=345)
    bup.place(x=550, y=405)
    # Listbox
    lstr = Listbox(admn)
    lstn = Listbox(admn)
    lstad = Listbox(admn)
    lstdob = Listbox(admn)
    # Listbox Configs
    lstr.config(height=14, width=7, font=('Calibri', 18), fg='black', relief='flat', yscrollcommand=scrollbar.set)
    lstn.config(height=14, width=16, font=('Calibri', 18), fg='black', relief='flat', yscrollcommand=scrollbar.set)
    lstad.config(height=14, width=7, font=('Calibri', 18), fg='black', relief='flat', yscrollcommand=scrollbar.set)
    lstdob.config(height=14, width=12, font=('Calibri', 18), fg='black', relief='flat', yscrollcommand=scrollbar.set)
    # Listbox position
    lstr.place(x=750, y=190)
    lstn.place(x=840, y=190)
    lstad.place(x=1038, y=190)
    lstdob.place(x=1128, y=190)
    # Scrollbar config
    scrollbar.config(command=ar)
    scrollbar.place(x=1280, y=190)

    # Data insertion
    # Roll

    def data_insertion():
        lstr.delete(0, 'end')
        lstad.delete(0, 'end')
        lstn.delete(0, 'end')
        lstdob.delete(0, 'end')
        cm = ['roll', 'StudentName', 'AdmissionNo', 'DOB']
        lst = [lstr, lstn, lstad, lstdob]
        for c in range(4):
            try:
                cursor.execute('select ' + cm[c] + ' from ' + clas)
            except mysql.connector.Error:
                pass
            cursor.fetchall()
            count = cursor.rowcount
            cursor.execute('select ' + cm[c] + ' from ' + clas)
            for i in range(count):
                a = cursor.fetchone()
                c_part = 0
                for cp in a:
                    c_part = cp
                lst[c].insert(i, '{0}'.format(c_part))

    data_insertion()
    admn.resizable(0, 0)
    cad.pack()
    admn.mainloop()


# Student section
def st_reg():
    stsu = Toplevel(top)
    stsu.title('Sign-up')

    def sreg():
        rol = entry_st_roll.get()
        us = entry_st_usn.get()
        pas = entry_st_pass.get()
        clas = entry_st_class.get()
        re_clas = clas.replace(" ", '')
        if rol == '':
            msgb.showinfo('Oops!!', 'Roll number field cannot be empty')
        elif us == '':
            msgb.showinfo('Oops!!', 'Username cannot be empty')
        elif pas == '':
            msgb.showinfo('Oops!!', 'Password field cannot be empty')
        elif re_clas == '':
            msgb.showinfo('Oops!!', 'Class field cannot be empty')
        else:
            cursor.execute('select studentname from ' + re_clas + ' where roll=' + rol)
            name = cursor.fetchone()
            if name is None:
                msgb.showinfo('Something went wrong at ' + time.ctime(), 'Roll number does not exist. '
                                                                         'Please contact class teacher to update your '
                                                                         'roll number')
            else:
                fil_name = ''
                for i in name:
                    fil_name += i
                n = 0
                r = 0
                cursor.execute('select username from senps')
                dat = cursor.fetchall()
                for a in dat:
                    for b in a:
                        if us == b:
                            n += 1
                cursor.execute('select roll from senps')
                rdat = cursor.fetchall()
                for c in rdat:
                    for a in c:
                        if rol == a:
                            r += 1
                if n == 1:
                    msgb.showinfo('Something went wrong at '+time.ctime(), 'Username already taken.')
                elif r == 1:
                    msgb.showinfo('Account already exists.', 'An account has been previously created using this '
                                                             'roll number. Kindly login through existing account')
                elif n == 0:
                    try:
                        cursor.execute(
                            "insert into senps values('{0}','{1}','{2}','{3}','{4}')".format(fil_name, us, pas, re_clas,
                                                                                             rol))
                        con.commit()
                        msgb.showinfo('Success!!', 'Account created successfully at ' + time.ctime())
                        stsu.destroy()
                    except mysql.connector.Error:
                        msgb.showinfo('Something went wrong at ' + time.ctime(), 'Please retry again!')

    # Structure
    st_su = Canvas(stsu, height=520, width=760)
    # Canvas image
    st_img = PhotoImage(file="V:\DBMS\Project_SDBMS[1]\Project SDBMS\img.png")
    st_su.create_image(0, 0, image=st_img, anchor=NW)
    # Canvas text
    st_su.create_text(170, 50, text='Sign-Up', font=('Calibri', 60), fill='light blue')
    st_su.create_text(280, 120, text='Please fill up the following credentials:', font=('Calibri', 22), fill='white')
    st_su.create_text(227, 180, text='Enter class:', font=('Calibri', 28), fill='white')
    st_su.create_text(250, 260, text='Enter Roll No.:', font=('Calibri', 28), fill='white')
    st_su.create_text(266, 330, text='Enter username:', font=('Calibri', 28), fill='white')
    st_su.create_text(264, 400, text='Enter password:', font=('Calibri', 28), fill='white')
    # Entry boxes
    entry_st_class = Entry(st_su, width=25, bd=4)
    entry_st_roll = Entry(st_su, width=25, bd=4)
    entry_st_usn = Entry(st_su, width=25, bd=4)
    entry_st_pass = Entry(st_su, width=25, bd=4)
    # Entry box position
    entry_st_class.place(x=410, y=170)
    entry_st_roll.place(x=410, y=250)
    entry_st_usn.place(x=410, y=320)
    entry_st_pass.place(x=410, y=390)
    # Button
    register = Button(st_su, text='REGISTER!', font='Calibri', width=12, height=1, activebackground='light green',
                      command=sreg)
    register.place(x=325, y=440)
    # Misc
    st_su.pack()
    stsu.resizable(0, 0)
    stsu.mainloop()


def s_ver():
    usn = ensus.get()
    pas = ensps.get()
    cursor.execute('select username from senps')
    dat = cursor.fetchall()
    cn = 0
    for i in dat:
        for a in i:
            if usn == a:
                cn += 1
            else:
                pass
    if cn == 1:
        pa = 0
        cursor.execute("select password from senps where username='{0}'".format(usn))
        pd = cursor.fetchall()
        for b in pd:
            for c in b:
                if pas == c:
                    pa += 1
                else:
                    pass
        if pa == 1:
            cursor.execute("select roll from senps where username='{0}'".format(usn))
            ro = ''
            a = cursor.fetchone()
            for i in a:
                for j in i:
                    ro += j
            spl(ro)
            return ro
        else:
            msgb.showinfo('Something went wrong at ' + time.ctime(), 'Incorrect Password!')
    else:
        msgb.showinfo('Something went wrong at ' + time.ctime(), 'Incorrect Username!')


# Student post login interface
def spl(ro):
    slog = Toplevel(top)
    sli = Canvas(slog, height=690, width=1288)
    slog.title('Login Successful!')
    # Canvas image
    simg = PhotoImage(file='V:\DBMS\Project_SDBMS[1]\Project SDBMS\studentlogimg.png')
    sli.create_image(0, 0, image=simg, anchor=NW)
    # Data
    cursor.execute('select name from senps where roll='+ro)
    name = ''
    d1 = cursor.fetchone()
    for i in d1:
        for j in i:
            name += j
    cursor.execute('select class from senps where roll=' + ro)
    clas = ''
    d2 = cursor.fetchone()
    for i in d2:
        for j in i:
            clas += j
    cursor.execute('select dob from ' + clas + " where roll={0}".format(ro))
    dob = ''
    d3 = cursor.fetchone()
    for i in d3:
        for j in i:
            dob += j
    cursor.execute('select admissionno from ' + clas + " where roll={0}".format(ro))
    d4 = cursor.fetchall()
    admnno = ''
    for i in d4:
        for j in i:
            admnno += str(j)
    # Canvas text
    sli.create_text(250, 70, text="Welcome!", font=("Calibri", 75), fill='orange')
    sli.create_text(1050, 25, text='LOGGED IN AT ' + time.ctime(), font=("Calibri", 20, 'bold'), fill='gold')
    sli.create_text(340, 130, text=name, font=("Calibri", 25, 'bold'), fill='orange')
    sli.create_text(170, 220, text='CLASS: ' + clas, font=("Calibri", 35, 'bold'), fill='yellow')
    sli.create_text(225, 320, text='ROLL NO.: ' + ro, font=("Calibri", 35, 'bold'), fill='Yellow')
    sli.create_text(235, 420, text='DOB: ' + dob, font=("Calibri", 35, 'bold'), fill='yellow')
    sli.create_text(265, 520, text='Admission No.: ' + admnno, font=("Calibri", 35, 'bold'), fill='yellow')
    sli.create_text(800, 155, text='SESSIONS', font=("Calibri", 30), fill='light blue')
    sli.create_text(1102, 155, text='AUTOMATA', font=("Calibri", 30, 'bold'), fill='blue')
    sli.create_text(1102, 270, text='Web Development', font=("Calibri", 30, 'bold'), fill='blue')
    sli.create_text(1102, 375, text='MATHEMATICS', font=("Calibri", 30, 'bold'), fill='blue')
    sli.create_text(1102, 485, text='Computer Networks', font=("Calibri", 30, 'bold'), fill='blue')
    sli.create_text(1102, 600, text='DBMS', font=("Calibri", 30, 'bold'), fill='blue')
    # Scroll bar
    scrollbar = Scrollbar(slog)
    scrollbar.place(x=910, y=180)
    # List boxes
    session = Listbox(slog)
    cs = Listbox(slog)
    phy = Listbox(slog)
    chem = Listbox(slog)
    math = Listbox(slog)
    eng = Listbox(slog)
    # Listbox config
    session.config(height=13, width=12, font=('Calibri', 23), fg='green', relief='flat', yscrollcommand=scrollbar.set)
    phy.config(height=1, width=12, font=('Calibri', 23), fg='green', relief='flat')
    chem.config(height=1, width=12, font=('Calibri', 23), fg='green', relief='flat')
    math.config(height=1, width=12, font=('Calibri', 23), fg='green', relief='flat')
    cs.config(height=1, width=12, font=('Calibri', 23), fg='green', relief='flat')
    eng.config(height=1, width=12, font=('Calibri', 23), fg='green', relief='flat')
    # Listbox position
    session.place(x=710, y=180)
    phy.place(x=1010, y=180)
    chem.place(x=1010, y=290)
    math.place(x=1010, y=400)
    cs.place(x=1010, y=510)
    eng.place(x=1010, y=620)
    # Listbox insertion
    cursor.execute('show tables')
    dat = cursor.fetchall()
    da = cursor.rowcount
    for i in dat:
        for a in i:
            co = len(a)
            if (a[:3]) == clas:
                if co == 3 or co == 2 or a == 'enps' or a == 'senps':
                    pass
                else:
                    d = str(a[3:]).upper()
                    session.insert(da, d)

    def cur(nil):
        value = session.get(session.curselection())
        pr(value)

    def pr(value):
        phy.delete(0, 'end')
        chem.delete(0, 'end')
        math.delete(0, 'end')
        cs.delete(0, 'end')
        eng.delete(0, 'end')
        cursor.execute('select phy from ' + clas + value + " where roll={0}".format(ro))
        pm = cursor.fetchone()
        for phy_mark in pm:
            phy.insert(1, phy_mark)
        cursor.execute('select chem from ' + clas + value + " where roll={0}".format(ro))
        cm = cursor.fetchone()
        for chem_mark in cm:
            chem.insert(1, chem_mark)
        cursor.execute('select math from ' + clas + value + " where roll={0}".format(ro))
        mm = cursor.fetchone()
        for math_mark in mm:
            math.insert(1, math_mark)
        cursor.execute('select cs from ' + clas + value + " where roll={0}".format(ro))
        cm = cursor.fetchone()
        for cs_mark in cm:
            cs.insert(1, cs_mark)
        cursor.execute('select eng from ' + clas + value + " where roll={0}".format(ro))
        em = cursor.fetchone()
        for eng_mark in em:
            eng.insert(1, eng_mark)

    def sc(*args):
        session.yview(*args)

    scrollbar.config(command=sc)
    session.bind('<<ListboxSelect>>', cur)
    slog.resizable(0, 0)
    sli.pack()
    slog.mainloop()


# Structure
# Canvas background
canvas = Canvas(top, width=1200, height=600)
bgi = PhotoImage(file="V:\DBMS\Project_SDBMS[1]\Project SDBMS\logimg.png")
canvas.create_image(0, 0, image=bgi, anchor=NW)
# Canvas text
canvas.create_text(290, 190, text="TEACHER LOGIN:", font=("Calibri", 55), fill='cyan')
canvas.create_text(230, 280, text="Username:", font=("Calibri", 35), fill='white')
canvas.create_text(237, 360, text="Password:", font=("Calibri", 35), fill='white')
# Student login text
canvas.create_text(900, 190, text="STUDENT LOGIN:", font=("Calibri", 55), fill='cyan')
canvas.create_text(800, 280, text="Username:", font=("Calibri", 35), fill='white')
canvas.create_text(807, 360, text="Password:", font=("Calibri", 35), fill='white')
# Time
canvas.create_text(250, 75, text='Session start at ' + time.ctime(), font=("Calibri", 20), fill='white')
canvas.create_text(950, 580, text="Note: Please don't close this window until the end of the session.",
                   font=("Calibri", 13), fill='white')
# Entry boxes
enus = Entry(top, bd=5, width=30)
enpas = Entry(top, bd=5, width=30, show='*')
# Student entry boxes
ensus = Entry(top, bd=5, width=30)
ensps = Entry(top, bd=5, width=30, show='*')
# Entry position
enus.place(x=370, y=270)
enpas.place(x=370, y=350)
ensus.place(x=940, y=270)
ensps.place(x=940, y=350)
# Buttons
lg = Button(top, text="Log-In!", height=1, width=11, activebackground='orange', font='Calibri', command=ver)
su = Button(top, text="Sign-UP!", height=1, width=11, activebackground='orange', font='Calibri', command=sign_up)
stlg = Button(top, text="Log-In!", height=1, width=11, activebackground='orange', font='Calibri', command=s_ver)
strg = Button(top, text="Register!", height=1, width=11, activebackground='orange', font='Calibri', command=st_reg)
# Button position
lg.place(x=400, y=430)
su.place(x=240, y=430)
stlg.place(x=970, y=430)
strg.place(x=810, y=430)
top.resizable(0, 0)
canvas.pack()
top.mainloop()
