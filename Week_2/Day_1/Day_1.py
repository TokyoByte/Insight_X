import pandas as pd

file = "student_marks.csv"

data = pd.read_csv(file)

#data.head()
print(data.head())
print(data.describe())

data_1 = {
        "fruits" : ["Orange", "Apple", "Guava", "Banana", "Grapes"],
        "Fruit_ID" : [1,2,3,4,5]
}

df = pd.DataFrame(data_1)

print(df.head())