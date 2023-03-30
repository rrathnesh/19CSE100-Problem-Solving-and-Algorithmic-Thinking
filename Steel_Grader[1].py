print("Number of steels need to be graded")
n = int(input())
i = 0
for i in range(0, n - 1 + 1, 1):
    print("What is the hardness of the steel " + str(i + 1))
    hardness = float(input())
    print("Enter the carbon content in the steel" + str(i + 1))
    carboncontent = float(input())
    print("What is the Tensile strength of the steel" + str(i + 1))
    tensilestrength = float(input())
    if hardness > 50 and carboncontent < 0.7 and tensilestrength > 5600:
        print("The grade is 10 for the respective steel sample")
    else:
        if hardness > 50 and carboncontent < 0.7:
            print("The grade is 9 for the respective steel sample")
        else:
            if carboncontent < 0.7 and tensilestrength > 5600:
                print("The grade is 8 for the respective steel sample")
            else:
                if hardness > 50 and tensilestrength > 5600:
                    print("The grade is 7 for the respective steel sample")
                else:
                    if hardness > 50 or carboncontent < 0.7 or tensilestrength > 5600:
                        print("The grade is 6 for the respective steel sample")
                    else:
                        print("The grade is 5 for the respective steel sample")
print("Thanks for using")
