import csv
#opening reference file and creating list of header
CSVfile = open('Question2,3/reference.csv')
csvreader = csv.reader(CSVfile)
header = next(csvreader)
rows = []
#Creating a list of reference file
for row in csvreader:
    row[3]='0'
    rows.append(row)
print('Details of the student who were absent are:')
print('Roll No.','      ','Name')
#Central code
for x in rows:
    roll_no = x[1]
    input_file = open("Question2,3/attendance.txt", 'r')
    #Searching if the roll no exists in the attendance list or not
    iterator = 0
    for lines in input_file.readlines():
        if roll_no in lines:
            x[3]='1'
            iterator = 1
            break
    #If roll No doesn't appears in the list then he is absent and thus printing name and roll no
    if iterator == 0:
        print(x[1],'     ',x[2])
    input_file.close()
#Making the final-attendence file
with open('Question2,3/final-attendance.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(header)
    write.writerows(rows)
CSVfile.close()