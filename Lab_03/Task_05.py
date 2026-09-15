import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('OnlineRetail.csv', encoding='unicode_escape')


print(df)
print(df.describe())
print("First Column: \n"+str(df.iloc[:,1]) + "\nLast Column: \n"+str(df.iloc[:,-1]))
df.hist(figsize=(12,10))
plt.tight_layout()
plt.show()
