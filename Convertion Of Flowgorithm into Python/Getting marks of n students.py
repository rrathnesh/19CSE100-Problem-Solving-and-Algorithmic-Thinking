print("Enter the number of students")
n = int(input())
sub1 = [0] * (n)
sub2 = [0] * (n)
sub3 = [0] * (n)
sub4 = [0] * (n)
sub5 = [0] * (n)
roll = [0] * (n)
total = [0] * (n)
avg = [0] * (n)

for x in range(0, n - 1 + 1, 1):
    
    # Collecting data and information from the user
    print("Enter roll number of student " + str(x + 1))
    input = int(input())
    roll[x] = input
    print("Enter marks of student in Physics")
    input = int(input())
    sub1[x] = input
    print("Enter marks of student in Computer Science")
    input = int(input())
    sub2[x] = input
    print("Enter marks of student in Chemistry")
    input = int(input())
    sub3[x] = input
    print("Enter marks of student in Mathematics")
    input = int(input())
    sub4[x] = input
    print("Enter marks of student in english")
    input = int(input())
    sub5[x] = input
    total[x] = sub1[x] + sub2[x] + sub3[x] + sub4[x] + sub5[x]
    avg[x] = float(total[x]) / 5
for x in range(0, n - 1 + 1, 1):
    
    # Evaluating the given datas and information from the user
    print("Roll number of the student :" + str(roll[x]))
    print("Marks of the student :" + str(sub1[x]) + ", " + str(sub2[x]) + ", " + str(sub3[x]) + ", " + str(sub4[x]) + ", " + str(sub5[x]))
    print("total marks of the student :" + str(total[x]))
    print("Average marks of the student :" + str(avg[x]))
