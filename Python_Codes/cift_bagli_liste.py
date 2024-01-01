﻿# -*- coding: utf-8 -*-                               
from asyncio.windows_events import NULL
from distutils.dist import command_re
from email.contentmanager import ContentManager
from tarfile import NUL
from textwrap import indent
from tkinter import *
from tkinter import messagebox

tk = Tk()

tk.title("Bağlı Liste")
tk.geometry("1000x500")
                                                     
class bosluk:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class BagliListe:
    def __init__(self):
        self.head = None
        self.tail = None

    def BosMu(self):
        return self.head is None

    def Boyut(self):
        sayac = 0
        bosluk = self.head
        
        while bosluk is not None:
            sayac += 1
            bosluk = bosluk.next
            
        return sayac

    def SonaEkle(self, data):
        if data == "":
            messagebox.showerror("HATA", "Değer giriniz!")            

        bosluk2 = bosluk(data)
        if self.BosMu():
            self.head = bosluk2
            self.tail = bosluk2
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
    
        else:
            self.tail.next = bosluk2
            bosluk2.prev = self.tail
            self.tail = bosluk2
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)

    def BasaEkle(self, data):
        if data == "":
            messagebox.showerror("HATA", "Değer giriniz!")
            
        bosluk2 = bosluk(data)
        if self.BosMu():
            self.head = bosluk2
            self.tail = bosluk2
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
    
        else:
            bosluk2.next = self.head
            self.head.prev = bosluk2
            self.head = bosluk2
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)

    def ArayaEkle(self, data, indeks):
        if data == "":
            messagebox.showerror("HATA", "Değer giriniz!")
            return
        
        if indeks == "":
            messagebox.showerror("HATA", "İndeks numarasi giriniz!")
            return   
        
        if int(indeks) >= liste.Boyut():
            messagebox.showerror("HATA", "Indeks numarasi gecersiz!")
            return

        if self.BosMu():
             self.head = bosluk(data)
             self.tail = bosluk(data)                                                      

        bosluk2 = bosluk(data)

        if indeks == 0:
             bosluk2.next = self.head
             bosluk2.prev = None
             self.head.prev = bosluk2
             self.head = bosluk2
             count = liste.Boyut()
             Label(text=count, font="Arial 11").place(width=11, x=610, y=260)

        elif indeks == self.Boyut():
             bosluk2.prev = self.tail
             bosluk2.next = None
             self.tail.next = bosluk2
             self.tail = bosluk2
             count = liste.Boyut()
             Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
            
        else:           
             bosluk3 = self.head
             for i in range(int(indeks) - 1):
                 bosluk3 = bosluk3.next                                                     

             bosluk2.next = bosluk3.next
             bosluk2.prev = bosluk3
             bosluk3.next.prev = bosluk2
             bosluk3.next = bosluk2
             count = liste.Boyut()
             Label(text=count, font="Arial 11").place(width=11, x=610, y=260)

    def AradanSil(self, indeks):
        if indeks == "":
            messagebox.showerror("HATA", "İndeks numarasi giriniz!")
            return
        
        if self.BosMu():
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
            return

        if indeks == 0:
            self.BasiSil()
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
            return
        
        if indeks == self.Boyut() - 1: 
           self.SonuSil()
           count = liste.Boyut()
           Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
           return
        
        if int(indeks) >= liste.Boyut():
            messagebox.showerror("HATA", "Indeks numarasi gecersiz!")
            return

        bosluk3 = self.head
        for i in range(int(indeks) - 1):
            bosluk3 = bosluk3.next                                                    

        temp = bosluk3.next
        bosluk3.next = temp.next
        temp.next.prev = bosluk3
        temp = None
        
    def BasiSil(self):
        if self.BosMu():
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
            return
        
        temp = self.head
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
    
        else:
            self.head.prev = None
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
            return temp.data                         

    def SonuSil(self):
        if self.BosMu():
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
            return
        
        temp = self.tail
        self.tail = self.tail.prev
        
        if self.tail is None:
            self.head = None
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
            
        else:
            self.tail.next = None
            count = liste.Boyut()
            Label(text=count, font="Arial 11").place(width=11, x=610, y=260)
            return temp.data

    def Yazdir(self):
         bosluk = self.head
    
         if self.BosMu():
             messagebox.showerror("Hata", "Liste boş!")
         else:            
             box = Listbox(tk, font="Verdana 12 bold")
             box.place(width=130, height=200, x=450, y=280)
             i = 1
             bosluk = self.head
             while bosluk is not None: 
                 box.insert(i, f"{i}. eleman: {bosluk.data}")
                 bosluk = bosluk.next
                 i += 1                  
                                            
liste = BagliListe()

entry1 = Entry(tk, width=15)
entry1.place(width=99, height=21, y=75, x=380)

entry2 = Entry(tk, width=15)
entry2.place(width=99, height=21, y=75, x=580)

giris1 = Label(text="    Veri Gir:", font="Verdana 8 bold").place(width=80, x=300, y=75)
giris2 = Label(text="İndeks Gir:", font="Verdana 8 bold").place(width=80, x=500, y=75)
sayi = Label(text="Listedeki Eleman Sayısı:", font="Verdana 8 bold").place(width=160, x=448, y=260)

buton1 = Button(tk,
                text="Başa Ekle", font="Verdana 12 bold",
                padx=10, pady=0,
                activebackground="green",
                activeforeground="white",
                foreground="white",
                bg="green",
                command=lambda: liste.BasaEkle(entry1.get())).place(width=100, height=60, x=150, y=110)

buton2 = Button(tk, text="Sona Ekle", font="Verdana 12 bold",
                padx=10, pady=0,
                activebackground="green",
                activeforeground="white",
                foreground="white",
                bg="green",
                command=lambda: liste.SonaEkle(entry1.get())).place(width=100, height=60, x=260, y=110)
   
buton3 = Button(tk, text="Araya Ekle", font="Verdana 12 bold",
                padx=10, pady=0,
                activebackground="green",
                activeforeground="white",
                foreground="white",
                bg="green",
                command=lambda: liste.ArayaEkle(entry1.get(), entry2.get())).place(width=100, height=60, x=370, y=110)

buton4 = Button(tk, text="Başı Sil", font="Verdana 12 bold",
                padx=10, pady=0,
                activebackground="red",
                activeforeground="white",
                foreground="white",
                bg="red",
                command=lambda: liste.BasiSil()).place(width=100, height=60, x=480, y=110)

buton5 = Button(tk, text="Sonu Sil", font="Verdana 12 bold",
                padx=10, pady=0,
                activebackground="red",
                activeforeground="white",
                foreground="white",
                bg="red",
                command=lambda: liste.SonuSil()).place(width=100, height=60, x=590, y=110)

buton6 = Button(tk, text="Aradan Sil", font="Verdana 12 bold",
                padx=10, pady=0,
                activebackground="red",
                activeforeground="white",
                foreground="white",
                bg="red",
                command=lambda: liste.AradanSil(entry2.get())).place(width=100, height=60, x=700, y=110)

buton7 = Button(tk, text="Listeyi Göster", font="Verdana 12 bold",
                padx=10, pady=0,
                activebackground="green",
                activeforeground="white",
                command=lambda: liste.Yazdir()).place(width=150, height=60, x=450, y=180)

lbl = Label(tk)
lbl.place(x=130, y=300)

tk.mainloop()