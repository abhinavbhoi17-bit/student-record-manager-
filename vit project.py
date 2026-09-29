#Student record manager
import csv
def student_record_info():
    "about the Student record manager"
    'res_no,name,dob,branch'
    print("This is Student Record Manager")
    print("It stores student records and perform suitable operations to maintain the record in spreadsheet")
def student_add_record():
    "to add record"
    f=open(r'd:\records.csv','a',newline='')
    a=int(input("Enter Res No: "))
    b=input("Enter Name: ")
    c=input("Enter DOB: ")
    d=input("Enter Branch: ")
    w=csv.writer(f)
    w.writerow([a,b,c,d])
    f.close()
    print("Student record added")
def student_update_record():
    "to update record"
    id=input("Enter Res No to update: ")
    a=[]
    b=0
    f=open(r'd:\records.csv','r',newline='')
    r=csv.reader(f)
    for i in r:
        if i[0]==id:
            i[1]=input("Enter New Name: ")
            i[2]=input("Enter New DOB: ")
            i[3]=input("Enter New Branch: ")
            b=1
        a.append(i)
    f.close()
    if b==1:
        f=open(r'd:\records.csv','w',newline='')
        w=csv.writer(f)
        w.writerows(a)
        f.close()
        print("Record updated!")
    else:
        print("Record not found.")
def student_delete_record():
    "to delete record"
    id=input("Enter Res No to delete: ")
    a=[]
    b=0
    f=open(r'd:\records.csv','r',newline='')
    r=csv.reader(f)
    for i in r:
        if i[0]==id:
            b=1
            continue
        a.append(i)
    f.close()
    if b==1:
        f=open(r'd:\records.csv','w',newline='')
        w=csv.writer(f)
        w.writerows(a)
        f.close()
        print("Record deleted!")
    else:
        print("Record not found.")
def student_display_record():
    "to display record"
    f=open(r'd:\records.csv','r',newline='')
    r=csv.reader(f)
    for i in r:
        print(i)
    f.close()
def student_search_record():
    "to search record"
    id=input("Enter Res No to search: ")
    f=open(r'd:\records.csv','r',newline='')
    r=csv.reader(f)
    for i in r:
        if i[0]==id:
            print("Record Found:",i)
            f.close()
            return
    print("Record not found.")
    f.close()
while True:
    n=0
    print("No.1 Student record information")
    print("No.2 To add student information to record")
    print("No.3 To update student information")
    print("No.4 To delete student information")
    print("No.5  display record")
    print("No.6 Search student record")
    print("No.7 To EXIT")
    n = int(input("Enter choice: "))
    if n==1:
        student_record_info()
    elif n==2:
        student_add_record()
    elif n==3:
        student_update_record()
    elif n==4:
        student_delete_record()
    elif n==5:
        student_display_record()
    elif n==6:
        student_search_record()
    elif n==7:
        break
    else:
        print("Enter again")
