#Pair programming by Ryuichiro and Abdullah

import json
import csv

#open JSON file and show it on STDOUT
with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)


#This is creating a csv file with the proper headers
with open('superheroes.csv', 'w') as f:
	writer =csv.writer(f)
	headers = ["name", "age", "secret identity", "powers", "squad name", "home town", "formed", "secret base", "active"]
	writer.writerow(headers)

#This loops through all the members and lists the attributes of each superhero in the csv file
	members = superheroes["members"]
	for member in members:
		name = member["name"]
		age = member["age"]
		identity = member["secretIdentity"]
		powers = member["powers"]
		squad = superheroes["squadName"]
		hometown = superheroes["homeTown"]
		formed = superheroes ["formed"]
		base = superheroes ["secretBase"]
		active = superheroes ["active"]
		writer.writerow([name, age, identity, powers, squad, hometown, formed, base, active])



#This is creating a csv file with the proper headers
with open('superheroes_by_power.csv', 'w') as f:
	writer =csv.writer(f)
	headers = ["name", "age", "secret identity", "powers", "squad name", "home town", "formed", "secret base", "active"]
	writer.writerow(headers)
	members = superheroes["members"]
	for member in members:
		for power in member["powers"]:
			name = member["name"]
			age = member["age"]
			identity = member["secretIdentity"]
			powers = power
			squad = superheroes["squadName"]
			hometown = superheroes["homeTown"]
			formed = superheroes ["formed"]
			base = superheroes ["secretBase"]
			active = superheroes ["active"]
			writer.writerow([name, age, identity, powers, squad, hometown, formed, base, active])