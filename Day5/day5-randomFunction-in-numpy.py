#Random function in Numpy 

import numpy as np


arr = np.random.rand(2,3)   # random rastgele sayı atar rand ise 0 ile 1 arasından bir sayı verir functionun icinde ise parametre default 1 olarak gelir eger sayı eklersem ekledigim sayıya göre matrix olusturur
print(arr)

arrRandint= np.random.randint(5) #randint ise tam sayı verir parametre bos kalırsa hata verir veya tek sayı verirsen ilk parametreyi 0 olarak tanımlar ornegin 5 verdim 0 ila 5 arasında rastgele bir tam sayı dondurur. 

arrRandintSize = np.random.randint(1,7, size=(2,3))  # burda da tek fark size verince sana verdigin size'a gore matrix verir

print(arrRandintSize)

#Seed np.random.seed() eger en uste veya calıstırmak istedigin yere bunu eklersen tum arrayleri sabit tutar icine verdigin sayıya gore degistirir ama her calısıtırfıgında aynı sonucu verir ornegin..

np.random.seed(42)

arrSeed = np.random.randint(4,8, size =(2,5)) # Üstte 'Seed' kullanıdıgım icin 4 ile 8 arasındaki rakamlarla olusturulan 2ye 5 lik bir matrix her calıstırıldıgında aynı sonucu verecektir 
print(arrSeed)