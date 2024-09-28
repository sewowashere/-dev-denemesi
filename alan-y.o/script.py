import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:\\Users\\DELL\\Favorites\\Desktop\\ödev python\\Housing.csv", usecols=['price', 'bedrooms'])
print(df.head(100))

x = df['price']
y = df['bedrooms']

plt.hist(df['price'], bins=100, alpha= 1)
plt.title('Evlerde Fiyat ve Yatak Odasi Sayisi Arasindaki İlişki')
plt.xlabel('Fiyat')
plt.xticks(ticks=[])
plt.ylabel('Yatak Odasi Sayisi')
plt.yticks(ticks=[])
plt.grid(axis='y')

plt.show()