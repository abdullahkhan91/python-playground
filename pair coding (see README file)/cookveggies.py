#By Ryuichiro and Abdullah

import csv
import json

#Read from the vegetables.csv file and create a dictionary called vegetables 
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    vegetables = [dict(veggie) for veggie in vegetables]

#Print the variable to check if the context above works
print(vegetables)

#Write the variable into a JSON file
with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent = 4)

