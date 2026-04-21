with open("input_file.csv","r") as infile, open("output_file.csv","a") as outfile:
    for line in infile:
        # Method 1
        print(line.strip(),file=outfile)

        # Method2
        # print(line.strip())
        # outfile.write(line)
