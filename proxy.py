import csv
CSVfile = open("Question2,3/reference.csv")

# Making rows - list of reference file
csvreader = csv.reader(CSVfile)
header = next(csvreader)
rows = []
for row in csvreader:
    row[3]='0'
    rows.append(row)

# Making list_of_attendance - list of attendance file
a_file = open("Question2,3/attendance.txt", "r")
list_of_attendance = []
list_size = 0
for line in a_file.readlines():
    line = line.strip()
    list_of_attendance.append(line)
    list_size = list_size + 1
a_file.close()

# Main Program
list_of_proxy_roll_no = []
#Finding the row which contains the name
for attendance in list_of_attendance:
    if 'AM' in attendance:
        attendance = attendance.replace(attendance[-8:],'')
        no_of_attendance = 0
        list_of_students_attendences = []
        #Counting no. of times the person gave attendance
        iterator_loop = 0
        for list_item in list_of_attendance:
            iterator_loop = iterator_loop + 1
            if attendance in list_item:
                iterator = 0
                iterator_nested_loop = iterator_loop
                #Counting no. of times the person gave attendance consecutively
                while iterator==0 and iterator_nested_loop<list_size:
                    if 'AM' not in list_of_attendance[iterator_nested_loop]:
                        list_of_students_attendences.append(list_of_attendance[iterator_nested_loop])
                        iterator_nested_loop = iterator_nested_loop +1
                        no_of_attendance = no_of_attendance + 1
                    else:
                        iterator = 1
        #Till now we have found the no_of_attendance (no of times a preson has given attendance) and list_of_students_attendences 
        #(list of the attendences the student has given)
        #Now if the no_of_attendences(different) of the student are greater than 1 then he has given proxy
        if no_of_attendance >1 and list_of_students_attendences.count(list_of_students_attendences[0])!=no_of_attendance:
            for x in list_of_students_attendences:
                if list_of_students_attendences.count(x)==list_of_attendance.count(x):
                    list_of_proxy_roll_no.append(x)
#Printing the roll no and name of the students who gave proxy
print('Details of the students who gave proxy:')
print('Roll No.','     ','Name')
for x in rows:
    for list_item in list_of_proxy_roll_no:
        if x[1] in list_item:
            print(x[1],'    ',x[2])
            break
CSVfile.close()