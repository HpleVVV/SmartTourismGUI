import os
import csv
import functools
from itertools import chain
import operator
import numpy as np
import pandas as pd
from tkcalendar import *
from cgitb import text
from tkinter import *
from tkinter.ttk import *
from ttkwidgets.autocomplete import AutocompleteEntry
import tkcalendar
from tkcalendar import Calendar
import sqlite3
from tkinter import messagebox
from tkinter.messagebox import showinfo,showerror
from datetime import datetime
from PIL import Image
from PIL import ImageTk as itk
from statistics import mode
from collections import Counter
from collections import OrderedDict
from PIL import ImageTk, Image
import random
from tkinter import messagebox
from numpy.random import choice


os.chdir(r'C:\Users\Huy\Desktop\smarttourismgui')
cities = ['Danang', 'Hanoi', 'Hochiminh', 'Hue']
master = Tk()

class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("900x700")
        self.login()
        self.interest
        

    def login(self):
        for i in self.master.winfo_children():
            i.destroy()


        Label(master, text="Name").grid(row=0)
        Label(master, text="Age").grid(row=1)
        Label(master, text="Gender").grid(row=2)
        gender=StringVar()
        radiobutton_1 = Radiobutton(master, text='Male', variable=gender, value='male').grid(row=3, column=1)
        radiobutton_2 = Radiobutton(master, text='Female', variable=gender, value='female').grid(row=3, column=2)



        Label(master, text="Diem den").grid(row=4)

        diemden = AutocompleteEntry(completevalues=cities,)
        diemden.grid(row=4, column=2)

        age = IntVar()
        name = Entry(master)
        age = Entry(master)
        


        name.grid(row=0, column=1)
        age.grid(row=1, column=1)

        global userdb
        userdb = sqlite3.connect('user2.db')
        tablecreate = """ CREATE TABLE IF NOT EXISTS USERS2 (
           ID INTEGER PRIMARY KEY AUTOINCREMENT,
           Name TEXT NOT NULL,
           Age INT NOT NULL,
           Gender TEXT NOT NULL,
           Diemden TEXT NOT NULL,
           Interest TEXT NOT NULL,
           SavedPlan TEXT NOT NULL)"""
        userdb.execute(tablecreate)
        userdb.commit()
        

        def getdata():
            global Diemden
            global userinterest
            Name=name.get()
            Age=age.get()
            Gender=gender.get()
            Diemden=diemden.get()
            userinterest = "Placeholder For Interest"
            usersavedplan = "Placeholder For SavedPlan"
            userdb.execute('insert into USERS2(Name,Age,Gender,Diemden,Interest,SavedPlan) values (?,?,?,?,?,?)', (str(Name),str(Age),str(Gender),str(Diemden),str(userinterest),str(usersavedplan)))
            userdb.commit()

    

        Button(master, 
          text='Quit', 
          command=master.quit).grid(row=5, 
                                    column=0, 
                                    sticky=W, 
                                    pady=4)
        Button(master, 
          text='Next', command=lambda:[getdata(),self.interest()]).grid(row=5, 
                                         column=2, 
                                        sticky=W, 
                                        pady=4)
    def interest(self):
        for i in self.master.winfo_children():
            i.destroy()
        Label(master, text = "Diem den cua ban la: " + Diemden).grid(row=1,column=1)
        Label(master, text = "Nhung hoat dong ban thuong lam trong chuyen du lich, chon it nhat 3 hoat dong").grid(row=2,column=1)

        kientruc = StringVar()
        dongvat = StringVar()
        leonui = StringVar()
        muasam = StringVar()
        hoatdongthethao = StringVar()
        lehoi = StringVar()
        nghethuat = StringVar()
        canhquan = StringVar()
        maohiem = StringVar()
        giaitri = StringVar()
        nhahang = StringVar()
        spa = StringVar()

        chkbutton_1 = Checkbutton(master, text = "Kien truc, lich su", variable = kientruc, onvalue = 'vanhoa', offvalue = 0).grid(row=3, column=1)
        chkbutton_2 = Checkbutton(master, text = "Dong vat, thuc vat, he sinh thai", variable = dongvat, onvalue = 'thiennhien', offvalue = 0).grid(row=3, column=3)
        chkbutton_3 = Checkbutton(master, text = "Leo nui", variable = leonui, onvalue = 'phieuluu', offvalue = 0).grid(row=4, column=1)
        chkbutton_4 = Checkbutton(master, text = "Mua sam", variable = muasam, onvalue = 'thanhthi', offvalue = 0).grid(row=4, column=3)
        chkbutton_5 = Checkbutton(master, text = "Hoat dong the thao", variable = hoatdongthethao, onvalue = 'thethao', offvalue = 0).grid(row=5, column=1)
        chkbutton_6 = Checkbutton(master, text = "Le hoi van hoa", variable = lehoi, onvalue = 'vanhoa', offvalue = 0).grid(row=5, column=3)
        chkbutton_7 = Checkbutton(master, text = "Nghe thuat", variable = nghethuat, onvalue = 'vanhoa', offvalue = 0).grid(row=6, column=1)
        chkbutton_8 = Checkbutton(master, text = "Canh quan thien nhien", variable = canhquan, onvalue = 'thiennhien', offvalue = 0).grid(row=6, column=3)
        chkbutton_9 = Checkbutton(master, text = "Hoat dong mao hiem", variable = maohiem, onvalue = 'thethao', offvalue = 0).grid(row=7, column=1)
        chkbutton_10 = Checkbutton(master, text = "Trung tam giai tri", variable = giaitri, onvalue = 'thanhthi', offvalue = 0).grid(row=7, column=3)
        chkbutton_11 = Checkbutton(master, text = "Nha hang", variable = nhahang, onvalue = 'thanhthi', offvalue = 0).grid(row=8, column=1)
        chkbutton_12 = Checkbutton(master, text = "Spa, club, casino", variable = spa, onvalue = 'thanhthi', offvalue = 0).grid(row=8, column=3)

        global subprofile
        subprofile = ["vanhoa", "thiennhien", "phieuluu", "thethao", "thanhthi"]
        



        def getinterest():
            global interest
            interest = [kientruc.get(),
                        dongvat.get(),
                        leonui.get(),
                        muasam.get(),
                        hoatdongthethao.get(),
                        lehoi.get(),
                        nghethuat.get(),
                        canhquan.get(),
                        maohiem.get(),
                        giaitri.get(),
                        nhahang.get(),
                        spa.get(),] 
        
        
        
        Button(master, text = "Next", command= lambda:[getinterest(),self.display()]).grid(row=14, column = 2)
    
    def display(self):
        for i in self.master.winfo_children():
            i.destroy()
        
        Label(master, text= "Your subprofile:").grid(row=1,column=1)
        Label(master, text="\n".join(map(str, interest))).grid(row=2,column=1)
        Label(master, text="Your destination: " + Diemden).grid(row=7,column=1)
        
        
        interestk1 = list(set(interest).intersection(set(subprofile)))
    

        global userinterest
        userinterest = " ".join(interestk1)

    



        def updateInterestToTable():
            userdb = sqlite3.connect('user2.db')
            cursor = userdb.cursor()

            interestupdate = """UPDATE USERS2 SET Interest = ? WHERE ID = (SELECT MAX(ID) FROM USERS2)"""

            cursor.execute(interestupdate, (userinterest,))
            userdb.commit()
            userdb.close()





        cal = Calendar(master, selectmode = 'day', date_pattern='dd/mm/yyyy')
        cal.grid(row=10,column=5)

        def grad_date():
            date.config(text = "Your starting date is:" + cal.get_date())

        Button(master, text = "Get Starting Date", command = grad_date).grid(row=15,column=5)
        
        date = Label(master, text = "")
        date.grid(row=16,column=5)
        
        endcal = Calendar(master, selectmode = 'day', date_pattern='dd/mm/yyyy')
        endcal.grid(row=10,column=10)

        def grad_enddate():
            enddate.config(text = "Your ending date is:" + endcal.get_date())

        Button(master, text = "Get Ending Date", command = grad_enddate).grid(row=15,column=10)
        
        enddate = Label(master, text = "")
        enddate.grid(row=16,column=10)

        def travelday1():
            date_format = "%d/%m/%Y"
            d0 = datetime.strptime(endcal.get_date(), date_format)
            d1 = datetime.strptime(cal.get_date(), date_format)
            travelday.config(text= d0 - d1)
        Button(master, text= "Count", command=travelday1).grid(row=17,column=10)
        travelday = Label(master, text="")
        travelday.grid(row=18, column=10)

        def retrive_day():
            global day
            day = travelday.cget("text")
        Button(master, text="Next", command= lambda:[updateInterestToTable(),retrive_day(),self.popularitymodule()]).grid(row=20,column=10)



   
    def popularitymodule(self):
        for i in self.master.winfo_children():
            i.destroy()
        Label(master, text="Top popular destination in  " + Diemden).grid(row=1, column=3)
        global poidata


        poidata= pd.read_csv("POIdata.csv")

        global poi

        poi = poidata.loc[poidata["Diemden"]== Diemden]

        poipop = poi[['POIname', 'Popularity']]

        global popularpoi

        popularpoi = poipop.nlargest(n=4, columns=['Popularity'])
        

        popularpoi.insert(2, "Rank", [1,2,3,4],True)

        print(type(popularpoi))

        

        top1poi = popularpoi.loc[popularpoi["Rank"]== 1]
        top2poi = popularpoi.loc[popularpoi["Rank"]== 2]
        top3poi = popularpoi.loc[popularpoi["Rank"]== 3]
        top4poi = popularpoi.loc[popularpoi["Rank"]== 4]
        global poi1
        global poi2
        global poi3
        global poi4

    
        poi1 = top1poi.iloc[0]['POIname']
      
        poi2 = top2poi.iloc[0]['POIname']
        poi3 = top3poi.iloc[0]['POIname']
        poi4 = top4poi.iloc[0]['POIname']

        print(poi)
        



        






        Label(master, text="Top1:   " + poi1).grid(row=2, column=4)
        Label(master, text="Top2:   " + poi2).grid(row=3, column=4)
        Label(master, text="Top3:   " + poi3).grid(row=4, column=4)
        Label(master, text="Top4:   " + poi4).grid(row=5, column=4)

        global poimatch
        global inputmatchmodule


    
        def inputmatchmodule():
            poimatch1 = poi.loc[poi['Subprofile'] == "vanhoa", 'POIname']
            poimatch2 = poi.loc[poi['Subprofile'] == "thiennhien", 'POIname']
            poimatch3 = poi.loc[poi['Subprofile'] == "phieuluu", 'POIname']
            poimatch4 = poi.loc[poi['Subprofile'] == "thethao", 'POIname']
            poimatch5 = poi.loc[poi['Subprofile'] == "thanhthi", 'POIname']

            

            if "vanhoa" in userinterest: 
                poimatch1 = poimatch1
            else:
                poimatch1 = pd.Series(dtype=str)
           
            if "thiennhien" in userinterest: 
                poimatch2 = poimatch2
            else:
                poimatch2 = pd.Series(dtype=str)
            
            if "phieuluu" in userinterest: 
                poimatch3 = poimatch3
            else:
                poimatch3 = pd.Series(dtype=str)
            
            if "thethao" in userinterest: 
                poimatch4 = poimatch4
            else:
                poimatch4 = pd.Series(dtype=str)
            
            if "thanhthi" in userinterest: 
                poimatch5 = poimatch5
            else:
                poimatch5 = pd.Series(dtype=str)
            
            poimatch1list = poimatch1.tolist()
            poimatch2list = poimatch2.tolist()
            poimatch3list = poimatch3.tolist()
            poimatch4list = poimatch4.tolist()
            poimatch5list = poimatch5.tolist()
            
            poimatch = poimatch1list + poimatch2list + poimatch3list + poimatch4list + poimatch5list

            

            #hybrid module popular + match
            poipopular = popularpoi['POIname'].values.tolist()

            

            highrecommendedpoiset = set(poipopular).intersection(poimatch)
            
            highrecommendedpoi = list(highrecommendedpoiset)


            popularmatchpoi = poipopular 
            popularmatchpoi.extend(x for x in poimatch if x not in popularmatchpoi)


            mediumrecommendedpoiset = set(popularmatchpoi) ^ set(highrecommendedpoi)
            mediumrecommendedpoi = list(mediumrecommendedpoiset)
            poiname = poi.POIname.to_list()

            lowrecommendedpoiset = set(poiname) ^ set(popularmatchpoi)
            lowrecommendedpoi= list(lowrecommendedpoiset)

            return poimatch, highrecommendedpoi, popularmatchpoi, mediumrecommendedpoi, lowrecommendedpoi



            


        Button(master,text="Plan your trip", command= lambda:[self.planningmodule(), inputmatchmodule()]).grid(row=6, column=4)

        
                
           
    def planningmodule(self):
        for i in self.master.winfo_children():
            i.destroy()

        
        Label(master, text= "Your travel schedule:").grid(row=1, column=0)
        poimatch, highrecommendedpoi, popularmatchpoi, mediumrecommendedpoi, lowrecommendedpoi = inputmatchmodule()
        print('high',highrecommendedpoi)
        print('medium',mediumrecommendedpoi)
        print('low',lowrecommendedpoi)
        recommendedpoi = highrecommendedpoi + mediumrecommendedpoi + lowrecommendedpoi
        print('recom', recommendedpoi)

        totalday=[int(s) for s in day.split() if s.isdigit()]

        k = [str(integer) for integer in totalday]
        a_string = "".join(k)

        x = int(a_string)


        for i in range(1,x+1):
            c= 1+3*(i-1)
            r=int
            if c>8:
                r=15
                c=1+3*(i-4)

            else:
                r=5
            
            Label(master, text= "Day" + str(i) +" :                                                         ").grid(row= r, column= c)


            if i ==1:
                Label(master, text="Breakfast "+str(i)).grid(row=r+1,column= c)
                BlockM1 = StringVar()
                while True:
                    try:
                      M1=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                      continue
                    break
                    
                BlockM1.set(M1)
                Label(master, text= BlockM1.get()).grid(row=r+2,column= c)
                if M1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(M1)
                    except:
                       pass
                elif M1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(M1)
                       
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(M1)
                      
                    except:
                        pass
                BlockM2 = StringVar()
                while True:
                    try:
                       M2=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                       continue
                    break
                BlockM2.set(M2)
                Label(master, text= BlockM2.get()).grid(row=r+3,column= c)
                if M2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(M2)
                       
                    except:
                       pass
                elif M2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(M2)
                       
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(M2)
                       
                    except:
                        pass
                Label(master, text="Lunch "+str(i)).grid(row=r+4,column= c)
                BlockA1 = StringVar()
                while True:
                    try:
                       A1=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                       continue
                    break
                BlockA1.set(A1)
                Label(master, text= BlockA1.get()).grid(row=r+5,column= c)
                if A1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(A1)
                      
                    except:
                       pass
                elif A1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(A1)
                      
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(A1)
                       
                    except:
                        pass
                BlockA2 = StringVar()
                while True:
                    try:
                        A2=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockA2.set(A2)
                Label(master, text= BlockA2.get()).grid(row=r+6,column= c)
                if A2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(A2)
                       
                    except:
                       pass
                elif A2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(A2)
                       
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(A2)
                       
                    except:
                        pass
                Label(master, text="Dinner "+str(i)).grid(row=r+7,column= c)
                BlockN1 = StringVar()
                while True:
                    try:
                        N1= random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockN1.set(N1)
                Label(master, text= BlockN1.get()).grid(row=r+8,column= c)
                if N1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(N1)
                       
                    except:
                       pass
                elif N1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(N1)
                      
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(N1)
                       
                    except:
                        pass
                BlockN2 = StringVar()
                while True:
                    try:
                        N2= random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockN2.set(N2)
                Label(master, text= BlockN2.get()).grid(row=r+9,column= c)
                if N2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(N2)
                    except:
                       pass
                elif N2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(N2)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(N2)
                    except:
                        pass
                continue
            
            
                
            if i ==2:
                Label(master, text="Breakfast "+str(i)).grid(row=r+1,column= c)
                BlockM1 = StringVar()
                while True:
                    try:
                      M1=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                      continue
                    break
                    
                BlockM1.set(M1)
                Label(master, text= BlockM1.get()).grid(row=r+2,column= c)
                if M1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(M1)
                    except:
                       pass
                elif M1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(M1)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(M1)
                    except:
                        pass
                BlockM2 = StringVar()
                while True:
                    try:
                       M2=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                       continue
                    break
                BlockM2.set(M2)
                Label(master, text= BlockM2.get()).grid(row=r+3,column= c)
                if M2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(M2)
                    except:
                       pass
                elif M2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(M2)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(M2)
                    except:
                        pass
                Label(master, text="Lunch "+str(i)).grid(row=r+4,column= c)
                BlockA1 = StringVar()
                while True:
                    try:
                       A1=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                       continue
                    break
                BlockA1.set(A1)
                Label(master, text= BlockA1.get()).grid(row=r+5,column= c)
                if A1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(A1)
                    except:
                       pass
                elif A1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(A1)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(A1)
                    except:
                        pass
                BlockA2 = StringVar()
                while True:
                    try:
                        A2=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockA2.set(A2)
                Label(master, text= BlockA2.get()).grid(row=r+6,column= c)
                if A2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(A2)
                    except:
                       pass
                elif A2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(A2)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(A2)
                    except:
                        pass
                Label(master, text="Dinner "+str(i)).grid(row=r+7,column= c)
                BlockN1 = StringVar()
                while True:
                    try:
                        N1= random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockN1.set(N1)
                Label(master, text= BlockN1.get()).grid(row=r+8,column= c)
                if N1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(N1)
                    except:
                       pass
                elif N1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(N1)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(N1)
                    except:
                        pass
                BlockN2 = StringVar()
                while True:
                    try:
                        N2= random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockN2.set(N2)
                Label(master, text= BlockN2.get()).grid(row=r+9,column= c)
                if N2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(N2)
                    except:
                       pass
                elif N2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(N2)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(N2)
                    except:
                        pass
                continue
            if i ==3:
                Label(master, text="Breakfast "+str(i)).grid(row=r+1,column= c)
                BlockM1 = StringVar()
                while True:
                    try:
                      M1=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                      continue
                    break
                    
                BlockM1.set(M1)
                Label(master, text= BlockM1.get()).grid(row=r+2,column= c)
                if M1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(M1)
                    except:
                       pass
                elif M1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(M1)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(M1)
                    except:
                        pass
                BlockM2 = StringVar()
                while True:
                    try:
                       M2=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                       continue
                    break
                BlockM2.set(M2)
                Label(master, text= BlockM2.get()).grid(row=r+3,column= c)
                if M2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(M2)
                    except:
                       pass
                elif M2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(M2)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(M2)
                    except:
                        pass
                Label(master, text="Lunch "+str(i)).grid(row=r+4,column= c)
                BlockA1 = StringVar()
                while True:
                    try:
                       A1=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                       continue
                    break
                BlockA1.set(A1)
                Label(master, text= BlockA1.get()).grid(row=r+5,column= c)
                if A1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(A1)
                    except:
                       pass
                elif A1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(A1)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(A1)
                    except:
                        pass
                BlockA2 = StringVar()
                while True:
                    try:
                        A2=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockA2.set(A2)
                Label(master, text= BlockA2.get()).grid(row=r+6,column= c)
                if A2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(A2)
                    except:
                       pass
                elif A2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(A2)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(A2)
                    except:
                        pass
                Label(master, text="Dinner "+str(i)).grid(row=r+7,column= c)
                BlockN1 = StringVar()
                while True:
                    try:
                        N1= random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockN1.set(N1)
                Label(master, text= BlockN1.get()).grid(row=r+8,column= c)
                if N1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(N1)
                    except:
                       pass
                elif N1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(N1)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(N1)
                    except:
                        pass
                BlockN2 = StringVar()
                while True:
                    try:
                        N2= random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockN2.set(N2)
                Label(master, text= BlockN2.get()).grid(row=r+9,column= c)
                if N2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(N2)
                    except:
                       pass
                elif N2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(N2)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(N2)
                    except:
                        pass
                continue
            if i ==4:
                Label(master, text="Breakfast "+str(i)).grid(row=r+1,column= c)
                BlockM1 = StringVar()
                while True:
                    try:
                      M1=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                      continue
                    break
                    
                BlockM1.set(M1)
                Label(master, text= BlockM1.get()).grid(row=r+2,column= c)
                if M1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(M1)
                    except:
                       pass
                elif M1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(M1)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(M1)
                    except:
                        pass
                BlockM2 = StringVar()
                while True:
                    try:
                       M2=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                       continue
                    break
                BlockM2.set(M2)
                Label(master, text= BlockM2.get()).grid(row=r+3,column= c)
                if M2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(M2)
                    except:
                       pass
                elif M2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(M2)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(M2)
                    except:
                        pass
                Label(master, text="Lunch "+str(i)).grid(row=r+4,column= c)
                BlockA1 = StringVar()
                while True:
                    try:
                       A1=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                       continue
                    break
                BlockA1.set(A1)
                Label(master, text= BlockA1.get()).grid(row=r+5,column= c)
                if A1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(A1)
                    except:
                       pass
                elif A1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(A1)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(A1)
                    except:
                        pass
                BlockA2 = StringVar()
                while True:
                    try:
                        A2=random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockA2.set(A2)
                Label(master, text= BlockA2.get()).grid(row=r+6,column= c)
                if A2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(A2)
                    except:
                       pass
                elif A2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(A2)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(A2)
                    except:
                        pass
                Label(master, text="Dinner "+str(i)).grid(row=r+7,column= c)
                BlockN1 = StringVar()
                while True:
                    try:
                        N1= random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockN1.set(N1)
                Label(master, text= BlockN1.get()).grid(row=r+8,column= c)
                if N1 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(N1)
                    except:
                       pass
                elif N1 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(N1)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(N1)
                    except:
                        pass
                BlockN2 = StringVar()
                while True:
                    try:
                        N2= random.choice(random.choice(random.choices([highrecommendedpoi,mediumrecommendedpoi,lowrecommendedpoi],[70, 25, 5],k=1)))
                    except IndexError:
                        continue
                    break
                BlockN2.set(N2)
                Label(master, text= BlockN2.get()).grid(row=r+9,column= c)
                if N2 in highrecommendedpoi:
                    try:
                       highrecommendedpoi.remove(N2)
                    except:
                       pass
                elif N2 in mediumrecommendedpoi:
                    try:
                       mediumrecommendedpoi.remove(N2)
                    except:
                        pass
                else:
                    try:
                       lowrecommendedpoi.remove(N2)
                    except:
                        pass
                continue
           
           
           
            if i >=5:
                messagebox.showerror("Too long travel", "We dont have enough sources to make plan for more than 5 days trips.")
                break
            
                

                



        

    
app(master)
master.mainloop()