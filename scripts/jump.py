import requests
import json
import csv
from datetime import datetime
import pytz

# Python 3.7

# Set some constants
est = pytz.timezone('US/Eastern')
timestamp = (datetime.now(est))
filename = '../output/jump-' + timestamp.strftime("%Y-%m-%d-%H%M") + '.csv'
company = 'jump'
url = 'https://gbfs.uber.com/v1/atls/free_bike_status.json'

# Call the url. The data will arrive as a string you can format into a dict.
response = requests.get(url)
decoded = (response.content.decode("utf-8"))
jumps = json.loads(decoded)

# Output this to a plain .csv spreadsheet.
# First, just once, write the header row.
# Use the keys from the first item in the dict, and add company and the timestamp.
# Make all that into a list and write it.
# FWIW, what this creates is a header row like this:
# ['bike_id','lat','lon','is_reserved','is_disabled','jump_vehicle_type',
# 'jump_ebike_battery_level','jump_vehicle_name','company','time_scraped']

header_row = list(jumps['data']['bikes'][0].keys())
header_row.append('company')
header_row.append('time_scraped')

csvfile = open(filename, 'a')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(header_row)

# Now make an empty list.
# It'll be a list of lists.
# Each row will be populated with data from one scooter.

jumps_list = []

if (jumps['data']['bikes']):
    for i in range(len(jumps['data']['bikes'])):
        new_row = list(jumps['data']['bikes'][i].values())
        new_row.append(company)
        new_row.append(timestamp)
        jumps_list.append(new_row)

# Now write that list of lists to .csv
csvwriter.writerows(jumps_list)