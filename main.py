from tkinter import *
from tkinter import messagebox
import os
class passs:
    def __init__(self,abc):
        self.abc=abc
        # self.abc=Tk()
        self.abc.title("Password Remeber")
        self.abc.geometry("500x630")
        #=======variables
        self.emailinp=StringVar()
        self.passinp=StringVar()
        self.aa=StringVar()
        self.bb=StringVar()
        self.pass_data=StringVar()
        frame1=LabelFrame(bd=7,relief=GROOVE,bg="gray60")
        frame1.place(x=0,y=0,height=90,relwidth=1)
        frame2=LabelFrame(text="Email",bd=4,relief=SUNKEN,bg="")
        frame2.place(x=00,y=100,relwidth=1,height=500)
        self.txtarea=Text(frame2,height=3)
        self.txtarea.pack(fill=X)
    def save_pass(self):
         self.a=self.emailinp.get()
         self.b=self.passinp.get()
         op=messagebox.askyesno("Conform","Do You want to Save this Id and Password")
         if op>0:
            self.pass_data=(f"Id={self.a}\nPassword={self.b}")
            f1=open("Passwords/"+str(self.a)+".txt","w")
            f1.write(self.pass_data)
            f1.close()
            messagebox.showinfo("Saved","Your Password is Saved")
         else:
             return
    def reset(self):
        self.emailinp.set("")
        self.passinp.set("")
        self.txtarea.delete("1.0")
    def bill_search(self):
        present="no"
        self.mama=(f"{self.emailinp.get()}.txt")
        # print(self.mama)
        for i in os.listdir("Passwords/"):
            if i==self.mama:
                f1=open(f"Passwords/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","No Data Found")

abc=Tk()
obj=passs(abc)
abc.mainloop()
