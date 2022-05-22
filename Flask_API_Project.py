import csv
import pandas as pd
from Data_Science_Project_Final import values

whole = []
with open("Final_Project.csv",'r') as f:
    reader = csv.reader(f)
    for row in reader:
        whole.append(row)
headers = whole[0]
data = whole[1:]

final_list = {}
for star_data in data:
    temp_dict = {
        "name" : data[1],
        "mass" : data[4],
        "radius" : data[5],
        "distance" : data[6],
        "gravity" : data[8]
    }

    temp_dict["sepcifications"] = star_data[1]
    final_list.append(temp_dict)

print(final_list)