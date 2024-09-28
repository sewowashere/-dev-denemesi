import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\DELL\\Favorites\\Desktop\\ödev python\\Housing.csv", usecols=['price', 'area'])
print("correct")
print(df.head())

x = df['price']
y = df['area']

plt.hist(df['price'], bins=100, alpha=1) 
plt.title('Evlerde Fiyat ve Büyüklük Arasindaki İliski')
plt.xlabel('Fiyat')
plt.ylabel('Alan')
plt.grid(axis='y')

plt.show()




