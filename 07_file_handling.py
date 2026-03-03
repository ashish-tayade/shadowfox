# 07_file_handling.py
import csv

with open("student_marks.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

for row in rows:
    total = int(row["Math"]) + int(row["Science"]) + int(row["English"])
    row["Total"] = total
    row["Average"] = total/3

with open("updated_marks.csv", "w", newline="") as file:
    fieldnames = rows[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("File updated successfully")