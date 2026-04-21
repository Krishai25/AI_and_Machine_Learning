import csv
with open("input_file.csv" ,"r") as infile:
     reader=csv.DictReader(infile)
     for row in reader:
         print(row["Marks"])

with open("input_file.csv" ,"r") as infile:
    lines=infile.readlines()
    for line in lines[1:]:
        coloumns=line.strip().split(",")
        print(coloumns[0])