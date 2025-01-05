from tkinter import*
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter


class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1366x768+0+0")
        
        # ================================Veriable=====================================================
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.adddress1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.duedate_var=StringVar()
        self.daysofbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=15,relief=RIDGE,font=("times new roman",43,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=9,relief=RIDGE,padx=15,bg="powder blue")
        frame.place(x=0,y=105,width=1366,height=370)
        
        # =================================Frame Left ======================================================
        dataframeLeft=LabelFrame(frame,text="LIBRARY MEMBER INFORMATION",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"))
        dataframeLeft.place(x=0,y=5,width=780,height=330)
        
        lblMember=Label(dataframeLeft,bg="powder blue",text="Memeber Type:",font=("arial",12,"bold"),padx=1,pady=4)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(dataframeLeft,font=("arial",12,"bold"),textvariable=self.member_var,width=20,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)
        
        lblPRN_No=Label(dataframeLeft,font=("arial",12,"bold"),text="PRN No :",padx=1,pady=2,bg="powder blue")
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_no=Entry(dataframeLeft,font=("arial",12),textvariable=self.prn_var,width=22)
        txtPRN_no.grid(row=1,column=1)
        
        lblTitle=Label(dataframeLeft,font=("arial",12,"bold"),text="ID No :",padx=1,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(dataframeLeft,font=("arial",12),textvariable=self.id_var_var,width=22)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(dataframeLeft,font=("arial",12,"bold"),text="First Name :",padx=1,pady=4,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(dataframeLeft,font=("arial",12),textvariable=self.firstname_var,width=22)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(dataframeLeft,font=("arial",12,"bold"),text="Last Name :",padx=1,pady=4,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(dataframeLeft,font=("arial",12),textvariable=self.lastname_var,width=22)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(dataframeLeft,font=("arial",12,"bold"),text="Address 1 :",padx=1,pady=4,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(dataframeLeft,font=("arial",12),textvariable=self.adddress1_var,width=22)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(dataframeLeft,font=("arial",12,"bold"),text="Address 2 :",padx=1,pady=4,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(dataframeLeft,font=("arial",12),textvariable=self.address2_var,width=22)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(dataframeLeft,font=("arial",12,"bold"),text="Post Code :",padx=1,pady=4,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostcode=Entry(dataframeLeft,font=("arial",12),textvariable=self.postcode_var,width=22)
        txtPostcode.grid(row=7,column=1)
        
        lblMobile=Label(dataframeLeft,font=("arial",12,"bold"),text="Mobile No :",padx=1,pady=4,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(dataframeLeft,font=("arial",12),textvariable=self.mobile_var,width=22)
        txtMobile.grid(row=8,column=1)
        
        lblBookId=Label(dataframeLeft,font=("arial",12,"bold"),text="Book ID :",padx=1,pady=4,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(dataframeLeft,font=("arial",12),textvariable=self.bookid_var,width=22)
        txtBookId.grid(row=0,column=3)
        
        lblBooktitle=Label(dataframeLeft,font=("arial",12,"bold"),text="Book Title :",padx=1,pady=4,bg="powder blue")
        lblBooktitle.grid(row=1,column=2,sticky=W)
        txtBooktitle=Entry(dataframeLeft,font=("arial",12),textvariable=self.booktitle_var,width=22)
        txtBooktitle.grid(row=1,column=3)
        
        lblAuther=Label(dataframeLeft,font=("arial",12,"bold"),text="Book Auther :",padx=1,pady=4,bg="powder blue")
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(dataframeLeft,font=("arial",12),textvariable=self.auther_var,width=22)
        txtAuther.grid(row=2,column=3)
        
        
        lblBorrowedDate=Label(dataframeLeft,font=("arial",12,"bold"),text="Borrowed Date:",padx=1,pady=4,bg="powder blue")
        lblBorrowedDate.grid(row=3,column=2,sticky=W)
        txtBorrowedDate=Entry(dataframeLeft,font=("arial",12),textvariable=self.dateborrowed_var,width=22)
        txtBorrowedDate.grid(row=3,column=3)
        
        lblDueDate=Label(dataframeLeft,font=("arial",12,"bold"),text="Due Date :",padx=1,pady=4,bg="powder blue")
        lblDueDate.grid(row=4,column=2,sticky=W)
        txtDueDate=Entry(dataframeLeft,font=("arial",12),textvariable=self.duedate_var,width=22)
        txtDueDate.grid(row=4,column=3)
        
        
        lblDaysOnBook=Label(dataframeLeft,font=("arial",12,"bold"),text="Days On Book :",padx=1,pady=4,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(dataframeLeft,font=("arial",12),textvariable=self.daysofbook_var,width=22)
        txtDaysOnBook.grid(row=5,column=3)
        
        lblreturn=Label(dataframeLeft,font=("arial",12,"bold"),text="Late Return Fine :",padx=1,pady=4,bg="powder blue")
        lblreturn.grid(row=6,column=2,sticky=W)
        txtreturn=Entry(dataframeLeft,font=("arial",12),textvariable=self.lateratefine_var,width=22)
        txtreturn.grid(row=6,column=3)
        
        lbloverdue=Label(dataframeLeft,font=("arial",12,"bold"),text="Over Due Date :",padx=1,pady=4,bg="powder blue")
        lbloverdue.grid(row=7,column=2,sticky=W)
        txtoverdue=Entry(dataframeLeft,font=("arial",12),textvariable=self.dateoverdue_var,width=22)
        txtoverdue.grid(row=7,column=3)
        
        
        lblPrice=Label(dataframeLeft,font=("arial",12,"bold"),text="Actual Price :",padx=1,pady=4,bg="powder blue")
        lblPrice.grid(row=8,column=2,sticky=W)
        txtPrice=Entry(dataframeLeft,font=("arial",12),textvariable=self.finalprice_var,width=22)
        txtPrice.grid(row=8,column=3)
        
        # ====================================Right Frame==============================================
        
        dataframeRight=LabelFrame(frame,bd=12,padx=15,relief=RIDGE,bg="powder blue",
                                  font=("arial",12,"bold"),text="Book Details")
        dataframeRight.place(x=790,y=5,width=510,height=330)
        
        self.txtBox=Text(dataframeRight,font=("arial",12,"bold"),width=30,height=15,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollBar=Scrollbar(dataframeRight)
        listScrollBar.grid(row=0,column=1,sticky="ns") ## ns= north south
        
        Listbook=["Clean Code","Code Complete","Design Patterns:Elements of reuseable Object-Oriented Software","Effective Java",
                  "Introduction to Algorithms","The Pragmatic Programmer","Refactoring:Improving the design of existing Code",
                  "Haed Fist Design Patterns","Code: The hiiden Language of Computer Hardware & Software",
                  "Structure and Tnterpretation of Computer Programs","Eloquent Javascript","Python Crash Course","Javascript: The Good Part","Domain-Driven Design","Thinking In Java"]
        
        
        def SelectBook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if(x=="Clean Code"):
                self.bookid_var.set("BKID101")
                self.booktitle_var.set("Clean Code")
                self.auther_var.set("Robert C. Martin")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.699")
                
            elif(x=="Code Complete"):
                self.bookid_var.set("BKID102")
                self.booktitle_var.set("Code Complete")
                self.auther_var.set("Steve McConnell")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.1500")
                
            elif(x=="Design Patterns:Elements of reuseable Object-Oriented Software"):
                self.bookid_var.set("BKID103")
                self.booktitle_var.set("Design Patterns:Elements of reuseable Object-Oriented Software")
                self.auther_var.set("Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides (Gang of Four)")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
                
            elif(x=="Effective Java"):
                self.bookid_var.set("BKID104")
                self.booktitle_var.set("Effective Java")
                self.auther_var.set("Joshua Bloch")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
                
            elif(x=="Introduction to Algorithms"):
                self.bookid_var.set("BKID105")
                self.booktitle_var.set("Introduction to Algorithms")
                self.auther_var.set("Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
                
            elif(x=="The Pragmatic Programmer"):
                self.bookid_var.set("BKID106")
                self.booktitle_var.set("The Pragmatic Programmer")
                self.auther_var.set("Andrew Hunt and David Thomas")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
                
            elif(x=="Refactoring:Improving the Design of Existing Code"):
                self.bookid_var.set("BKID107")
                self.booktitle_var.set("Refactoring: Improving the Design of Existing Code")
                self.auther_var.set("Martin Fowler")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
            
            elif(x=="Head First Design Patterns" ):
                self.bookid_var.set("BKID108")
                self.booktitle_var.set("Head First Design Patterns")
                self.auther_var.set("Eric Freeman, Elisabeth Robson, Bert Bates, and Kathy Sierra")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
                
            elif(x=="Code:The Hidden Language of Computer Hardware and Software"):
                self.bookid_var.set("BKID109")
                self.booktitle_var.set("Code:The Hidden Language of Computer Hardware and Software")
                self.auther_var.set("Charles Petzold")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
                
            elif(x=="Structure and Interpretation of Computer Programs"):
                self.bookid_var.set("BKID110")
                self.booktitle_var.set("Structure and Interpretation of Computer Programs")
                self.auther_var.set("Harold Abelson and Gerald Jay Sussman")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
                
                
            elif(x=="Eloquent JavaScript"):
                self.bookid_var.set("BKID111")
                self.booktitle_var.set("Eloquent JavaScript")
                self.auther_var.set("Marijn Haverbeke")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
                
            elif(x=="Python Crash Course"):
                self.bookid_var.set("BKID112")
                self.booktitle_var.set("Python Crash Course")
                self.auther_var.set("Eric Matthes")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
                
            elif(x=="JavaScript:The Good Parts"):
                self.bookid_var.set("BKID113")
                self.booktitle_var.set("JavaScript:The Good Parts")
                self.auther_var.set("Douglas Crockford")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
            
            elif(x=="Domain-Driven Design"):
                self.bookid_var.set("BKID114")
                self.booktitle_var.set("Domain-Driven Design")
                self.auther_var.set("Eric Evans")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
                
            elif(x=="Thinking in Java"):
                self.bookid_var.set("BKID115")
                self.booktitle_var.set("Thinking in Java")
                self.auther_var.set("Bruce Eckel")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d2)
                self.daysofbook_var.set(15)
                self.lateratefine_var.set("Rs.45")
                self.dateborrowed_var.set("No")
                self.finalprice_var.set("Rs.899")
        
        
        
        
        listbox=Listbox(dataframeRight,font=("arial",12,"bold"),width=18,height=15)
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0,column=0,padx=4)
        listScrollBar.config(command=listbox.yview)
        
        for item in Listbook:
            listbox.insert(END,item)
        # ==================================Button frame ==============================================
        
        frameButton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameButton.place(x=0,y=475,width=1366,height=70)
        
        btnaddData=Button(frameButton,command=self.add_data,text="Add Data",font=("arial",16,"bold"),width=15,bg="blue",fg="white")
        btnaddData.grid(row=0,column=0)
        
        btnaddData=Button(frameButton,command=self.Show_data,text="Show Data",font=("arial",16,"bold"),width=15,bg="blue",fg="white")
        btnaddData.grid(row=0,column=1)
        
        btnaddData=Button(frameButton,command=self.Update,text="Update",font=("arial",16,"bold"),width=15,bg="blue",fg="white")
        btnaddData.grid(row=0,column=2)
        
        btnaddData=Button(frameButton,command=self.delete,text="Delete",font=("arial",16,"bold"),width=15,bg="blue",fg="white")
        btnaddData.grid(row=0,column=3)
        
        btnaddData=Button(frameButton,command=self.Reset,text="Reset",font=("arial",16,"bold"),width=15,bg="blue",fg="white")
        btnaddData.grid(row=0,column=4)
        
        btnaddData=Button(frameButton,command=self.iExit,text="Exit",font=("arial",16,"bold"),width=15,bg="blue",fg="white")
        btnaddData.grid(row=0,column=5)
         # ==================================Information frame ==============================================
        
        framedetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framedetails.place(x=0,y=545,width=1366,height=195)
        
        table_frame=Frame(framedetails,bd=6,relief=RIDGE,bg="powder blue")
        table_frame.place(x=0,y=2,width=1290,height=170)
        
        xscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(table_frame,columns=("member","prnno","title","firstname","lastname","address1","address2","postid",
                                                             "mobile","bookid","booktitle","auther","dateborrowed","duedate","days",
                                                             "laterreturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        
        
        
        self.library_table.heading("member",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("duedate",text="Due Date")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("laterreturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("member",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("duedate",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("laterreturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sANKET@2112",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
        self.member_var.get(),
        self.prn_var.get(),
        self.id_var_var.get(),
        self.firstname_var.get(),
        self.lastname_var.get(),
        self.adddress1_var.get(),
        self.address2_var.get(),
        self.postcode_var.get(),
        self.mobile_var.get(),
        self.bookid_var.get(),
        self.booktitle_var.get(),
        self.auther_var.get(),
        self.dateborrowed_var.get(),
        self.duedate_var.get(),
        self.daysofbook_var.get(),
        self.lateratefine_var.get(),
        self.dateoverdue_var.get(),
        self.finalprice_var.get(),
        ))
        
        conn.commit()
        self.fetch_data
        conn.close()
        
        messagebox.showinfo("Sucess","Member has been inserted sucessfully")
        
    def Update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sANKET@2112",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,BookID=%s,BookTitle=%s,Auther=%s,Dateborrowed=%s,Duedate=%s,daysofbook=%s,laterreturnfine=%s,overduedate=%s,finalprice=%s where PRN_no=%s",(
                                                self.member_var.get(),
                                                self.id_var_var.get(),
                                                self.firstname_var.get(),
                                                self.lastname_var.get(),
                                                self.adddress1_var.get(),
                                                self.address2_var.get(),                                                                                                                                                                                                                                                     
                                                self.postcode_var.get(),
                                                self.mobile_var.get(),
                                                self.bookid_var.get(),
                                                self.booktitle_var.get(),
                                                self.auther_var.get(),
                                                self.dateborrowed_var.get(),
                                                self.duedate_var.get(),
                                                self.daysofbook_var.get(),
                                                self.lateratefine_var.get(),
                                                self.dateoverdue_var.get(),
                                                self.finalprice_var.get(),
                                                self.prn_var.get(),                 
                                                ))
        
        conn.commit()
        self.fetch_data()
        self.Reset()
        conn.close()
        
        messagebox.showinfo("sucess","Member has been Updated")
        
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sANKET@2112",database="hospital")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values'].split(',')
        
        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.adddress1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.auther_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.duedate_var.set(row[13])
        self.daysofbook_var.set(row[14])
        self.lateratefine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])
        
        
    def Show_data(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN NO\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID No\t\t"+self.id_var_var.get()+"\n")
        self.txtBox.insert(END,"FirstName\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"LastName\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1\t\t"+self.adddress1_var.get()+"\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Auther\t\t"+self.auther_var.get()+"\n")
        self.txtBox.insert(END,"Borrowed Date\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"Due Date\t\t"+self.duedate_var.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook\t\t"+self.daysofbook_var.get()+"\n")
        self.txtBox.insert(END,"LateRateFine\t\t"+self.lateratefine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"FinalPrice\t\t"+self.finalprice_var.get()+"\n")
        
        
        
    def Reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.adddress1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.duedate_var.set(""),
        self.daysofbook_var.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.id_var_var.set("")
        self.txtBox.delete("1.0",END)
        
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do You Want to Exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()==""or self.id_var_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="sANKET@2112",database="hospital")
            my_cursor=conn.cursor()
            query="delete from library where PRN_no=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fetch_data()
            self.Reset()
            conn.close()
            
            messagebox.showinfo("Sucess","Member has been Deleted")
            
        
             
    
if __name__== "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
    