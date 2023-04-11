
vector = [1, 5, 3, 6, 9]
array = []
n = 8

vector.sort()

test1 = 0
test2 = 0

for number in range(len(vector)):
    if vector[number] > 0:
        test1 += vector[number]
    elif vector[number] < 0:
        test2 += vector[number]

if not(test1 >= n or test2 < n):
    print("No solution")
    exit(0)

vector.append(0)

y = []

for number in range(len(vector)):
    y.append(len(vector))

x = len(vector) - 1
calculatable = []

while x != 0:
    for number in y:
        if vector[number-1] not in calculatable:
            if vector[number-1] != 0:
                calculatable.append(vector[number-1])
    test1 = 0
    for number in calculatable:
        test1 += number
    if test1 == n:
        calculatable.sort()
        counter = 0
        for number in calculatable:
            if number == 0:
                counter += 1
        for number in range(counter):
            calculatable.remove(0)
        if calculatable not in array:
            array.append(calculatable)
            print(calculatable)
    calculatable = []
    y[-1] -= 1
    counter = 0
    for number in y:
        if number == 0:
            if y[x] == 0:
                x -= 1
            if counter != 0:
                y[counter-1] -= 1
                y[counter] = len(vector)
            else:
                print("x should be 0, x is " + str(x))
        counter += 1


