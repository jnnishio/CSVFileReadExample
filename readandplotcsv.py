import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('aumicwasp.csv')
x=df['JD']
y=df['Flux']
plt.plot(x,y)