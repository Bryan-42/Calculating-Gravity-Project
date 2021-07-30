import csv
import pandas as pd

rows = []

with open("final_Scaper.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

star_masses = []
star_radiuses = []
star_names = []

for star_data in star_data_rows:
    star_masses.append(star_data[3])
    star_radiuses.append(star_data[4])
    star_names.append(star_data[1])

star_gravity = []

for index, name in enumerate(star_names):
  gravity = (float(star_masses[index])*1.989e+30) / (float(star_radiuses[index])*float(star_radiuses[index])* 6.957e+8 * 6.957e+8)
  star_gravity.append(gravity)

headers.append("gravity")

with open ("final.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data_rows)