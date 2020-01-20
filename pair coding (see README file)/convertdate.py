# By Abdullah and Ryuichiro
from datetime import datetime

# Set a variable birthday 
birthday = "1-May-12"

# Parse the date using datetime.datetime.strptime.
parsed_date = datetime.strptime(birthday, "%d-%b-%y")

# Use strftime to output a date that looks like "5/1/2012".
date_str = parsed_date.strftime("%-m/%-d/%Y")
print(date_str)