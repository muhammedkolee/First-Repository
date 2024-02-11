import pandas as pd
import numpy as np
from numpy.random import randn

# ▓▓▓PANDAS SERIES▓▓▓

# pandas_series = pd.Series() # Series bir obje oluşturuldu. (Farklı türlerde olabilir.)
# print(pandas_series) # --> Series([], dtype: object)

# numbers = [10, 20, 30, 40]
# pandas_series = pd.Series(numbers) # int64 tipinde bir nesne oluşturuldu.
# print(pandas_series)

# letters = ["a", "b", "c"]
# pandas_series = pd.Series(letters) # object türünde bir obje tanımlandı.
# print(pandas_series)

# random = [1,2,3,"a","b","c"]
# pandas_series = pd.Series(random) # object türünde bir obje oluşturuldu.
# print(pandas_series)

# num = 5
# pandas_series = pd.Series(num) # int64 türünde bir obje oluşturuldu.
# print(pandas_series)

# pandas_series = pd.Series(5, [0,1,2,3]) # 0'dan 3'e (dahil) kadar (4 adet) 5 sayılı bir obje oluşturur. (int64)
# print(pandas_series)

# pandas_series = pd.Series([20, 30, 40, 50], ["a", "b", "c", "d"]) # Index numaları 0,1 yerine a, b gibi olur.
# print(pandas_series)

# dict = {'a': 1, 'b': 2, 'c': 3}
# pandas_series = pd.Series(dict) # Sözlüğü Pandas serisi olarak yazdırır. Key solda, Value sağda.
# print(pandas_series)

# random_nums = np.random.randint(10,100,3)
# pandas_series = pd.Series(random_nums, ['a', 'b', 'c'])
# print(pandas_series[0]) # Index numaraları değişse bile ilk eleman 0. indexte kabul edilir.
# print(pandas_series[:2]) # İlk iki elemanı yazdırır.
# print(pandas_series['a']) # a indexine sahip değeri döndürür.
# print(pandas_series[['a', 'c']]) # a ve c indexine sahip değeri döndürür.

# random_nums = np.random.randint(10,100,3)
# print(random_nums.ndim) # Listenin boyutunu döndürür. (1)
# print(random_nums.dtype) # Listenin tipini döndürür. (int32)
# print(random_nums.shape) # Listenin kaça kaç olduğunu döndürür. (3,)
# print(random_nums.sum()) # Listenin toplamını döndürür. (3,)
# print(random_nums.max()) # Listenin maksimum değerini döndürür. (3,)
# result = random_nums + random_nums  # Elemanları toplayarak yazar.
# print(pd.Series(result)) # Elemanları toplayarak yazar.

# opel2018 = pd.Series([20,30,40,50], ["astra", "corsa", "mokka", "insignia"])
# opel2019 = pd.Series([40,30,20,10], ["astra", "corsa", "Grandland", "insignia"])
# total = opel2018 + opel2019
# print(total) # Olmayan değerler için NaN değerinin döndürür. Olmayan değerler tek başına yazdırırlırsa hata verir.

# ▓▓▓PANDAS SERIES▓▓▓




# ▓▓▓PANDAS DATAFRAME▓▓▓
# İki adet serinin birleştirilmesidir. İndex numaraları satır numarası olarak gözükür ve ayrıca sütunlara isim verilebilir. (Excel)
# Excel ya da SQL gibi verileri kolayca aşmayı sağlar.

# df = pd.DataFrame() # Boş bir DataFrame
# df = pd.DataFrame([1,2,3,4]) # Sütun ismi 0 olan bir DataFrame
# df = pd.DataFrame([["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]]) # Sütun ismi 0 ve 1 olan bir DataFrame
# df = pd.DataFrame([["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]], columns= ["İsim", "Not"]) # Sütunlara İsim ve Not isimlerini verdik.
# df = pd.DataFrame([["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]], columns= ["İsim", "Not"], index = [1,2,3,4]) # Index numarasını 1'den başlattık.
# print(df)



# dict = {"Name": ["Ahmet", "Ali", "Yağmur", "Çınar"], "Grade": [50,60,70,80]}
# df = pd.DataFrame(dict) # Dizi yerine sözlük kullanılarak aynı seri oluşturuldu.
# print(df)



# dict_list = [
#                 {"Name": "Ahmet", "Grade":50},
#                 {"Name": "Ali", "Grade":60},
#                 {"Name": "Yağmur", "Grade":70},
#                 {"Name": "Çınar", "Grade":0}
#             ]

# df = pd.DataFrame(dict_list)
# print(df)



# nums1 = np.random.randint(0, 100, 5)
# nums2 = np.random.randint(0, 100, 5)

# ps1 = pd.Series(nums1)
# ps2 = pd.Series(nums2)

# data = dict(apples = ps1, oranges = ps2) # dict tipinde orange ve apple keylerini (sütun) serilere (satır) eşitledik.

# df = pd.DataFrame(data) # dict veri tipini DataFrame'e döndürdük.
# print(df)

# ▓▓▓PANDAS DATAFRAME▓▓▓





# ▓▓▓PANDAS İLE DOSYADAN VERİ OKUMA▓▓▓

# df = pd.read_csv("Pandas\sample.csv", encoding="utf-8") # Aynı dizinde bulunan sapmle.csv isimli dosyayı okuyoruz.
# print(df)

# df = pd.read_json("Pandas\sample.json", encoding="utf-8")
# print(df)

# ▓▓▓PANDAS İLE DOSYADAN VERİ OKUMA▓▓▓





# ▓▓▓DATAFRAMELER İLE ÇALIŞMA▓▓▓

# df = pd.DataFrame(randn(3,3), index = ["A", "B", "C"], columns = ["Column 1", "Column 2", "Column 3"])

# print(df["Column 1"]) # Sadece Column 1 yazdırılır.
# print(df[["Column 1", "Column 2"]]) # 2 kolonu da yazdırır.
# print(df.loc["A"]) # A indeksindeki değerleri gönderir.
# loc["row", "column"] => loc[:, "column"] (sadece kolonu seçmek için)
# print(df.loc[:, "Column 2"])
# print(df.loc[:,"Column 1":"Column 3"]) # Kolon 1'den 3'e kadar olanları yazdırır. (!!! 3 DAHİL)
# print(df.iloc[1]) # 1. indexteki değer gelir. (.loc[1] dersek hata alırız.)

# df["Column 4"] = pd.Series(randn(3), ["A", "B", "C"]) # 4. kolonu ekler.
# df["Column 5"] = df["Column 1"] + df["Column 3"]
# print(df.drop("Column 3", axis= 1)) # Orijinal dataframede silinmez, sadece silinmiş hali bir kerelik yazdırılır.
# df.drop("Column 3", axis= 1, inplace=True) # Orijinal listeden de silinir. (Default olarak false değeri vardır.)
# print(df)

# ▓▓▓DATAFRAMELER İLE ÇALIŞMA▓▓▓





# ▓▓▓DATAFRAME FİLTRELEME▓▓▓

# data = np.random.randint(10, 100, 75).reshape(15,5)
# df = pd.DataFrame(data, columns = ["Kolon1", "Kolon2", "Kolon3", "Kolon4", "Kolon5"])

# print(df.columns) # Kolon bilgilerini verir.
# print(df.head()) # İlk 5 satırı yazdırır.
# print(df.head(10)) # İlk 10 satır yazdırılır.
# print(df.tail()) # Son 5 satırı yazdırır.
# print(df["Kolon 1"].head()) # Sadece Kolon 1'in ilk 5 satırını yazdırır.
# print(df[5:15]["Kolon 1"].head()) # 5'ten itibaren sadece Kolon 1'deki verileri 5 kere yazar.
# print(df > 50) # 75 veriden hangisi 50'den büyükse onların bool değerini döndürür.
# print(df[df > 50]) # Verilerden 50'den büyük olanları yazar, küçük olanlara NaN yazar.
# print(df["Kolon 1"] > 50) # Sadece Kolon 1 için verilen koşulu sağlar.
# print(df[df["Kolon 1"] > 50][["Kolon 1", "Kolon 2"]]) # Kolon 1'deki verilerden 50'den büyük olanların indeks numarasına sahip olanları alır ve bu indeksteki Kolon 1 ve Kolon 2 verilerini getirir.
# print(df[(df["Kolon 1"] > 50) & (df["Kolon 2"] > 50)][["Kolon 1", "Kolon 2"]]) # Kolon 1 ve Kolon 2'deki verilerin 50'den büyük olanlarının indeksini alır ve Kolon 1 ve Kolon 2'deki verilerini yazar. (& = ve operatörü)
# print(df[(df["Kolon 1"] > 50) | (df["Kolon 2"] > 50)]) # | = ya da operatörü
# print(df.query("Kolon1 > 50 & Kolon1 % 2 == 0")) # Kolon1'de hem çift hem de 50'den büyük olan değerler yazdırıldı.

# ▓▓▓DATAFRAME FİLTRELEME▓▓▓





# ▓▓▓UYGULAMA▓▓▓

# df = pd.read_json("Pandas\imdb_data.json")
# print(df[(df["movie_year"] == 2014) | (df["movie_year"] == 2015)][["movie_name", "movie_year"]])

# ▓▓▓UYGULAMA▓▓▓





# ▓▓▓DATAFRAMEDE GROUPBY KULLANIMI▓▓▓

# personeller = {
#     'Çalışan': ['Ahmet Yılmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz','Ali Turan', 'Rıza Ertürk', 'Mustafa Can'],
#     'Departman': ['İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe','İnsan Kaynakları'],
#     'Yaş': [30,25,45,50,23,34,42],
#     'Semt': ['Kadıköy', 'Tuzla', 'Maltepe', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadıköy'],
#     'Maaş': [5000, 3000, 4000, 3500, 2750, 6500, 4500] 
# }

# df = pd.DataFrame(personeller)

# print(df["Maaş"].sum()) # Tüm maaşları toplar.
# print(df.groupby("Departman").groups) # Departmanı ayrı gruplara böler.
# print(df.groupby(["Departman", "Semt"]).groups) # Departman ve semte göre gruplandırma yaparak yazdırır.

# semtler = df.groupby("Semt") # Semtlere göre gruplandırır.
# for name, group in semtler:
#     print(name)
#     print(group)

# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

# print(df.groupby("Semt").get_group("Kadıköy")) # Kadıköyde çalışan kişileri yazdırır.
# print(df.groupby("Departman").get_group("Muhasebe")) # Muhasebede çalışan kişileri yazdırır.
# print(df.groupby("Departman")["Maaş"].mean()) # Departmana göre maaş ortalamasını yazdırır.
# print(df.groupby("Semt")["Yaş"].mean()) # Semte göre yaş ortalamalarını yazdırır.
# print(df.groupby("Semt")["Çalışan"].count()) # Smetlere göre çalışan kişi sayısını yazdırır.
# print(df.groupby("Departman")["Yaş"].max()) # Departmanlara göre en yüksek yaşı olanı yazdırır.
# print(df.groupby("Departman")["Yaş"].max()["Muhasebe"]) # Departmanlara göre en yüksek yaşı olanın yalnızca muhasebe olanları yazdırır.
# print(df.groupby("Departman")["Yaş"].agg(np.mean)) # Departmana göre yaş ortalaması numpy üzerinden hesaplandı.

# ▓▓▓DATAFRAMEDE GROUPBY KULLANIMI▓▓▓





# ▓▓▓BOZUK VEYA EKSİK VERİLER▓▓▓

# data = np.random.randint(10,100,15).reshape(5,3)
# df = pd.DataFrame(data, index= ['a', 'c', 'e', 'f', 'h'], columns = ['kolon1', 'kolon2', 'kolon3'])

# df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

# print(df.drop(['a', 'b'], axis = 0)) # axis=1 olduğunda kolon, 0 olduğunda satır silinir.
# print(df.isnull()) # Değeri NaN olan değerleri True olarak döndürür.
# print(df.notnull()) # Değeri NaN olmayan değerleri True olarak döndürür.
# print(df.isnull().sum()) # Null olan değerleri sayar.
# print(df["kolon1"].isnull().sum()) # Sadece kolon1'deki null değerlerini sayar.

# newKolon = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 10] #np.nan NaN değeri atar.
# df["kolon4"] = newKolon # Yeni kolon eklendi.

# print(df[df["kolon4"].isnull()]) #kolon4'te bulunan null değerlerinin olduğu satırı yazdırdı.
# print(df[df["kolon4"].notnull()]["kolon4"]) # kolon4'te null olmayan değerlerin sadece kolon4 için değerlerini döndürdü.
# print(df.dropna()) # Satırın herhangi bir kolonunda NaN değeri varsa o satırı silerek döndürür. (axis=1 yapılırsa kolona göre arama yapar.)
# print(df.dropna(how = "all")) # Bütün satır NaN ise siler değilse silmez.
# print(df.dropna(subset=["kolon1", "kolon2"])) # NaN aramasını yalnızca kolon1 ve kolon2'de yapar.
# print(df.dropna(thresh=2)) # Eğer satırda en az 2 tane normal değer varsa silmez.
# print(df.fillna(value= 'no input')) # NaN olan alanları no input ile doldurur.

# NaN olan değerleri çıkartıp kalan sayısal değerleri toplayıp döndüren fonksiyon.
# def ortalama(df):
#     toplam = df.sum().sum()
#     adet = df.size - df.isnull().sum().sum()
#     return toplam / adet

# ▓▓▓BOZUK VEYA EKSİK VERİLER▓▓▓





# ▓▓▓STRİNG FONKSİYONLAR▓▓▓

# data = pd.read_csv("Pandas\sample.csv")

# data.dropna(inplace=True) #data değişkeninde NaN değeri olan tüm satırlar silindi.

# data["DEALSIZE"] = data["DEALSIZE"].str.upper() # DEALSIZE kolonundaki tüm string değerler büyük harf yapıldı.
# data["index"] = data["DEALSIZE"].str.find("Medium") # DEALSIZE kolonunda her satırda kaç adet Medium yazıyorsa yeni bir kolon oluşturarak bunun sayısını yazar. 
# data = data.DEALSIZE.str.contains("Small") # DEALSIZE kolonunda Small geçen satırları True olarak döndürür.
# data = data[data.DEALSIZE.str.contains("Small")] # True olarak dönen değerlerin değerlerini yazar.
# data = data.DEALSIZE.str.replace("Medium", "Orta") # İçinde Medium geçen DEALSIZE kolonunu Orta olarak değiştirir.

# data[["FirstName", "LastName"]] = data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True) # Name kolonu içindeki ismi ve soyismi farklı kolonlarda yazdırmak için bu kodu kullanırız. 2'den fazla ismi olanlar için koşula göre hareket eder. (Bu csv dosyasında çalışmıyor.)

# print(data.head(10))

# ▓▓▓STRİNG FONKSİYONLAR▓▓▓





# ▓▓▓JOIN VE MERGE METHODLARI▓▓▓

# customers = {
#     'CustomerID': [1,2,3,4],
#     'FirstName': ['Ahmet', 'Ali', 'Hasan', 'Canan'],
#     'LastName': ['Yılmaz', 'Korkmaz', 'Çelik', 'Toprak']
# }

# orders = {
#     'OrderID': [10,11,12,13],
#     'CustomerID': [1,2,5,7],
#     'OrderDate': ['2010-07-04', '2010-10-07','2010-03-05','2010-08-12']
# }

# df_customers = pd.DataFrame(customers, columns = ["CustomerID", "FirstName", "LastName"])
# df_orders = pd.DataFrame(orders, columns = ["OrderID", "CustomerID", "OrderDate"])

# result = pd.merge(df_customers, df_orders, how="inner") # İnner birleştirme işlemi yapıldı. (İki tabloda ortak olanların birleştirilmesi.)
# result = pd.merge(df_customers, df_orders, how="left") # Left birleştirme işlemi yapıldı. (1. tablodakilerin tümü ve iki tabloda ortak olanlar birleştirildi.)
# result = pd.merge(df_customers, df_orders, how="right") # Right birleştirme işlemi yapıldı. (2. tablodakilerin tümü ve iki tabloda ortak olanlar birleştirildi.)
# result = pd.merge(df_customers, df_orders, how="outer") # Outer birleştirme işlemi yapıldı. (Bütün veriler birleştirildi.)

# result = pd.concat([dataframe1, dataframe2]) # datafram1 ve dataframe2 birleştirildi. (axis = 1 olursa kolonları yan yana yazar.)

# print(result)

# ▓▓▓JOIN VE MERGE METHODLARI▓▓▓





# ▓▓▓DATAFRAME METHODLARI▓▓▓

# data = {
#     "kolon1": [1,2,3,4,5],
#     "kolon2": [10,20,20,40,50],
#     "kolon3": ["abc","bcfa","dafba","stfafff","1ui"]
# }

# df = pd.DataFrame(data)

# def kareal(x):
#     return x*x

# print(df["kolon2"].unique()) # kolon2'deki değerleri yazar fakat tekrar eden değerleri yazmaz.
# print(df["kolon2"].nunique()) # Tekrarsız kaç eleman olduğunu yazdırır.
# print(df["kolon2"].value_counts()) # Hangi elemandan kaç tane olduğunun sayısını döndürür.
# print(df["kolon1"] * 2) # Elemanların 2 ile çarpılmış hallerini yazdırır.
# print(df["kolon1"].apply(kareal)) # kolon1 üzerindeki bütün değerler sırasıyla kareal fonksiyonuna gider.
# print(df["kolon3"].apply(len)) # Her elemanın kaç karakter olduğunu döndürür.
# print(len(df.columns)) # DataFramede kaç kolon olduğunun sayısını döndürür.
# print(df.index) # Kaçtan başlayıp kaça gider ve artış miktarını döndürür.
# print(len(df.index)) # Kaç satır olduğunu döndürür.
# print(df.info) # Detaylı bilgi verir.
# print(df.sort_values("kolon3")) # kolon3'e göre sıralama yapar.
# print(df.sort_values("kolon3", ascending=False)) # Çoktan aza doğru sıralama yapar.
# print(df.pivot_table(index="Ay", columns="Kategori", values="Gelir")) # Tekrarlayan bilgileri daha düzenli yazmak için Ay bilgisini satır, Kategori bilgisini kolon yapar. Değerleri ise gelir olarak yazar.

# ▓▓▓DATAFRAME METHODLARI▓▓▓





# ▓▓▓UYGULAMALAR▓▓▓

# data = pd.read_csv("Pandas\\nba.csv")

# print(data.head(10))
# print(data.count("columns"))
# result = data[(data["age"] <= 25) & (data["age"] >= 20)][["player_name", "team_abbreviation"]]
# result = data[data["player_name"] == "John Holland"]["team_abbreviation"]
# result = data.groupby("team_abbreviation").get_group("VAN")
# result = result[result["age"] <= 25][["player_name", "age"]]
# result = data["team_abbreviation"].value_counts()
# result = ""
# for i in data["player_name"]:
#     if "and" in i.lower():
#         result += i + "\n"

# print(result)

# ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

# df = pd.read_csv("Pandas\GBvideos.csv")

# result = df

# result = df.head(10)
# result = df[5:].head()
# result = df.columns
# result = df.count("columns")

# df.drop(["thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description"], axis=1,  inplace=True)

# result = df["dislikes"].mean()
# result = df["likes"].mean()
# result = df["likes"].head(50).mean()
# result = df["dislikes"].head(50).mean()
# result = df[["likes", "dislikes"]].head(50)
# result = df[df["views"].max() == df["views"]]
# result = df[df["views"].min() == df["views"]]
# result = df.sort_values("views",ascending=False).head(10)
# result = df.groupby("channel_title")["views"].mean()
# result = df.sort_values("comment_count", ascending=False)
# result = df.value_counts("category_id")
# df["length_title"] = df["title"].str.len()
# result = df["length_title"]

# print(result)