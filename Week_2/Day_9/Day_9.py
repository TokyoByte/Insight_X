import pandas as pd

file = "student_marks.csv"

data = pd.read_csv(file)

#data.head()
print(data.head())


print(data.groupby("DOB")["Maths"].mean())