
# -*- coding: utf-8 -*-                               #UTF8 (T�rk�e karakterler) format�ndaki harfleri kullanabilmek i�in yaz�lan komut.
import random                                         #Rastgele say�lar olu�turmak i�in random k�t�phanesine eri�im sa�lad�k.
                                                     
class bosluk:                                         #bosluk isminde bir s�n�f olu�turduk.       
    def __init__(self, data):                         #S�n�f�n de�i�kenlerini ve davran��lar�n� belirleyen �nemli bir fonksiyondur.
        self.data = data                              #Gelen de�eri d���me e�itlemek i�in gerekli i�lemleri yap�yoruz.
        self.next = None                              #D���mden sonraki d���m�n de�erine None (bo�) de�erini at�yoruz.
        self.prev = None                              #D���mden �nceki d���m� de�erine None (bo�) de�erini at�yoruz.
                                                     
class BagliListe:                                     #BagliListe ad�nda yeni bir s�n�f olu�turuyoruz.
    def __init__(self):                               #bosluk s�n�f�ndaki fonksiyona eri�mek i�in yeni bir fonksiyon yaz�yoruz.
        self.head = None                              #head d���n�n de�erine None (bo�) de�eri at�yoruz.
        self.tail = None                              #tail d���n�n de�erine None (bo�) de�eri at�yoruz.

    def BosMu(self):                                  #BosMu isminde bir fonksiyon olu�turuyoruz ve listenin bo� olup olmad���n� kontrol ediyoruz.
        return self.head is None                      #Listenin ilk eleman� bo� ise True de�erini d�nd�r�r.

    def Boyut(self):                                  #Boyut isminde fonksiyon olu�turuyoruz. Bu fonksiyon listenin b�t�n elemanlar�n� say�yor ve bize eleman say�s�n� d�nd�r�yor.
        sayac = 0                                     #Eleman say�s�n� saymas� icin sayac isimli de�i�ken tan�ml�yor ve bunu s�f�ra e�itliyoruz.
        bosluk = self.head                            #Listenin ilk eleman�n� bosluk isimli de�i�kene e�itliyoruz.
        while bosluk is not None:                     #Bo�luk None (bo�) de�erine e�it olana kadar d�ng�y� s�rd�r�yoruz.
            sayac += 1                                #D�ng� her d�nd���nde sayac de�i�kenini bir artt�r�yoruz.
            bosluk = bosluk.next                      #D�ng� her d�nd���nde bosluk de�i�kenini bir sonraki d���me ge�iriyoruz. Yani bir nevi d���mler aras�nda gezdiriyoruz.
        return sayac                                  #D�ng� bitti�inde sayac de�i�kenini geri d�nd�r�yoruz.

    def SonaEkle(self, data):                         #SonaEkle isminde yeni bir fonksiyon olu�turuyoruz. Listenin sonuna eleman eklememizi sa�l�yor.
        bosluk2 = bosluk(data)                        #Kullan�c�dan gelen de�eri bosluk2 de�i�kenine at�yoruz.
        if self.BosMu():                              #Listenin bo� olup olmad���n� kontrol ediyoruz. E�er bo� ise if komut blo�una giriyoruz.
            self.head = bosluk2                       #bosluk2 de�i�kenindeki de�eri head de�i�kenine at�yoruz.
            self.tail = bosluk2                       #bosluk2 de�i�kenindeki de�eri tail de�i�kenine at�yoruz.
        else:                                         #E�er liste bo� de�ilse else komut blo�una giriyoruz.
            self.tail.next = bosluk2                  #bosluk2 de�i�kenini tail (son d���m) de�i�keninden sonraki d���me at�yoruz.
            bosluk2.prev = self.tail                  #tail (son d���m) de�i�kenini gelen de�erin (bosluk2) bir �nceki d���m�ne at�yoruz.
            self.tail = bosluk2                       #bosluk2 de�i�kenini tail (son d���m) de�i�kenine at�yoruz.
                                                      #Gelen de�i�keni tailden sonraki d���me atad�k ve tail de�i�kenini son d���m olarak g�ncelledik.

    def BasaEkle(self, data):                         #BasaEkle isimli bir fonksiyon olu�turuyoruz. Listenin ba��na eleman eklememizi sa�l�yor.
        bosluk2 = bosluk(data)                        #Kullan�c�dan gelen de�eri bosluk2 de�i�kenine at�yoruz.
        if self.BosMu():                              #Listenin bo� olup olmad���n� kontrol ediyoruz. E�er bo� ise if komut blo�una giriyoruz.
            self.head = bosluk2                       #bosluk2 de�i�kenindeki de�eri head de�i�kenine at�yoruz.
            self.tail = bosluk2                       #bosluk2 de�i�kenindeki de�eri tail de�i�kenine at�yoruz.
        else:                                         #E�er liste bo� de�ilse else komut blo�una giriyoruz.
            bosluk2.next = self.head                  #head (ba�) de�i�kenini gelen elemandan sonraki d���me at�yoruz.
            self.head.prev = bosluk2                  #Gelen eleman� head (ba�) de�i�keninden �nceki de�er olarak at�yoruz.
            self.head = bosluk2                       #Gelen eleman� head (ba�) olarak g�ncelliyoruz.
                                                      #Gelen de�i�keni headden �nceki d���me atad�k ard�ndan head de�i�kenini ilk d���m olarak g�ncelledik.

    def ArayaEkle(self, data, indeks):                #ArayaEkle isimli yenibir fonksiyon olu�turuyoruz. Bu fonksiyon listenin herhangi bir indeksine eleman eklememizi sa�l�yor.
       if self.BosMu():                               #Listenin bo� olup olmad���n� kontrol ediyoruz. E�er bo� ise if komut blo�una giriyoruz.
            self.head = bosluk(data)                  #Kullan�c�dan gelen de�eri head de�i�kenine at�yoruz.
            self.tail = self.head                     #head de�i�kenini tail de�i�kenine at�yoruz.
                                                      #Liste bo� ise gelen eleman� hem head hem de tail d���m� yap�yoruz ��nk� listede yaln�zca bir eleman oluyor.

       bosluk2 = bosluk(data)                         #�leride kullanmak amac�yla gelen de�eri bosluk2 de�i�kenine at�yoruz.

       if indeks == 0:                                #E�er kullan�c� 0. indekse (en ba�a) eleman eklemek istediyse bu komut blo�una giriyoruz.
            bosluk2.next = self.head                  #head de�i�kenini gelen elemandan sonraki d���m olarak at�yoruz.
            self.head.prev = bosluk2                  #Gelen eleman� head de�i�keninden �nceki eleman olarak at�yoruz.
            self.head = bosluk2                       #Gelen eleman� head de�i�kenine at�yoruz.
                                                      #Girilen eleman� en ba�a ekleyerek head de�i�kenine g�ncelliyoruz.

       if indeks == self.Boyut():                     #E�er kull�n�c� listenin sonuna eleman eklemek isterse bu komut blo�una giriyoruz.
            bosluk2.prev = self.tail                  #tail de�i�kenini gelen elemandan bir �nceki olarak at�yoruz.
            self.tail.next = bosluk2                  #Gelen eleman� tail de�i�keninden sonraki olarak at�yoruz.
            self.tail = bosluk2                       #Gelen eleman� tail de�i�keni olarak at�yoruz.
                                                      #Gelen eleman� son d���me atad�k ve tail de�i�kenini g�ncelledik.

       bosluk3 = self.head                            #�leride kullanmak amac�yla gelen de�eri bosluk3 de�i�kenine at�yoruz.
       for i in range(indeks - 1):                    #for d�ng�s�n� kullan�c�n�n girdi�i say�n�n 1 eksi�i kadar d�nd�r�yoruz.
           bosluk3 = bosluk3.next                     #bosluk3 de�i�keninden sonraki d���m� bosluk3 de�i�kenine at�yoruz.
                                                      #bosluk3 de�i�kenini girilen indeks say�s�ndan bir �nceki d���me getiriyoruz.

       bosluk2.next = bosluk3.next                    #bosluk3 de�i�keninden sonraki de�i�keni bosluk2 de�i�keninden sonraki de�i�kene at�yoruz.
       bosluk2.prev = bosluk3                         #bosluk3 de�i�kenini bosluk2 de�i�keninden �nceki de�i�kene at�yoruz.
       bosluk3.next.prev = bosluk2                    #bosluk2 de�i�kenini bosluk3 de�i�keninden sonrakinden �nceki d���me at�yoruz.
       bosluk3.next = bosluk2                         #bosluk2 de�i�kenini bosluk3 de�i�keninden sonrakine at�yoruz.


    def AradanSil(self, indeks):                      #AradanSil isimli bir fonksiyon olu�turuyoruz.
        if self.BosMu():                              #Listenin bo� olup olmad���n� kontrol ediyoruz.
            return

        if indeks == 0:                               #Girilen indeks say�s� 0 ise bu komut blo�una giriyoruz.
            self.BasiSil()                            #En ba�taki eleman� sildirmek i�in BasiSil fonksiyonunu �a��r�yoruz.
            return

        if indeks == self.Boyut() - 1:                #Girilen indeks numaras� son eleman� i�aret ediyor ise bu komut blo�una giriyoruz.
           self.SonuSil()                             #Son eleman� sildirmek i�in SonuSil fonksiyonunu �a��r�yoruz.
           return

        bosluk3 = self.head                           #head de�i�kenini bosluk3 de�i�kenine at�yoruz.
        for i in range(indeks - 1):                   #Girilen indeks numaras�ndan bir �nceki say� kadar for d�ng�s�n� d�nd�r�yoruz.  
            bosluk3 = bosluk3.next                    #bosluk3 de�i�keninden sonraki d���m� bosluk3 de�i�kenine at�yoruz.
                                                      #bosluk3 de�i�kenini istenilen d���me getiriyoruz.

        temp = bosluk3.next                           #bosluk3 de�i�kenini temp de�i�kenine at�yoruz.
        bosluk3.next = temp.next                      #tempten sonraki de�i�keni bosluk3ten sonraki de�i�kene at�yoruz.
        temp.next.prev = bosluk3                      #bosluk3� tempin sonrakinden �nceki de�i�kene at�yoruz.
        temp = None                                   #temp de�i�kenini bo�lu�a at�yoruz.


    def BasiSil(self):                                #BasiSil isminde bir fonksiyon olu�turuyoruz. En ba�taki eleman� silmek i�in bu fonksiyonu �a��r�yoruz.
        if self.BosMu():                              #Listenin bo� olup olmad���n� kontrol ediyoruz.
            return      
        temp = self.head                              #head de�i�kenini temp de�i�kenine at�yoruz.
        self.head = self.head.next                    #head de�i�keninden sonraki d���m� head de�i�kenine at�yoruz.
        if self.head is None:                         #E�er head de�i�keni None (bo�) ise bu komut blo�una giriyoruz.
            self.tail = None                          #tail de�i�kenine None (bo�) de�erini at�yoruz.
        else:                                         #head de�i�keni None (bo�) de�ilse bu de�i�kene giriyoruz.
            self.head.prev = None                     #head de�i�keninden �nceki d���me None (bo�) de�erini at�yoruz.
        return temp.data                              #temp de�i�keninin de�erini d�nd�r�yoruz.
                                                      #En ba�taki eleman� silerek silinen de�eri geri d�nd�rd�k.

    def SonuSil(self):                                #SonuSil isminde bir fonksiyon olu�turduk. Bu fonksiyon son eleman� silmek i�in �a��r�l�yor.
        if self.BosMu():                              #Listenin bo� olup olmad���n� kontrol ediyoruz. Liste bo� ise bu komut blo�una giriyoruz.
            return
        temp = self.tail                              #tail de�i�kenini temp de�i�kenine at�yoruz.
        self.tail = self.tail.prev                    #tailden �nceki d���m� tail de�i�kenine at�yoruz.
        if self.tail is None:                         #E�er tail de�i�keni None (bo�) ise bu komut blo�una girilir.
            self.head = None                          #head de�i�kenini None (bo�) olarak g�nceller.
        else:                                         #E�er tail de�i�keni None (bo�) de�ilse bu komut blo�una girilir.
            self.tail.next = None                     #tailden sonraki d���m� None (bo�) olarak g�nceller.
        return temp.data                              #Silinen de�eri geri d�nd�r�r.

    def Yazdir(self):                                 #Yazdir isminde fonksiyon olu�turduk. Bu fonksiyon listenin elemanlar�n� yazd�rmam�z� sa�lar.
        bosluk = self.head                            #head de�i�kenini bosluk de�i�kenine at�yoruz.
        if self.BosMu():                              #E�er liste bo� ise bu komut blo�una gireriz.
            print("Liste bos.")                       #Ekrana Liste bo�. yazd�r�yoruz.
        else:                                         #E�er liste bo� de�ilse bu komut blo�una giriyoruz.
            bosluk = self.head                        #head de�i�kenini bosluk de�i�kenine at�yoruz.
            while bosluk.next is not None:            #bosluktan sonraki de�er None (bo�) olana kadar d�ng� d�n�yor.
                print(f"{bosluk.data} ---> ", end="") #Ekrana �nce de�eri ard�ndan ---> �ek�ini yazd�r�yoruz.
                bosluk = bosluk.next                  #bosluktan sonraki de�eri boslu�a atad�k.
            print(bosluk.data)                        #bosluk de�i�kenin de�erini ekrana yazd�rd�k. (D�ng� d���nda yazma sebebimiz son elemandan sonra ekrana ---> okunu yazd�rmamak.)

liste = BagliListe()                                  #liste isminde bir ba�l� liste olu�turduk.
print(f"Liste bos mu = {liste.BosMu()}")              #Liste bo� mu diye sorduk ve ekrana True ya da False yazd�rd�k.
print(f"Listedeki eleman sayisi={liste.Boyut()}")     #Listedeki eleman say�s�n� yazd�rd�k.
liste.BasaEkle(random.randint(0, 100))                #Listenin ba��na rastgele bir de�er atad�k.
liste.SonaEkle(random.randint(0, 100))                #Listenin sonuna rastgele bir de�er atad�k.
liste.ArayaEkle(random.randint(0, 100), 1)            #Listenin 1. indeksine rastgele bir de�er atad�k.
liste.BasaEkle(random.randint(0, 100))                #Listenin ba��na rastgele bir de�er atad�k.
liste.SonaEkle(random.randint(0, 100))                #Listenin sonuna rastgele bir de�er atad�k.
liste.ArayaEkle(random.randint(0, 100), 2)            #Listenin 2. indeksine rastgele bir de�er atad�k.
liste.Yazdir()                                        #Listeyi yazd�rd�k.
print(f"Liste bos mu = {liste.BosMu()}")              #Liste bo� mu sorgusunu d�nd�rd�k.
print(f"Listedeki eleman sayisi={liste.Boyut()}")     #Listenin eleman say�s�n� yazd�rd�k.
liste.BasiSil()                                       #Listenin ba��ndaki eleman� sildik.
liste.SonuSil()                                       #Listenin sonundaki eleman� sildik.
liste.AradanSil(1)                                    #Listenin 1. indeksteki eleman�n� sildik.
liste.Yazdir()                                        #Listeyi yazd�rd�k.
print(f"Listedeki eleman sayisi={liste.Boyut()}")     #Listedeki eleman say�s�n� yazd�rd�k.