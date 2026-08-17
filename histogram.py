import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("studentsmarks.csv")
print(df.columns)
totals=[
    df["Math"].sum(),
    df["Physics"].sum(),
    df["Chemistry"].sum(),
    df["Computer Science"].sum()
]
subjects=[
    "Maths",
    "Physics",
    "Chemistry",
    "Computer Science"
    
    
]
plt.figure(figsize=(8,8))
plt.pie(
    totals,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("total marks by subject")
plt.show()