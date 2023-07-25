# List Comprehensions
#GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.

import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns
["NUM_" + col.upper()if df[col].dtype !='O' else col.upper() for col in df.columns]

# GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
 # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']

[col.upper() + "_FLAG" if "NO" not in col else col.upper() for col in df.columns]

 # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################
#
og_list = ["abbrev", "no_previous"]
#
# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()

# Pandas Alıştırmalar

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
df=sns.load_dataset("titanic")
df.head()
df.shape

# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
df["sex"].value_counts()

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
df.nunique()

Görev 4: pclass değişkeninin unique değerleri bulunuz.
df['pclass'].unique()

# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df[['pclass','parch']].nunique()

# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
df['embarked'].dtype
df['embarked']=df['embarked'].astype('category')
df['embarked'].dtype

# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
df[df['embarked']=='C'].head()

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
df[df['embarked']!='S'].head()

df[df["embarked"] != "S"]["embarked"].unique()

df[~(df["embarked"] == "S")]["embarked"].unique()

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df[(df['age'] < 30) & (df['sex']=='female')].head()

# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
df[(df['fare'] > 500) | (df['age'] > 70)].head()

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()

# Görev 12: who değişkenini dataframe'den düşürün.
df.drop('who', axis=1, inplace=True)
df.head()