# By Abdullah and Ryuichiro
import csv
import json

# Read vegtables.csv into a variable called vegtables.
with open("vegetables.csv") as f:
	reader = csv.DictReader(f)
	vegetables = list(reader)
	vegetables = [dict(veggie) for veggie in vegetables]

# Group vegtables by color as a variable vegtables_by_color.
vegetables_by_color = {}
for veggie in vegetables:
	color = veggie["color"]
	if color in vegetables_by_color:
		vegetables_by_color[color].append(veggie)
	else:
		vegetables_by_color[color] = [veggie]

# Output vegtables_by_color into a json called vegtables_by_color.json.
with open("vegetables_by_color.json", "w") as f:
	json.dump(vegetables_by_color, f, indent = 2)