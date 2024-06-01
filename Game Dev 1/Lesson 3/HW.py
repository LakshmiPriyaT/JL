import random
n = int(input("Enter the dimensions of the matrix - "))
matrix = []
for i in range(n):
    temp = []
    for j in range(n):
        x = int(input("Enter your element - "))
        temp.append(x)
    matrix.append(temp)
print(matrix) 
count = 0
for i in range(n):
    count += matrix[i][i]
print("The trace of the elements in the matrix is",count)

#hW 2
list = []
for i in range(21):
    j = int(input("enter marks of the student: "))
    list.append(j)
list1=[]
list2=[]
list3=[]
for i in list:
    if i <=30:
        list1.append(i)
    elif 31 <= i <= 69:
        list2.append(i)
    elif i >=70:
        list3.append(i)
print("list with marks less than 30 is",list1)
print("list with marks between 31 and 69 is",list2)
print("list with marks greater than 70",list3)
