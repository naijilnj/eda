# ================================
# 1. Exploring File Types
# ================================
fo = open("fo.txt", "wb")
print("File Name:", fo.name)
print("Is Closed:", fo.closed)
print("Mode:", fo.mode)
fo.close()


# ================================
# 2. Write and Read Text File
# ================================
file = open("sample.txt", "w")
file.write("EDA is good\nAll are good")
file.close()

file = open("sample.txt", "r")
print("\nFile Content:\n", file.read())
file.close()


# ================================
# 3. Pickle (Binary Storage)
# ================================
import pickle

data_pickle = [1, 2, 3, 4]

with open("data.pkl", "wb") as file:
    pickle.dump(data_pickle, file)

with open("data.pkl", "rb") as file:
    print("\nPickle Data:", pickle.load(file))


# ================================
# 4. API Request
# ================================
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print("\nAPI Status Code:", response.status_code)

response2 = requests.get("http://api.open-notify.org/astros")
print("API JSON Response:", response2.json())


# ================================
# 5. JSON Read & Write
# ================================
import json

data_json = {
    "Name": "Naijil",
    "Age": 21,
    "City": "Mumbai"
}

with open("data.json", "w") as file:
    json.dump(data_json, file)

with open("data.json", "r") as file:
    print("\nJSON Data:", json.load(file))


# ================================
# 6. Pandas DataFrame & CSV
# ================================
import pandas as pd

data_pd = {
    "Name": ["A", "B", "C"],
    "Age": [10, 20, 30],
    "Job": ["Accountant", "CEO", "Marketing"],
    "Salary": [50000, 100000, 60000]
}

df = pd.DataFrame(data_pd)
df.to_csv("sample.csv", index=False)

df_read = pd.read_csv("sample.csv")
print("\nCSV Data:\n", df_read)


# ================================
# 7. CSV to Excel
# ================================
df.to_excel("sample.xlsx", sheet_name="Data", index=False)

df_excel = pd.read_excel("sample.xlsx")
print("\nExcel Data:\n", df_excel)


# ================================
# 8. Dictionary Example
# ================================
people = [
    {"id": 1, "name": "Gaurav"},
    {"id": 2, "name": "Nikola"},
    {"id": 3, "name": "Priyog"}
]

print("\nPeople Data:")
for person in people:
    print(person["id"], person["name"])