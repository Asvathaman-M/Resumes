import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os

path=os.environ["userprofile"]
try:
    os.mkdir(path+"\\Documents\\PyBank Database")
except FileExistsError:
    pass

con = sqlite3.connect(path+"\\Documents\\PyBank Database\\Database.db")
cur = con.cursor()

cur.execute("create table if not exists account  (Name char(100) NOT NULL, Acc_no varchar(10) NOT NULL UNIQUE, Ph_no int(10) NOT NULL UNIQUE, Email_id varchar(100) NOT NULL UNIQUE)")
cur.execute("create table if not exists balance (Acc_no INTEGER NOT NULL UNIQUE, Balance varchar(40) NOT NULL, Name char(100) NOT NULL, Pin varchar(4) NOT NULL)")


cur.execute("select max(Acc_no) from account ")
"""for acc in cur:
    x=acc[0]
    y=int(x)+1
    acc_no_def=y
""" 
def main_window():

    def return_home(window):
        window.destroy()
        main_window()

    def closer(s):
        s.destroy()

    def new_user():
        win.destroy()
        def check1():
            Hello = (ent_name.get(),ent_ph_no.get(),ent_email_id.get(),ent_pin.get(),ent_balance.get())
            N = 0
            for i in range(5):
                if not Hello[i]:
                    N =  N+1
            if N == 5:
                messagebox.showinfo("Invalid","No details have been entered")
            elif N < 5 and N > 0:
                messagebox.showinfo("Invalid","Enter All the details\nto proceed")

            else:
                if ent_name.get().isalpha() and str(ent_ph_no.get()).isdigit() and str(ent_pin.get()).isdigit() and str(ent_balance.get()).isdigit() is True:
                    exc()
                elif ent_name.get().isalpha() and str(ent_ph_no.get()).isdigit() and str(ent_pin.get()).isdigit() and str(ent_balance.get()).isdigit() is False:
                    messagebox.showerror("Error","Invalid datatype")


        def exc():
            e_n=ent_name.get()
            e_p=ent_ph_no.get()
            e_em=ent_email_id.get()
            e_pn=ent_pin.get()
            #e_acc=ent_acc_no.get()
            e_b=ent_balance.get()
            
            global acc_no_def
            gvn_acc_no=acc_no_def
        
        

            try:
                cur.execute("insert into account values('{}','{}','{}','{}')".format(e_n,gvn_acc_no,e_p,e_em))
                cur.execute("insert into balance values('{}','{}','{}','{}')".format(gvn_acc_no,e_b,e_n,e_pn))
                con.commit()
                messagebox.showinfo("Message","Account sucessesfully created")
                messagebox.showinfo("Important Information","your account no is = '{}' . kindly note it down for further transactions!".format(gvn_acc_no))
                return_home(win1)
            except Exception as e:
                messagebox.showinfo('Invalid',e)


        win1 = Tk()
        win1.geometry("365x300")
        win1.title("Create your Account")
        
        name = Label(win1,text = "Enter your Name ")
        name.place(x = 30,y = 10)
        
        ph_no = Label(win1,text = "Enter your Phone Number ")
        ph_no.place(x = 30,y = 40)
        
        email_id = Label(win1,text = 'Enter your E-mail id ')
        email_id.place(x = 30,y = 70)
        
        pin = StringVar()
        pin = Label(win1,text = "Enter a new 4-digit pin ")
        pin.place(x = 30,y = 100)
        
        #acc_no = Label(win1,text="enter your account no ")
        #acc_no.place(x = 30,y = 130)

        balance = Label(win1,text='Enter your intial balance ')
        balance.place(x = 30,y = 130)
        
        ent_name=Entry(win1)
        ent_ph_no=Entry(win1)
        ent_email_id=Entry(win1)
        ent_pin=Entry(win1,show="*")
        #ent_acc_no=Entry(win1)
        ent_balance=Entry(win1)
        
        ent_name.place(x = 200,y = 10)
        ent_ph_no.place(x = 200,y = 40) 
        ent_email_id.place(x = 200,y = 70)
        ent_pin.place(x = 200,y = 100)
        #ent_acc_no.place(x = 200,y = 130)
        ent_balance.place(x = 200,y = 130)
        #global acc_no_def
        #gvn_acc_no=acc_no_def+1
        
        #messagebox.showinfo("Important Information","your account no is = '{}' . kindly note it down for further transactions!".format(gvn_acc_no))
       
        crtacc=Button(win1,text='Create',command= check1 ,bd = 5,width = 6).place(x=45,y=220)
        Back = Button(win1, text = 'Back', command = lambda: return_home(win1),bd = 5,width = 5).place(x = 200, y = 220)
        win1.mainloop()
    
    
        
    def contnue():
        win.destroy()

        def func1():

            def Logout(x):
                messagebox.showinfo("Info","You have sucessesfully\nLoged out")
                x.destroy()
                main_window()
            
            global path    
            win2.destroy()

            win3 = Tk()
            win3.geometry("400x370")
            win3.title("FUNCTION TO PROCEED")
            win3.resizable(height=False,width=False)

            img=Image.open(path+r"\Downloads\finding-sunshine.jpg")
            img=img.resize((400,400), Image.ANTIALIAS)
            img1=ImageTk.PhotoImage(img)

            lab=Label(win3,image=img1)
            lab.pack()

            dep = Button(win3,text = 'Deposit',command = add, width = 16, bd = 7)
            wid = Button(win3,text = 'Withdraw',command = sub, bd = 7, width = 16)
            trnc = Button(win3,text = 'Account Tansaction', command = trnsfr, bd = 7, width = 16)
            blnc = Button(win3, text = "Balance", command = show, bd = 7, width = 16)
            logout = Button(win3, text = "Logout", command = lambda:Logout(win3), bd = 7)

            dep.place(x=10 , y = 45)
            wid.place(x=255,y=45)
            trnc.place(x=10,y=245)
            blnc.place(x = 255, y = 245)
            logout.pack(fill = 'x', side = 'bottom')

            win3.mainloop()

            

        def check():
            a = (ent_name.get(),ent_acc_no.get(),ent_pin_no.get())
            n = 0
            for i in range(3):
                if not a[i]:
                    n = n+1

            if n == 0:

                if str(ent_pin_no.get()).isdigit() and ent_name.get().isalpha() and str(ent_acc_no.get()).isdigit() is True:

                    with open("Temp.txt",'w+') as f:
                        f.write(ent_acc_no.get())
                    
                    cur.execute("select * from balance where Acc_no = {}".format(ent_acc_no.get()))

                    for i in cur:
                        name = i[2]
                        pin = i[3]

                    if ent_name.get() == name:

                        if str(ent_pin_no.get()) == pin:
                            func1()

                        else:
                            messagebox.showinfo("Import","Pin does  not Match")

                    else:
                        messagebox.showinfo("Warning","No name found")

                elif str(ent_pin_no.get()).isdigit() and str(ent_name.get()).isalpha() and str(ent_acc_no.get()).isdigit() is False:
                    messagebox.showinfo("Warning","The values you entered\n are not in correct datatype")
                
                else:
                    messagebox.showinfo("Message","No rocords found")
            
            elif n==1:
                messagebox.showinfo("Warning","one of the field\n is empty")
            
            elif n==2:
                messagebox.showinfo("Warning","Two fields are empty")
            
            else:
                messagebox.showinfo("Warning","No values Entered")

            
            
        def add():
        
            def cnfrm1():
                en_pn=ent_pin.get()
                en_amt=ent_amt.get()

                d = (ent_pin.get(),ent_amt.get())
                n = 0

                with open("Temp.txt") as f:
                    e_acc = f.read()
                cur.execute("select Pin from balance where acc_no='{}'".format(e_acc))
                for i in cur:
                    for j in i:
                        pin2=j

                for a in range(2):
                    if not d[a]:
                        n = n+1

                if n == 2:
                    messagebox.showwarning('Info','Fields are Empty')
                elif n == 1:
                    messagebox.showinfo('Info',"Don't leave the field Empty")
                elif str(en_pn) != str(pin2):
                    messagebox.showwarning('Info','Incorrect PIN entered Aborting>>>>')
                    win4.destroy()
                elif str(en_pn)==str(pin2):
                    cur.execute("update balance set balance=balance+'{}' where acc_no='{}'".format(en_amt,e_acc))
                    messagebox.showinfo("sucesses","{} has been deposited".format(en_amt))
                    win4.destroy()
                    con.commit()
                else:
                    messagebox.showerror("Exception", Exception)


           
            win4 = Tk()
            win4.geometry("250x150")
            win4.title("Deposit")
        
            pin = Label(win4,text = "Enter your pin ")
            amt = Label(win4,text = 'Enter your ammount')
        
            ent_pin=Entry(win4,show="*")
            ent_amt=Entry(win4)
        
            pin.grid(row=3,column=0)
            amt.grid(row=4,column=0)
      
            ent_pin.grid(row=3,column=1)
            ent_amt.grid(row=4,column=1)
        
            cnf1 = Button(win4, text = 'Submit', command=cnfrm1).place(x = 10, y = 80)
            
        def sub():

            def cnfrm2():
                en_amt=ent_amt.get()
                en_pn=ent_pin.get()

                d = (ent_amt.get(),ent_pin.get())

                n = 0

                with open("Temp.txt") as f:
                    e_acc = f.read()
                cur.execute("select Pin from balance where acc_no='{}'".format(e_acc))
                for i in cur:
                    for j in i:
                        pin2=j
                
                for a in range(2):
                    if not d[a]:
                        n = n+1

                if n == 2:
                    messagebox.showinfo('Info','Fields are Empty')
                elif not ent_pin.get():
                    messagebox.showinfo('Info',"Don't leave the\npin field Empty")
                elif str(ent_pin.get()).isdigit() and str(ent_amt.get()).isdigit() is False:
                    messagebox.showinfo('Info','PIN and Amount\nshould be in Number')
                elif str(en_pn)==str(pin2):
                    cur.execute("update balance set balance=balance-'{}' where acc_no='{}'".format(en_amt,e_acc))
                    messagebox.showinfo("sucesses","{} has been withdraw".format(en_amt))
                    con.commit()
                    win5.destroy()
                elif str(en_pn) != str(pin2):
                    messagebox.showinfo('Info','<<<<<incorrect pin entered aborting>>>>')
                    win5.destroy()
                else:
                    messagebox.showinfo('Message','<<<<Not encountered Error>>>>\nAborting')

            win5 = Tk()
            win5.geometry("250x150")
            win5.title("Withdraw")
        
        
            pin = Label(win5,text = "Enter your pin ")
            amt = Label(win5,text = 'Enter your ammount')
        
        
        
            ent_pin=Entry(win5,show="*")
            ent_amt=Entry(win5)
        
            pin.grid(row=3,column=0)
            amt.grid(row=4,column=0)
     
            ent_pin.grid(row=3,column=1)
            ent_amt.grid(row=4,column=1)
            
            cnf2=Button(win5,text='submit',command=cnfrm2).place(x=10,y=80) 
            
        def trnsfr():

            def cnfrm3():
                en_pn = ent_pin.get()
                en_amt = ent_amt.get()
                en_acc2 = ent_acc_no2.get()



                with open("Temp.txt") as f:
                    e_acc = f.read()
                cur.execute("select Pin from balance where acc_no='{}'".format(e_acc))

                for i in cur:
                    for j in i:
                        pin2=j

                for a in range(2):
                    a=a+0
                if str(en_acc2) == str(e_acc):
                    messagebox.showerror()
                elif str(en_pn)==str(pin2):
                    cur.execute("update balance set balance=balance-'{}' where acc_no='{}'".format(en_amt,e_acc))
                    cur.execute("update balance set balance=balance+'{}' where acc_no='{}'".format(en_amt,en_acc2))
                    con.commit()
                elif not ent_amt.get():
                    messagebox.showinfo('Invalid','Amount must be Entered')
                elif not ent_pin.get():
                    messagebox.showwarning("Invalid","PIN must be Entered")
                elif str(en_pn) != str(pin2):
                    messagebox.showerror('Error','Incorrect PIN entered')
                    win6.destroy()
            
            win6 = Tk()
            win6.geometry("400x400")
            win6.title("Transaction")
        
            
            amt = Label(win6,text = 'Enter your ammount')
            acc_no2= Label(win6,text='Enter recievers account number')
            pin = Label(win6, text = "Enter your PIN")
                    
            ent_acc_no2=Entry(win6)
            ent_amt=Entry(win6)
            ent_pin = Entry(win6,show = '*')
        
            acc_no2.grid(row=2,column=0)
            amt.grid(row=4,column=0)
            ent_acc_no2.grid(row=2,column=2)
            ent_amt.grid(row=4,column=2)
            pin.grid(row = 6, column = 0)
            ent_pin.grid(row = 6, column = 2)


            cnf3=Button(win6,text='submit',command=cnfrm3).place(x=10,y=80) 

        def show():
            
            def verify():
                with open("Temp.txt") as f:
                    a = f.read()

                cur.execute("select Pin from balance where Acc_no = {}".format(a))
                for i in cur:
                    for j in i:
                        vpin = j

                if pin_v_ent.get() == vpin:
                    cur.execute("select Balance from balance where Acc_no = {}".format(a))
                    for a in cur:
                        for b in a:
                            king = b
                    messagebox.showinfo("Balance","Your Account Balance is {}".format(b))
                    window.destroy()

                elif not pin_v_ent.get():
                    messagebox.showwarning("Field is Empty","Enter the PIN to proceed")
                    window.destroy()

                elif pin_v_ent.get() != vpin:
                    messagebox.showerror("Warning","PIN does not Match")
                    window.destroy()



            window = Tk()
            window.geometry("250x150")
            window.title("Verification")

            pin_v = Label(window, text = "Enter your PIN for Verification")
            pin_v_ent = Entry(window, show = "*")
            pin_b = Button(window, text = "Submit", command = verify)

            pin_v.pack()
            pin_v_ent.pack()
            pin_b.pack()

            window.mainloop()

            
        
        win2 = Tk()
        win2.geometry("300x200")
        win2.title("Login Page")
        
        name = Label(win2,text = "Enter your Name: ")
        acc_no = Label(win2,text="Enter your account no")
        pin_no = Label(win2, text = "Enter your 4-Digit Pin")
       
        name.place(x = 10,y = 10)
        acc_no.place(x = 10,y = 40)
        pin_no.place(x = 10,y = 70)
            
        ent_name=Entry(win2)  
        ent_acc_no=Entry(win2)
        ent_pin_no = Entry(win2,show = '*')
        
        ent_name.place(x = 150,y = 10 )
        ent_acc_no.place(x = 150,y = 40 )
        ent_pin_no.place(x = 150,y = 70 )

        
        contu=Button(win2, text = 'Login', command = check,bd = 7 ).place(x=50,y=150)
        Back = Button(win2, text = 'Back', command = lambda: return_home(win2), bd = 7).place(x = 200, y = 150)
        
        win2.mainloop()

    global path

    win = Tk()
    win.title("Welcome to PyBank")
    win.geometry("400x250")
    win.resizable(height=False,width=False)

    img=Image.open(path+r"\Downloads\bank 1st pic.jpg")
    img=img.resize((400,210), Image.ANTIALIAS)
    img1=ImageTk.PhotoImage(img)

    lab=Label(win,image=img1)
    lab.pack()

    new_user = Button(win, text = 'Create New User', command = new_user, bd = 7)
    old_user = Button(win, text = 'Login', command = contnue, width=10,  bd = 7)
    Button(win, text="Quit", command=win.destroy, bd = 7).pack(fill = 'x', side = 'bottom')

    new_user.place(x=45, y=50)
    old_user.place(x=45,y=100)

    win.mainloop()

main_window()

