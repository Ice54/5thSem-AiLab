import pandas as pd

data = {
    "Name": ["Raahim","Sumaira","Asjad"],
    "Age": [40,50,60],
    "Salary": [100,80,90]
}
df = pd.DataFrame(data)
df["Bonus"] = df["Salary"] * 0.1
print(df)

print(df.drop("Age",axis=1))


