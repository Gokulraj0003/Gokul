
import tkinter
from tkinter import*
class contact_Book:
    def __init__(self):
        self.book=tkinter.Tk()
        self.book.geometry("500x500")
        self.book.title("contackbook")
        self.book.configure(background = "orange")
        self.first()
        self.book.mainloop()
    def first(self):

        Label_1=Label(self.book,text="CONTACT BOOK",font=("time new roman",30,"bold italic"),bg="orange",fg="red").place(x=70,y=50)
        Label_2=Label(self.book,text="First_name    :",font=("time new roman",20,"bold "),bg="orange",fg="green").place(x=50,y=150)
        Label_3=Label(self.book,text="Last_name     :",font=("time new roman",20,"bold "),bg="orange",fg="green").place(x=50,y=200)
        Label_4=Label(self.book,text="Age                :",font=("time new roman",20,"bold "),bg="orange",fg="green").place(x=50,y=250)
        Label_5=Label(self.book,text="Ph_no            :",font=("time new roman",20,"bold"),bg="orange",fg="green").place(x=50,y=300)
        self.e1 = StringVar()
        self.e2 = StringVar()
        self.e3 = StringVar()
        self.e4 = StringVar()
        entry1 = Entry(self.book,textvariable = self.e1,width="25").place(x=255,y=160)
        entry2 = Entry(self.book,show="",textvariable=self.e2,width="25").place(x=255,y=210)
        entry3 = Entry(self.book,show="",textvariable=self.e3,width="25").place(x=255,y=260)
        entry4 = Entry(self.book,show="",textvariable=self.e4,width="25").place(x=255,y=310)
        
        button1 = Button(self.book,text="Create",font=("time new roman",15,"bold"),command=self.insert,bg="#EC720C",width="10",bd="4").place(x=50,y=380)
        button2 = Button(self.book,text="Delete",font=("time new roman",15,"bold"),command=self.delete_contack,bg="#EC720C",width="10",bd="4").place(x=190,y=380)
        button3 = Button(self.book,text="Update",font=("time new roman",15,"bold"),command=self.update,bg="#EC720C",width="10",bd="4").place(x=330,y=380)
   
#insert
    def insert(self):
        import pymysql
        db_connection= pymysql.connect(
            host="localhost",
            user="root",
            password="gokulraj",
            database="contact_books"
        )
        my_database=db_connection.cursor()
        sql_statement= "INSERT INTO contacts(first_name,last_name,age,ph_no)values(%s,%s,%s,%s)"
        values= (self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get())
        my_database.execute(sql_statement,values)
        db_connection.commit()
        print("connected successfully")

#Update
    def update(self):
          import pymysql
          db_connection = pymysql.connect(
              host="localhost",
              user="root",
              password="gokulraj",
              database="contact_books"
          )
          my_database = db_connection.cursor()

          sql_statement = "UPDATE contacts SET ph_no=%s,last_name=%s,age=%s WHERE first_name=%s"
          values = (self.e4.get(), self.e2.get(),self.e3.get(),self.e1.get())  
          my_database.execute(sql_statement, values)
          db_connection.commit()
          print("Updated successfully")



#Delete
    def delete_contack(self):
        import pymysql

        db_connection = pymysql.connect(
            host="localhost",
            user="root",
            password="gokulraj",
            database="contact_books"
        )
        my_database = db_connection.cursor()
        
        sql_query = "DELETE FROM contacts WHERE first_name = %s"
        value = (self.e1.get(),)
        my_database.execute(sql_query, value)
        db_connection.commit()
        print("Row(s) deleted successfully!")

c=contact_Book()


