import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:\\Users\\DELL\\Favorites\\Desktop\\ödev python\\Housing.csv", usecols=['price', 'stories'])
print(df.head())

x = df['stories']
y = df['price']

plt.hist(df['stories'], bins=10, alpha= 1)
plt.title('Evlerde Fiyat ve Kat Sayisi Arasindaki İliski')
plt.xlabel('Kat')
plt.xticks(ticks=[1, 2, 3, 4])
plt.ylabel('Fiyat')
plt.yticks(ticks=[])
plt.grid(axis='y')

plt.show()