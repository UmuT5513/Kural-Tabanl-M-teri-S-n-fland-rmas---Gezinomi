import pandas as pd
import numpy as np
#-------------------------Görev 1------------------------------
#---SORU 1---
pd.set_option('display.max_columns', None) #df nin tamamını "...." olmadan gösterir.
pd.set_option('display.width', 500) #tek bir satırda gösterir.
df = pd.read_excel("miuul_gezinomi.xlsx")
print(df.head())

#---SORU 2---
df["SaleCityName"].unique()
df["SaleCityName"].value_counts()

#---SORU 3---
df["ConceptName"].unique()

#---SORU 4---
df["ConceptName"].value_counts()

#---SORU 5---
df.groupby("SaleCityName")["Price"].sum()
df.groupby("SaleCityName").agg({"Price": "sum"})

#---SORU 6---
df.groupby("ConceptName")["Price"].sum()

#---SORU 7---
df.groupby("SaleCityName")["Price"].mean()

#---SORU 8---
df.groupby("ConceptName")["Price"].mean()

#---SORU 9---
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price" : "mean"})


#Görev 2: SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz.----------------------------
df["SaleCheckInDayDiff"].nunique()

bins = [0, 7, 30, 90, df["SaleCheckInDayDiff"].max()]

labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["cat_SaleCheckInDayDiff"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
print(df.head())


#Görev 3: Şehir-Concept-EB Score, Şehir-Concept- Sezon, Şehir-Concept-CInDay kırılımında ortalama ödenen ücret ve yapılan işlem sayısı cinsinden inceleyiniz.
df.groupby(["SaleCityName", "ConceptName", "cat_SaleCheckInDayDiff"]).agg({"Price" : ["mean", "count"]})


#Görev 4:  City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız.
agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price" : "mean"})


#Görev 5:  Indekste yer alan isimleri değişken ismine çeviriniz
level_based_df = agg_df.reset_index()
level_based_df.head()


#Görev 6:  Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
level_based_df["sales_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() for row in level_based_df.values]
level_based_df.head()


#Görev 7:  Yeni müşterileri (personaları) segmentlere ayırınız.
level_based_df["SEGMENT"] = pd.qcut(level_based_df["Price"], 4, labels=["D","C","B","A"])
level_based_df.head()


#Görev 8:  Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini  tahmin ediniz.
new_user = "ANTALYA_ODA + KAHVALTI_LOW"
level_based_df[level_based_df["sales_level_based"] == new_user]