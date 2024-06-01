# Count the occurrence of vowels in the string entered by the user
"""
# Approach - 1
inputStr = input("Enter the string - ")
vowels = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
    }
    
for c in inputStr:
    if c in vowels:
        vowels[c] += 1
        
print(vowels)
"""
# Approach - 2
inputStr = input("Enter the string - ")
vowelsList = ["a","e","i","o","u"]
vowels = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}

for c in inputStr:
    if c in vowelsList:
        if c in vowels:
            vowels[c] += 1
        else:
            vowels[c] = 1
            
print(vowels)

# Count the occurrence of each alphabhet in the string entered by the user

inputStr = input("Enter the string - ")
charCount = {}

for c in inputStr:
    if c.isalpha():
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1
            
print(charCount)



# Find if the number entered by the user is a Panagram or not ?

