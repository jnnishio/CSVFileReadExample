import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('aumicwasp.csv')
x=df['JD']
y=df['Flux']
plt.plot(x,y,linestyle = "", marker = ".")
plt.xlim(1280,1300)
plt.xlabel("Julian Date (days)")
plt.ylabel("Flux (Normalized)")
plt.savefig('test.png')
