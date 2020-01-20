#By Ryuichiro and Abdullah, Day 5 classwork

import csv
import json

# Read vegetables.csv into a variable called vegetables.
with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	vegetables = list(reader)
	vegetables = [dict(veggie) for veggie in vegetables]


# Loop through vegetables and filter down to only green vegtables using a whitelist.
green_veggies = []
whitelist = ["okra", "arugula", "broccoli"]
for veggie in vegetables:
	if veggie["name"] in whitelist:
		green_veggies.append(veggie)

print(green_veggies)

# Write the veggies to a json file called greenveggies.json

with open("greenveggies.json", 'w') as f:
	json.dump(green_veggies, f, indent =4)


# Bonus: Output another csv called green_vegetables.csv.
with open('green_vegetables.csv', 'w') as f:
	writer =csv.writer(f)
	writer.writerow(['name', 'color'])
	for vegetable in green_veggies:
		writer.writerow([vegetable["name"], vegetable["color"]])





