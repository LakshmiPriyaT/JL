books = {
    "english": 200,
    "maths": 380,
    "physics":432,
    "chemistry": 890,
    "computerscience":890
}

while True:
  print("Options:")
  print("1.Display the list of books with cost")
  print("2.Insert a new book with cost")
  print("3.Modify an existing books cost")
  print("4.Exit")
  choice = input("Enter your choice: ") 
  if choice == '1':
    print("The list of books with cost: ",books) 
  elif choice == '2':
    new= input("Enter the name of the book you would like to add ") 
    cost = int(input("enter the cost of the book"))
    books[new]= cost
    print("The new name is added. The updated list is ",books) 
  elif choice == '3':
    change = input("Enter the name that you would like to change ") 
    if change in books.keys():
      cost = input("Enter the cost ")
      books[change] = int(cost)
      print("The cost has been changed. The updated list is ",books) 
    else:
      print("book name is not in the list")
  elif choice == '4':
    print("Thank you.") 
    break 
  else:
    print("Try again")  
