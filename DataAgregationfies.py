import pandas as pd
import csv
import json

def main():

    with open('fiesdataclean.csv', 'r') as arqcsv:
        reader = csv.reader(arqcsv, delimiter = ';')
        rows = list(reader)
    data = {}  
    enadeheader = rows[0]
    rows.pop(0)
    for row in rows:
        data[row[1]] = row
    with open('pda-prouni-2019.csv', 'r') as arqcsv:
        reader = csv.reader(arqcsv, delimiter = ';')
        prounidata = list(reader)

    agregatedcsv = [prounidata[0] + enadeheader]
    prounidata.pop(0)
    for student in prounidata:
        if student[1] in data:
            agregatedcsv.append(student + data[student[1]])
        else:
            agregatedcsv.append(student + ["", "", "", "", "", "", "", "", "", ""])
    with open("agregateddatafies.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(agregatedcsv)
if __name__ == "__main__":
    main()