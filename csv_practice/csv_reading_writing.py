import csv

with open("file.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Dallas", "Austin", "San Antonio"])
    writer.writerow(["Philly", "New Hope", "Harrisburg"])
