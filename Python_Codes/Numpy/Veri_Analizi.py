import numpy as np

# liste = np.array([1,2,3,4,5,6,7,8,9]) # Numpy tarafından bir adet bir boyutlu liste (dizi) oluşturuldu.

# print(type(liste)) # Çıktısı numpy.ndarray

# multi_array = liste.reshape(3,3) # array dizisinden 3x3'lük bir matris oluşturuldu.

# print(multi_array)

# random = np.arange(1,10, 2) # 1'den 10'a kadar 2'şer 2'şer liste oluşturur. [1, 10)
# zero = np.zeros(10) # 10 adet 0'dan oluşan dizi.
# one = np.ones(10) # 10 adet 1'den oluşan dizi.
# esit = np.linspace(0, 100, 5) # 0'dan 100'e kadar olan sayıları 5 eşit parçaya böler. 0 25 50 75 100
# rastgele = np.random.randint(0, 10, 2) # [0, 10) arasında rastgele iki sayı üretir.
# rastgele2 = np.random.rand(5) # 0 ile 1 arasında rastgele 5 sayı üretir.
# rastgele2 = np.random.randn(5) # -1 ile 1 arasında rastgele 5 sayı üretir.
# ortalama = rastgele.mean() # dizinin ortalamasını  verir.
# buyuk = rastgele.argmax() # dizideki en büyük elemanın index numarasını verir.

# print(random)

# multi = np.array([[0,1,2], [3,4,5], [6,7,8]])
# print(multi[1,2]) # 1. indeksteki elemanın 2. indeksteki elemanını ekrana yazdırır. (5)
#                   # Diğer tüm özellikler normal pythondaki listelerle aynı.

# dizi = np.array([1,2,3,4,5,6,7,8,9])
# print(dizi + 10) # Dizinin her elemanı 10 ile toplanır. Aynı şekilde çıkarılabilir, çarpılabilir ve bölünebilir; sinüsü, cosinüsü, karekökü, logatirması alınabilir.

# print(dizi <= 90) # Dizideki her elemanın 90'dan küçük ya da eşit olup olmadığına bakar ve her elemanın bool türünde bir değer gönderir.

# dizi1 = np.array([[1,2,3], [4,5,6]])
# dizi2 = np.array([[7,8,9],[10,11,12]])

# print(np.vstack((dizi1, dizi2))) # 4x3lük yeni bir dizi oluşur.
# print(np.hstack((dizi1, dizi2))) # 2x6lık yeni bir dizi oluşur.

# liste = np.arange(1,10)
# liste = liste.reshape(3,3)

# print(liste[:,0]) # listenin her elemanının ilk indeksindeki değeri yazar.