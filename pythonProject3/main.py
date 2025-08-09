import kivy_garden.zbarcam
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import TransitionBase, SlideTransition
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.layout import Layout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy_garden import zbarcam
from kivy.config import Config
from kivy.clock import Clock
from kivy.properties import NumericProperty
from mysql.connector import MySQLConnection
import mysql
from tkinter import *
import random
import time
import datetime
from tkinter import Tk,StringVar,ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import numpy as np
from pyzbar.pyzbar import decode




class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class MenuWindow(Screen):
    pass

class Monday(Screen):
    pass

class Tuesday(Screen):
    pass

class Wednesday(Screen):
    pass

class Thursday(Screen):
    pass

class Friday(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class GridLayout(Layout):
    pass

class Snack1(Screen):
    pass

class Snack2(Screen):
    pass

class Snack3(Screen):
    pass

class Snack4(Screen):
    pass

class Snack5(Screen):
    pass

class Lunch1(Screen):
    pass

class Lunch2(Screen):
    pass

class Lunch3(Screen):
    pass

class Lunch4(Screen):
    pass

class Lunch5(Screen):
    pass

class Final(Screen):
    pass


kv=Builder.load_file("my.kv")


class MainApp(App):
    def build(self):
        return kv

    def qr(a):
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        myDat=''
        while myDat=='':
            success, img = cap.read()
            for barcode in decode(img):
                global myData

                myData = barcode.data.decode('utf-8')
                myDat='yes'

                #db = mysql.connector.connect(host='localhost', user='root', password='root', database='canteen')
                #cursor = db.cursor()
                #cursor.execute("insert into canteen.customers values('betty',3);")
                #db.commit()



                pts=np.array([barcode.polygon],np.int32)
                pts=pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,(255,0,255,15))
                pts2=barcode.rect
                cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)







            cv2.imshow('Result', img)
            cv2.waitKey(1)
            if myDat=='yes':
                cv2.destroyWindow('Result')


    def submit(self):
        root=Tk()
        root.geometry("1000x750+0+0")
        root.title("TODAY'S MENU")


        Tops=Frame(root,width=600,height=100,bd=12,relief='groove',highlightbackground='yellow')
        Tops.pack(side=TOP)
        lblTitle=Label(Tops,font=('Cambria',25,'bold'),text="TODAY'S MENU")
        lblTitle.grid(row=0,column=0)

        BottomMainFrame=Frame(root,width=600,height=100,bd=12,relief="groove")
        BottomMainFrame.pack(side=TOP)

        BottomMainFrame1 = Frame(root, width=600, height=100, bd=12, relief="groove",highlightbackground='yellow')
        BottomMainFrame1.pack(side=BOTTOM)



        f1 = Frame(BottomMainFrame, width=200, height=100, bd=12, relief="groove",)
        f1.pack(side=LEFT)



        f1TOP = Frame(f1, width=100, height=100, bd=12, relief="groove", )
        f1TOP.pack(side=TOP)
        f1BOTTOM = Frame(f1, width=100, height=100, bd=12, relief="groove", )
        f1BOTTOM.pack(side=BOTTOM)






        var1=IntVar()
        var2 = IntVar()


        var1.set(0)
        var2.set(0)


        varlunch=StringVar()
        varsnack=StringVar()
        varTotal=StringVar()

        varlunch.set("0")
        varsnack.set("0")
        varTotal.set("0")

        def chkLunch():
            if (var1.get()==1):
                txtlunch.configure(state=NORMAL)
                varlunch.set("")
            elif(var1.get()==0):
                txtlunch.configure(state=DISABLED)
                varlunch.set("0")


        def chkSnack():
            if (var2.get()==1):
                txtsnack.configure(state=NORMAL)
                varsnack.set("")
            elif(var1.get()==0):
                txtsnack.configure(state=DISABLED)
                varsnack.set("0")

        def cost():
            meal1=float(varlunch.get())
            meal2=float(varsnack.get())
            varTotal.set(meal1*40 + meal2*20)


        def exit():
            qexit=messagebox.askyesno("Canteen","Do you want to exit?")
            if qexit>0:
                root.destroy()
                return
        def reset():
            varlunch.set("0")
            varsnack.set('0')

        db = mysql.connector.connect(host='localhost',user='root',password='root',database='canteen')
        cursor = db.cursor()

        def order():
            total = float(varTotal.get())
            meal1 = int(varlunch.get())
            meal2 = int(varsnack.get())

            execute = ('INSERT INTO canteen.CUSTOMERS values(%s,%s,%s,%s)')
            data = (myData, meal1, meal2, total)
            cursor.execute(execute, data)

            db.commit()
            db.close()
            messagebox.showinfo("ORDER PLACED", "Your Order Has Been Placed!")



        lblMeal = Label(f1TOP, font=('Cambria', 20, 'bold'), text="LUNCH")
        lblMeal.grid(row=0, column=0)

        lunch=Checkbutton(f1TOP,text="Veg Biriyani, Raita & Appalam\t\t\t ₹40",variable=var1,onvalue=1,offvalue=0,
                          font=('Cambria',18,'bold'),command=chkLunch).grid(row=1,column=0,sticky=W)
        txtlunch=Entry(f1TOP,font=('Cambria',18,'bold'),textvariable=varlunch,width=6,justify='left',state=DISABLED)
        txtlunch.grid(row=1,column=1)

        lblSnack = Label(f1TOP, font=('Cambria', 20, 'bold'), text="SNACK")
        lblSnack.grid(row=2, column=0)

        snack=Checkbutton(f1TOP,text="Stuffed paratha\t\t\t\t₹20",variable=var2,onvalue=1,offvalue=0,
                          font=('Cambria',18,'bold'),command=chkSnack).grid(row=3,column=0,sticky=W)
        txtsnack=Entry(f1TOP,font=('Cambria',18,'bold'),textvariable=varsnack,width=6,justify='left',state=DISABLED)
        txtsnack.grid(row=3,column=1)

        lblTotal = Label(f1BOTTOM, font=('Cambria', 18, 'bold'), text="TOTAL")
        lblTotal.grid(row=4, column=0)

        txttotal = Entry(f1BOTTOM, font=('Cambria', 18, 'bold'), textvariable=varTotal, width=6, justify='left',
                         state=DISABLED)
        txttotal.grid(row=4, column=1)

        btnTotal=Button(f1BOTTOM,padx=16,pady=1,bd=4,fg='black',font=('Cambria',18,'bold'),
                    text=' CHECK TOTAL',command=cost).grid(row=5,column=0)

        btnExit = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text='EXIT', command=exit).grid(row=5, column=2)
        btnReset=Button(f1BOTTOM,padx=16,pady=1,bd=4,fg='black',font=('Cambria',18,'bold'),
                    text=' RESET',command=reset).grid(row=5,column=1)

        btnOrder = Button(BottomMainFrame1, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' PLACE ORDER', command=order).grid(row=0, column=0)
        root.mainloop()
    def submi(self):
        root = Tk()
        root.geometry("1000x750+0+0")
        root.title("TODAY'S MENU")

        Tops = Frame(root, width=600, height=100, bd=12, relief='groove', highlightbackground='yellow')
        Tops.pack(side=TOP)
        lblTitle = Label(Tops, font=('Cambria', 25, 'bold'), text="TODAY'S MENU")
        lblTitle.grid(row=0, column=0)

        BottomMainFrame = Frame(root, width=600, height=100, bd=12, relief="groove")
        BottomMainFrame.pack(side=TOP)

        BottomMainFrame1 = Frame(root, width=600, height=100, bd=12, relief="groove", highlightbackground='yellow')
        BottomMainFrame1.pack(side=BOTTOM)

        f1 = Frame(BottomMainFrame, width=200, height=100, bd=12, relief="groove", )
        f1.pack(side=LEFT)

        f1TOP = Frame(f1, width=100, height=100, bd=12, relief="groove", )
        f1TOP.pack(side=TOP)
        f1BOTTOM = Frame(f1, width=100, height=100, bd=12, relief="groove", )
        f1BOTTOM.pack(side=BOTTOM)

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var1.set(0)
        var2.set(0)
        var3.set(0)
        varlunch = StringVar()
        varsnack = StringVar()
        varTotal = StringVar()
        varsnack1 = StringVar()
        varlunch.set("0")
        varsnack.set("0")
        varTotal.set("0")
        varsnack1.set("0")

        def chkLunch():
            if (var1.get() == 1):
                txtlunch.configure(state=NORMAL)
                varlunch.set("")
            elif (var1.get() == 0):
                txtlunch.configure(state=DISABLED)
                varlunch.set("0")

        def chkSnack():
            if (var2.get() == 1):
                txtsnack.configure(state=NORMAL)
                varsnack.set("")
            elif(var2.get()== 0):
                txtsnack.configure(state=DISABLED)
                varsnack.set("0")
        def chkSnack1():
            if(var3.get()==1):
                txtsnack1.configure(state=NORMAL)
                varsnack1.set("")
            elif (var3.get()==0):
                txtsnack1.configure(state=DISABLED)
                varsnack1.set("0")


        def cost():
            meal1 = float(varlunch.get())
            meal2 = float(varsnack.get())
            meal3=float(varsnack1.get())
            varTotal.set(meal1*40+meal2*20+meal3*15)
        def exit():
            qexit = messagebox.askyesno("Canteen", "Do you want to exit?")
            if qexit > 0:
                root.destroy()
                return

        def reset():
            varlunch.set("0")
            varsnack.set('0')
            varsnack1.set('0')

        db = mysql.connector.connect(host='localhost', user='root', password='root', database='canteen')
        cursor = db.cursor()

        def order():
            total = float(varTotal.get())
            meal1 = int(varlunch.get())
            a=int(varsnack.get())
            b=int(varsnack1.get())
            meal2 = (a+b)


            execute = ('INSERT INTO canteen.CUSTOMERS values(%s,%s,%s,%s)')
            data = (myData, meal1, meal2, total)
            cursor.execute(execute, data)

            db.commit()
            db.close()
            messagebox.showinfo("ORDER PLACED", "Your Order Has Been Placed!")

        lblMeal = Label(f1TOP, font=('Cambria', 20, 'bold'), text="LUNCH")
        lblMeal.grid(row=0, column=0)

        lunch = Checkbutton(f1TOP, text="Rice, Sambar, Poriyal &Appalam\t\t\t₹40",variable=var1,onvalue=1,
                            offvalue=0,
                            font=('Cambria', 18, 'bold'), command=chkLunch).grid(row=1, column=0, sticky=W)
        txtlunch = Entry(f1TOP, font=('Cambria', 18, 'bold'), textvariable=varlunch, width=6,
                         justify='left', state=DISABLED)
        txtlunch.grid(row=1, column=1)

        lblSnack = Label(f1TOP, font=('Cambria', 20, 'bold'), text="SNACK")
        lblSnack.grid(row=2, column=0)

        snack = Checkbutton(f1TOP, text="Chicken Cutlet\t\t\t\t\t₹20", variable=var2, onvalue=1, offvalue=0,
                            font=('Cambria', 18, 'bold'), command=chkSnack).grid(row=3, column=0, sticky=W)
        txtsnack = Entry(f1TOP, font=('Cambria', 18, 'bold'), textvariable=varsnack, width=6,
                         justify='left', state=DISABLED)
        txtsnack.grid(row=3, column=1)

        snack1 = Checkbutton(f1TOP, text="Veg Cutlet\t\t\t\t\t\t₹15",variable=var3,onvalue=1,offvalue=0,
                             font=('Cambria', 18, 'bold'), command=chkSnack1).grid(row=4,column=0,sticky=W)
        txtsnack1= Entry(f1TOP, font=('Cambria', 18, 'bold'), textvariable=varsnack1,width=6,
                         justify='left', state=DISABLED)
        txtsnack1.grid(row=4,column=1)

        lblTotal = Label(f1BOTTOM, font=('Cambria', 18, 'bold'), text="TOTAL")
        lblTotal.grid(row=4, column=0)

        txttotal = Entry(f1BOTTOM, font=('Cambria', 18, 'bold'), textvariable=varTotal, width=6,
                         justify='left',
                         state=DISABLED)
        txttotal.grid(row=4, column=1)

        btnTotal = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' CHECK TOTAL', command=cost).grid(row=5, column=0)

        btnExit = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                         text='EXIT', command=exit).grid(row=5, column=2)
        btnReset = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' RESET', command=reset).grid(row=5, column=1)

        btnOrder = Button(BottomMainFrame1, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' PLACE ORDER', command=order).grid(row=0, column=0)

        root.mainloop()

    def subm(self):
        root = Tk()
        root.geometry("1000x750+0+0")
        root.title("TODAY'S MENU")

        Tops = Frame(root, width=600, height=100, bd=12, relief='groove', highlightbackground='yellow')
        Tops.pack(side=TOP)
        lblTitle = Label(Tops, font=('Cambria', 25, 'bold'), text="TODAY'S MENU")
        lblTitle.grid(row=0, column=0)

        BottomMainFrame = Frame(root, width=600, height=100, bd=12, relief="groove")
        BottomMainFrame.pack(side=TOP)

        BottomMainFrame1 = Frame(root, width=600, height=100, bd=12, relief="groove", highlightbackground='yellow')
        BottomMainFrame1.pack(side=BOTTOM)

        f1 = Frame(BottomMainFrame, width=200, height=100, bd=12, relief="groove", )
        f1.pack(side=LEFT)

        f1TOP = Frame(f1, width=100, height=100, bd=12, relief="groove", )
        f1TOP.pack(side=TOP)
        f1BOTTOM = Frame(f1, width=100, height=100, bd=12, relief="groove", )
        f1BOTTOM.pack(side=BOTTOM)

        var1 = IntVar()
        var2 = IntVar()

        var1.set(0)
        var2.set(0)

        varlunch = StringVar()
        varsnack = StringVar()
        varTotal = StringVar()

        varlunch.set("0")
        varsnack.set("0")
        varTotal.set("0")

        def chkLunch():
            if (var1.get() == 1):
                txtlunch.configure(state=NORMAL)
                varlunch.set("")
            elif (var1.get() == 0):
                txtlunch.configure(state=DISABLED)
                varlunch.set("0")

        def chkSnack():
            if (var2.get() == 1):
                txtsnack.configure(state=NORMAL)
                varsnack.set("")
            elif (var1.get() == 0):
                txtsnack.configure(state=DISABLED)
                varsnack.set("0")

        def cost():
            meal1 = float(varlunch.get())
            meal2 = float(varsnack.get())
            varTotal.set(meal1 * 50 + meal2 * 10)

        def exit():
            qexit = messagebox.askyesno("Canteen", "Do you want to exit?")
            if qexit > 0:
                root.destroy()
                return

        def reset():
            varlunch.set("0")
            varsnack.set('0')

        db = mysql.connector.connect(host='localhost', user='root', password='root', database='canteen')
        cursor = db.cursor()

        def order():
            total = float(varTotal.get())
            meal1 = int(varlunch.get())
            meal2 = int(varsnack.get())

            execute = ('INSERT INTO canteen.CUSTOMERS values(%s,%s,%s,%s)')
            data = (myData, meal1, meal2, total)
            cursor.execute(execute, data)

            db.commit()
            db.close()
            messagebox.showinfo("ORDER PLACED", "Your Order Has Been Placed!")


        lblMeal = Label(f1TOP, font=('Cambria', 20, 'bold'), text="LUNCH")
        lblMeal.grid(row=0, column=0)

        lunch = Checkbutton(f1TOP, text="Paratha(2nos) & Chicken Curry\t\t\t₹50",variable=var1,onvalue=1,offvalue=0,
                            font=('Cambria', 18, 'bold'), command=chkLunch).grid(row=1, column=0, sticky=W)
        txtlunch = Entry(f1TOP, font=('Cambria', 18, 'bold'), textvariable=varlunch, width=6, justify='left',
                         state=DISABLED)
        txtlunch.grid(row=1, column=1)

        lblSnack = Label(f1TOP, font=('Cambria', 20, 'bold'), text="SNACK")
        lblSnack.grid(row=2, column=0)

        snack = Checkbutton(f1TOP, text="Sandwich\t\t\t\t\t\t₹15",variable=var2,onvalue=1,offvalue=0,
                            font=('Cambria', 18, 'bold'), command=chkSnack).grid(row=3, column=0, sticky=W)
        txtsnack = Entry(f1TOP, font=('Cambria', 18, 'bold'), textvariable=varsnack, width=6, justify='left',
                         state=DISABLED)
        txtsnack.grid(row=3, column=1)

        lblTotal = Label(f1BOTTOM, font=('Cambria', 18, 'bold'), text="TOTAL")
        lblTotal.grid(row=4, column=0)

        txttotal = Entry(f1BOTTOM, font=('Cambria', 18, 'bold'), textvariable=varTotal, width=6, justify='left',
                         state=DISABLED)
        txttotal.grid(row=4, column=1)

        btnTotal = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' CHECK TOTAL', command=cost).grid(row=5, column=0)

        btnExit = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                         text='EXIT', command=exit).grid(row=5, column=2)
        btnReset = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' RESET', command=reset).grid(row=5, column=1)

        btnOrder = Button(BottomMainFrame1, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' PLACE ORDER', command=order).grid(row=0, column=0)
        root.mainloop()

    def sub(self):
        root = Tk()
        root.geometry("1000x750+0+0")
        root.title("TODAY'S MENU")

        Tops = Frame(root, width=600, height=100, bd=12, relief='groove', highlightbackground='yellow')
        Tops.pack(side=TOP)
        lblTitle = Label(Tops, font=('Cambria', 25, 'bold'), text="TODAY'S MENU")
        lblTitle.grid(row=0, column=0)

        BottomMainFrame = Frame(root, width=600, height=100, bd=12, relief="groove")
        BottomMainFrame.pack(side=TOP)

        BottomMainFrame1 = Frame(root, width=600, height=100, bd=12, relief="groove", highlightbackground='yellow')
        BottomMainFrame1.pack(side=BOTTOM)

        f1 = Frame(BottomMainFrame, width=200, height=100, bd=12, relief="groove", )
        f1.pack(side=LEFT)

        f1TOP = Frame(f1, width=100, height=100, bd=12, relief="groove", )
        f1TOP.pack(side=TOP)
        f1BOTTOM = Frame(f1, width=100, height=100, bd=12, relief="groove", )
        f1BOTTOM.pack(side=BOTTOM)

        var1 = IntVar()
        var2 = IntVar()

        var1.set(0)
        var2.set(0)

        varlunch = StringVar()
        varsnack = StringVar()
        varTotal = StringVar()

        varlunch.set("0")
        varsnack.set("0")
        varTotal.set("0")

        def chkLunch():
            if (var1.get() == 1):
                txtlunch.configure(state=NORMAL)
                varlunch.set("")
            elif (var1.get() == 0):
                txtlunch.configure(state=DISABLED)
                varlunch.set("0")

        def chkSnack():
            if (var2.get() == 1):
                txtsnack.configure(state=NORMAL)
                varsnack.set("")
            elif (var1.get() == 0):
                txtsnack.configure(state=DISABLED)
                varsnack.set("0")

        def cost():
            meal1 = float(varlunch.get())
            meal2 = float(varsnack.get())
            varTotal.set(meal1 * 70 + meal2 * 10)

        def exit():
            qexit = messagebox.askyesno("Canteen", "Do you want to exit?")
            if qexit > 0:
                root.destroy()
                return

        def reset():
            varlunch.set("0")
            varsnack.set('0')

        db = mysql.connector.connect(host='localhost', user='root', password='root')
        cursor = db.cursor(buffered=True)

        def order():
            total = float(varTotal.get())
            meal1=int(varlunch.get())
            meal2=int(varsnack.get())

            execute=('INSERT INTO canteen.CUSTOMERS values(%s,%s,%s,%s)')
            data=(myData,meal1,meal2,total)
            cursor.execute(execute,data)

            db.commit()
            db.close()
            messagebox.showinfo("ORDER PLACED", "Your Order Has Been Placed!")

        lblMeal = Label(f1TOP, font=('Cambria', 20, 'bold'), text="LUNCH")
        lblMeal.grid(row=0, column=0)

        lunch = Checkbutton(f1TOP, text="Chicken Biriyani & Raita\t\t\t ₹70", variable=var1, onvalue=1, offvalue=0,
                            font=('Cambria', 18, 'bold'), command=chkLunch).grid(row=1, column=0, sticky=W)
        txtlunch = Entry(f1TOP, font=('Cambria', 18, 'bold'), textvariable=varlunch, width=6, justify='left',
                         state=DISABLED)
        txtlunch.grid(row=1, column=1)

        lblSnack = Label(f1TOP, font=('Cambria', 20, 'bold'), text="SNACK")
        lblSnack.grid(row=2, column=0)

        snack = Checkbutton(f1TOP,text="Bajji \t\t\t\t\t₹10",variable=var2,onvalue=1,offvalue=0,
                            font=('Cambria', 18, 'bold'), command=chkSnack).grid(row=3, column=0, sticky=W)
        txtsnack = Entry(f1TOP, font=('Cambria', 18, 'bold'), textvariable=varsnack, width=6, justify='left',
                         state=DISABLED)
        txtsnack.grid(row=3, column=1)

        lblTotal = Label(f1BOTTOM, font=('Cambria', 18, 'bold'), text="TOTAL")
        lblTotal.grid(row=4, column=0)

        txttotal = Entry(f1BOTTOM, font=('Cambria', 18, 'bold'), textvariable=varTotal, width=6, justify='left',
                         state=DISABLED)
        txttotal.grid(row=4, column=1)

        btnTotal = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' CHECK TOTAL', command=cost).grid(row=5, column=0)

        btnExit = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                         text='EXIT', command=exit).grid(row=5, column=2)
        btnReset = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' RESET', command=reset).grid(row=5, column=1)

        btnOrder = Button(BottomMainFrame1, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' PLACE ORDER', command=order).grid(row=0, column=0)
        root.mainloop()

    def su(self):
        root = Tk()
        root.geometry("1000x750+0+0")
        root.title("TODAY'S MENU")

        Tops = Frame(root, width=600, height=100, bd=12, relief='groove', highlightbackground='yellow')
        Tops.pack(side=TOP)
        lblTitle = Label(Tops, font=('Cambria', 25, 'bold'), text="TODAY'S MENU")
        lblTitle.grid(row=0, column=0)

        BottomMainFrame = Frame(root, width=600, height=100, bd=12, relief="groove")
        BottomMainFrame.pack(side=TOP)

        BottomMainFrame1 = Frame(root, width=600, height=100, bd=12, relief="groove", highlightbackground='yellow')
        BottomMainFrame1.pack(side=BOTTOM)

        f1 = Frame(BottomMainFrame, width=200, height=100, bd=12, relief="groove", )
        f1.pack(side=LEFT)

        f1TOP = Frame(f1, width=100, height=100, bd=12, relief="groove", )
        f1TOP.pack(side=TOP)
        f1BOTTOM = Frame(f1, width=100, height=100, bd=12, relief="groove", )
        f1BOTTOM.pack(side=BOTTOM)

        var1 = IntVar()
        var2 = IntVar()

        var1.set(0)
        var2.set(0)

        varlunch = StringVar()
        varsnack = StringVar()
        varTotal = StringVar()

        varlunch.set("0")
        varsnack.set("0")
        varTotal.set("0")

        def chkLunch():
            if (var1.get() == 1):
                txtlunch.configure(state=NORMAL)
                varlunch.set("")
            elif (var1.get() == 0):
                txtlunch.configure(state=DISABLED)
                varlunch.set("0")

        def chkSnack():
            if (var2.get() == 1):
                txtsnack.configure(state=NORMAL)
                varsnack.set("")
            elif (var1.get() == 0):
                txtsnack.configure(state=DISABLED)
                varsnack.set("0")

        def cost():
            meal1 = float(varlunch.get())
            meal2 = float(varsnack.get())
            varTotal.set(meal1 * 50 + meal2 * 15)

        def exit():
            qexit = messagebox.askyesno("Canteen", "Do you want to exit?")
            if qexit > 0:
                root.destroy()
                return

        def reset():
            varlunch.set("0")
            varsnack.set('0')

        db = mysql.connector.connect(host='localhost', user='root', password='root', database='canteen')
        cursor = db.cursor()

        def order():
            total = float(varTotal.get())
            meal1 = int(varlunch.get())
            meal2 = int(varsnack.get())
            #myData = barcode.data.decode('utf-8')

            execute = ('INSERT INTO canteen.CUSTOMERS values(%s,%s,%s,%s)')
            data = (myData, meal1, meal2, total)
            cursor.execute(execute, data)

            db.commit()
            db.close()
            messagebox.showinfo("ORDER PLACED","Your Order Has Been Placed!")



        lblMeal = Label(f1TOP, font=('Cambria', 20, 'bold'), text="LUNCH")
        lblMeal.grid(row=0, column=0)

        lunch = Checkbutton(f1TOP, text="Fried Rice \t\t\t\t\t ₹50", variable=var1, onvalue=1, offvalue=0,
                            font=('Cambria', 18, 'bold'), command=chkLunch).grid(row=1, column=0, sticky=W)
        txtlunch = Entry(f1TOP, font=('Cambria', 18, 'bold'), textvariable=varlunch, width=6, justify='left',
                         state=DISABLED)
        txtlunch.grid(row=1, column=1)

        lblSnack = Label(f1TOP, font=('Cambria', 20, 'bold'), text="SNACK")
        lblSnack.grid(row=2, column=0)

        snack = Checkbutton(f1TOP, text="Chicken Momos\t\t\t\t\t₹15",variable=var2,onvalue=1,offvalue=0,
                            font=('Cambria', 18, 'bold'), command=chkSnack).grid(row=3, column=0, sticky=W)
        txtsnack = Entry(f1TOP, font=('Cambria', 18, 'bold'), textvariable=varsnack, width=6, justify='left',
                         state=DISABLED)
        txtsnack.grid(row=3, column=1)

        lblTotal = Label(f1BOTTOM, font=('Cambria', 18, 'bold'), text="TOTAL")
        lblTotal.grid(row=4, column=0)

        txttotal = Entry(f1BOTTOM, font=('Cambria', 18, 'bold'), textvariable=varTotal, width=6, justify='left',
                         state=DISABLED)
        txttotal.grid(row=4, column=1)

        btnTotal = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' CHECK TOTAL', command=cost).grid(row=5, column=0)

        btnExit = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                         text='EXIT', command=exit).grid(row=5, column=2)
        btnReset = Button(f1BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' RESET', command=reset).grid(row=5, column=1)

        btnOrder = Button(BottomMainFrame1, padx=16, pady=1, bd=4, fg='black', font=('Cambria', 18, 'bold'),
                          text=' PLACE ORDER', command=order).grid(row=0, column=0)
        root.mainloop()



if __name__=="__main__":
    MainApp().run()