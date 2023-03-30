# Declaring the variables
array = [0] * (5)

for x in range(0, 4 + 1, 1):
    
    # Evaluating the given data or values
    print("Enter " + str(x + 1) + " value")
    input = int(input())
    array[x] = input
max = array[0]
for x in range(0, 4 + 1, 1):
    if array[x] > max:
        max = array[x]
print("The largest integer value in array is " + str(max))
