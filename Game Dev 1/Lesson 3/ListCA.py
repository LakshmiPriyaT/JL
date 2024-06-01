myList = [ [0,1,2,3], [3,2,1,0] ] 

#iteration
for i in range(0, len(myList)):
    for j in range(0, len(myList[0])):
        print(myList[i][j], end = " ")
    print("\n")

#appending
myList.append([3,6,7,9])
#iteration after append
for i in range(0, len(myList)):
    for j in range(0, len(myList[0])):
        print(myList[i][j], end = " ")
    print("\n")

#deleting
myList.remove(myList[2])
print(myList)

#counting the occurrence a particular num
count = 0

for i in myList:
    for j in i:
        if j == 3:
            count = count + 1
print("there are", count, "times 3's in the list")

#searching a particular num divisible by 1 and adding it

count = 0

for i in myList:
    for j in i:
        if j % 1 == 0 and j != 0:
            count += j
print("the sum is", count)

#reversing
myList.reverse()
print(myList)

#sorting
myList.sort()
print(myList)

#slicing
print(myList[1][0:2])
