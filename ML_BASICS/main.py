# import pandas as pd
import numpy as np


# from sklearn import DecisionTreeRegressor

# file_path = "../melb_data.csv"

# melb_data = pd.read_csv(file_path)
# # print(melb_data.columns)

# # print(melb_data.head().isnull().sum())
# y = melb_data.head()
# # print(y)

# # print(f"{melb_data['Address'].iloc[0:10:4]}")

# melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# X = melb_data[melbourne_features]
# # print(X.describe())

# # Define model. Specify a number for random_state to ensure same results each run
# melbourne_model = DecisionTreeRegressor(random_state=1)
# melbourne_model.fit(X, y)

# print("Making predictions for the following 5 houses:")
# print(X.head())
# print("The predictions are")
# print(melbourne_model.predict(X.head()))

# data = {
#     "student_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 104],
#     "name": [" Amaka ", "Bola", "CHIDI", "Dami", "Efe", "Femi", "Grace", "Hassan", "Ife", "John", "Dami"],
#     "city": ["lagos", "Abuja ", "LAGOS", "Ibadan", "Abuja", "Lagos", "Ibadan", "Abuja", "Lagos", "Ibadan", "Ibadan"],
#     "study_hours": ["2", "3", "5", None, "1", "4", "6", "bad", "3.5", "7", None],
#     "attendance": [65, 70, 85, 60, 50, 80, 95, 75, 88, 98, 60],
#     "score": [48, 55, 76, 42, 35, 68, 88, 61, 73, 94, 42],
#     "joined": ["2026-01-05", "2026-01-08", "2026-02-02", "2026-02-10", "2026-02-14", "2026-03-01", "2026-03-03", "not recorded", "2026-03-15", "2026-03-20", "2026-02-10"]
# }

# scores = pd.Series({'Bola': 43, 'Amaka': 60, })
# print(scores)

# raw = pd.DataFrame(data)
# print(raw)

# # print(raw.to_csv('stud_raw.csv', index=False))
# loaded = pd.read_csv('stud_raw.csv')
# # print(loaded)

# df = raw.copy()

# df['study_hours'] = pd.to_numeric(df['study_hours'], errors='coerce')
# # print(df['study_hours'].isnull().sum())

# # print(df.duplicated().sum())
# df = df.drop_duplicates().reset_index(drop=True)

# # isna() checks for missing values
# # print(df.isna().sum())
# print(raw['name'].head(2))

py_list = [2, 4, 6]
numbers = np.array(py_list)

print(py_list * 2)
print(numbers * 2)
print(type(numbers))