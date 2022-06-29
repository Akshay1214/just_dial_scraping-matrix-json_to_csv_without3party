# Importing Libraries
import csv 
import json

#  Load the json file
with open("test.json") as f:
    data = json.load(f)
    
# Looping through dictionary 
res = {i:[] for i in data.keys()}
for i in data.keys():
    for j in data[i].keys():
        res[i].append(data[i][j])

#  Writing to csv
with open("test_to_csv.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    key_list = list(res.keys())
    limit = len(res[key_list[0]])
    writer.writerow(res.keys())
    for i in range(limit):
        writer.writerow([res[x][i] for x in key_list])

'''
import csv 
import json

f = open('test.json')
data = json.load(f)
print(data)

with open("test_d.csv", "w") as outfile:
    writer = csv.writer(outfile)
    key_list = list(data.keys())
    limit = len(key_list)
    writer.writerow(data.keys())
    for i in range(limit):
        writer.writerow([data[x][i] for x in key_list])

with open("test_d.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(data.keys())
    writer.writerows(zip(*data.values()))

f = open('test.json')
data = json.load(f)
print(data)

with open("test_d.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(data.keys())
    writer.writerows(zip(*data.values()))
'''

'''
import csv 
import json 

with open("test.json") as f:
    data = json.load(f)
print(data)
stud_info = ["ID", "Name", "Marks", "Grades"]
new_data = data

for k, v in data.items():
    # print(k, v)
    print(f"For key {k}", data[k])
    for ky, val in data[k].items():
        print(f"For subkey {ky}", val)

# with open('title.csv', 'w') as f:  
#         writer = csv.DictWriter(f, fieldnames=stud_info)
#         writer.writeheader()
#         writer.writerows(data)   
#         print(data)

# col = 1
# for item in range(6):
#     writer.writerow(data)
#     print(col)
#     col += 1
'''
