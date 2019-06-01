try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter.ttk import *
    from tkinter import *
import sqlite3
conn= sqlite3.connect("NaaSClue_DATABASE.db")

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('starttime', 'endtime', 'status')
        tv.heading("#0", text='Item Name', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('starttime', text='Item ID')
        tv.column('starttime', anchor='center', width=100)
        tv.heading('endtime', text='Quantity')
        tv.column('endtime', anchor='center', width=100)
        tv.heading('status', text='price')
        tv.column('status', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        result=conn.execute("select * from ITEMS ")
        for row in result:
            k1=row[0]
            k2=row[1]
            k3=row[2]
            k4=row[3]
            self.treeview.insert('', 'end', text=k2, values=(k1,k3, k4))


def Customer():

    top1=Tk()
    top1.title('Haettenschweiler')
    top1.configure(background='#141a3a')
    l1=Label(top1,text="Please enter the items name to be searched")
    l1.pack()
    e1=Entry(top1,bd=5)
    rp=e1.get()
    e1.pack()
    def BUT4():
        rp=e1.get()
        c=0
        result=conn.execute("select * from ITEMS where I_NAME=='%s'" % (rp))
        for row in result:
            n=row[1]
            if(n==rp):
                c=1
        if(c==1):
            result1=conn.execute("select * from ITEMS where I_NAME=='%s'" % (rp))
            for row in result1:
                kp=row[2]
            if(kp>=0):
                l2=(Label(top1, bg='grey',font=('Haettenschweiler',20),text="Available %d kg " %(kp)+rp))
                l2.pack()
        else:
            l2=Label(top1, bg='grey',font=('Haettenschweiler',20),text="Sorry "+rp+" is not available")
            l2.pack() 
    b123=Button(top1,padx=5,pady=5,bd=8,text='ENTER',font=('Haettenschweiler',16),command=BUT4,bg='#0a98c9')
    b123.pack()
    top1.mainloop()
   
       
def notice():
    window = Toplevel(top)
    result=conn.execute("select * from ITEMS ")
    pp=0
    Label(window, bg='#0a98c9',font=('Haettenschweiler',20),height=2,width=25,text="OUT OF STOCK LIST").pack()
    for row in result:
        if(row[2]==0):
            k=row[1]
            pp=pp+1
            Label(window, bg='red',font=('Haettenschweiler',20),height=1,width=25,text="%d."%(pp)+k+" not available").pack()

def Management():
    top1=Tk()
    top1.title('Management')
    top1.configure(background='#141a3a')
    def Check_s():
        top11=Tk()
        top1.configure(background='#141a3a')
        result=conn.execute("select * from ITEMS ")
        Label(top11, bg='#0a98c9',font=('Haettenschweiler',20),height=5,width=50,text="OUT OF STOCK").pack()
        for row in result:
            if(row[2]<=10):
                Kk=row[1]
                Label(top11, bg='#0a98c9',font=('Haettenschweiler',20),height=5,width=50,text=Kk+" few left reorder soon").pack()
        top11.mainloop()
    def Restock():
        def BUT4():
            r=int(e1.get())
            r1=int(e11.get())
            conn.execute("UPDATE ITEMS SET QUANTITY=%d WHERE I_ID==%d" % (r1,r))
            #l2=Label(top1,text=r)
            l2=Label(top1, bg='grey',font=('Haettenschweiler',20),text="SUCCESSFULLY UPDATED")
            l2.pack()
            print(r)
        top1=Tk()
        top1.title('Restock')
        top1.configure(background='#141a3a')
        l1=Label(top1,text="Please enter the items ID")
        #l1.grid(row=0,column=0)
        l1.pack()
        e1=Entry(top1,bd=5)
        #e1.grid(row=0,column=1)
        r=e1.get()
        e1.pack()
        l11=Label(top1,text="Please enter the items quantity")
        #l11.grid(row=0,column=0)
        l11.pack()
        e11=Entry(top1,bd=5)
        #e1.grid(row=0,column=1)
        r1=e11.get()
        e11.pack()
        b123=Button(top1,padx=0,pady=0,bd=8,text='Enter',font=('Haettenschweiler',16),command=BUT4,bg='#0a98c9')
        b123.pack(side='left')
        top1.mainloop()
        
    def insert():
        def BUT4():
            i=int(e1.get())
            n=e11.get()
            q=int(e2.get())
            p=int(e22.get())
            conn.execute("INSERT INTO ITEMS (I_ID,I_NAME,QUANTITY,PRICE) VALUES (?,?,?,?)",(i,n,q,p));
            #l2=Label(top1,text=r)
            l2=Label(top1, bg='grey',font=('Haettenschweiler',20),text="SUCCESSFULLY UPDATED")
            l2.pack()
        top1=Tk()
        top1.title('Restock')
        top1.configure(background='#141a3a')
        l1=Label(top1,text="Please enter the items ID")
        #l1.grid(row=0,column=0)
        l1.pack()
        e1=Entry(top1,bd=5)
        #e1.grid(row=0,column=1)
        i=e1.get()
        e1.pack()
        l11=Label(top1,text="Please enter the item's name")
        #l11.grid(row=0,column=0)
        l11.pack()
        e11=Entry(top1,bd=5)
        #e1.grid(row=0,column=1)
        n=e11.get()
        e11.pack()
        l2=Label(top1,text="Please enter the item's quantity")
        #l1.grid(row=0,column=0)
        l2.pack()
        e2=Entry(top1,bd=5)
        #e1.grid(row=0,column=1)
        q=e2.get()
        e2.pack()
        l22=Label(top1,text="Please enter the item's price")
        #l11.grid(row=0,column=0)
        l22.pack()
        e22=Entry(top1,bd=5)
        #e1.grid(row=0,column=1)
        p=e22.get()
        e22.pack()
        b123=Button(top1,padx=0,pady=0,bd=8,text='Enter',font=('Haettenschweiler',16),command=BUT4,bg='#0a98c9')
        b123.pack(side='left')
        top1.mainloop()
    def Reorder():
        top1=Tk()
        top1.title('Recorder')
        top1.configure(background='#141a3a')
        App(top1)
        top1.mainloop()

    bb1=Button(top1,padx=5,pady=5,bd=8,text='Check Stock',font=('Haettenschweiler',16),command=Check_s,bg='#0a98c9')
    bb1.grid(row=1,column=1)
    bb1.config(width=60,height=2)
    bb2=Button(top1,padx=5,pady=5,bd=8,text='Restock',font=('Haettenschweiler',16),command=Restock,bg='#0a98c9')
    bb2.grid(row=2,column=1)
    bb2.config(width=60,height=2)
    bb33=Button(top1,padx=5,pady=5,bd=8,text='insert',font=('Haettenschweiler',16),command=insert,bg='#0a98c9')
    bb33.grid(row=3,column=1)
    bb33.config(width=60,height=2)
    bb3=Button(top1,padx=5,pady=5,bd=8,text='View Database',font=('Haettenschweiler',16),command=Reorder,bg='#0a98c9')
    bb3.grid(row=4,column=1)
    bb3.config(width=60,height=2)
    top1.mainloop()
    
    
    
def Cashier():
    def BUT4():
        r=int(e1.get())
        r1=int(e11.get())
        result=conn.execute("select * from ITEMS ")
        for row in result:
            if(int(row[0])==r):
                k2=int(row[2])
        if((k2-r1)>=0):
            conn.execute("UPDATE ITEMS SET QUANTITY=%d WHERE I_ID==%d" % (k2-r1,r))
            #l2=Label(top1,text=r)
            l2=Label(top1, bg='grey',font=('Haettenschweiler',20),text="SUCCESSFULLY UPDATED")
            l2.pack()
        else:
            #k3=r1-k2
            l2=(Label(top1, bg='grey',font=('Haettenschweiler',20),text="only %d kg available" %(k2)))
            l2.pack()
        print(r)
    top1=Tk()
    top1.title('Cashier')
    top1.configure(background='#141a3a')

    
    l1=Label(top1,text="Please enter the items' ID that is to be purchased ")
    #l1.grid(row=0,column=0)
    l1.pack()
    e1=Entry(top1,bd=5)
    #e1.grid(row=0,column=1)
    r=e1.get()
    e1.pack()
    l11=Label(top1,text="Please enter the items quantity that isto be purchased ")
    #l11.grid(row=0,column=0)
    l11.pack()
    e11=Entry(top1,bd=5)
    #e1.grid(row=0,column=1)
    r1=e11.get()
    e11.pack()
    b123=Button(top1,padx=0,pady=0,bd=8,text='Enter',font=('Haettenschweiler',16),command=BUT4,bg='#0a98c9')
    b123.pack(side='left')
    top1.mainloop()
    
def BUT5():
    window = Toplevel(top)
    b111=Button(top,padx=5,pady=5,bd=8,text='Customer',font=('Haettenschweiler',16),command=BUT4,bg='#0a98c9')
    b111.grid(row=1,column=1)
    b111.config(width=60,height=2)

def db():
    top1=Tk()
    top1.title('Cashier')
    top1.configure(background='#141a3a')
    K=0
    try:
        conn.execute("CREATE TABLE ITEMS(I_ID INT PRIMARY KEY NOT NULL,I_NAME TEXT NOT NULL,QUANTITY INT NOT NULL,PRICE INT NOT NULL);")
    except:
        Label(top1, bg='#0a98c9',font=('Haettenschweiler',20),height=10,width=50,text="DATABASE ALREADY CREATED").pack()
        K=1
    if(K!=1):
        Label(top1, bg='#0a98c9',font=('Haettenschweiler',20),height=10,width=50,text="DATABASE CREATED").pack()

top=Tk()
top.title('NaaSClue')
top.configure(background='#141a3a')

#App(top)
label=Label(top,bd=30,anchor=CENTER,text='WELCOME TO NaaSClue',fg='#cfd0d5',bg='#141a3a',font=('Agency FB Bold',60))
label.grid(row=0,column=2)


b1=Button(top,padx=3,pady=3,bd=40,text='PRODUCT SEARCH',font=('Haettenschweiler',20),command=Customer,bg='#0a98c9')
b1.grid(row=2,column=2)
b1.config(width=40,height=1)
b2=Button(top,padx=5,pady=5,bd=40,text='MANAGEMENT',font=('Haettenschweiler',20),command=Management,bg='#0a98c9')
b2.grid(row=3,column=2)
b2.config(width=40,height=1)

b3=Button(top,padx=5,pady=5,bd=40,text='CASHIER',font=('Haettenschweiler',20),command=Cashier,bg='#0a98c9')
b3.grid(row=4,column=2)
b3.config(width=40,height=1)


b4=Button(top,padx=5,pady=5,bd=40,text='CREATE DB',font=('Haettenschweiler',20),command=db,bg='#0a98c9')
b4.grid(row=5,column=2)
b4.config(width=40,height=1)




b11=Button(top,text='NOTIFICATIONS',bd=10,font=('ARIAL BLACK',18),bg='#6d6e74',fg='#000000',command=notice)
b11.grid(row=3,column=5)
b11.config(width=15,height=2)
top.mainloop()

