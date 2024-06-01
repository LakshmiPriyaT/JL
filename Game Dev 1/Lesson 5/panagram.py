numberAsString = input("Enter the number - ")

numCount = {"1","2","3","4","5","6","7","8","9"}
numcount = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
}  
for num in numberAsString:
    if num in numCount:
        numcount[num] += 1
print(numcount)
panagram = True
for count in numcount.values():
    if count == 0:
        panagram = False

if panagram:
    print("Entered number is a Panagram")
else:
    print("Entered number is not a Panagram")