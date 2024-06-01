#creating a nested dict
classroom = {
"ajay":{
    "age": 15,
    "marks":[89,85,90,86,90]
},
"baskar":{
    "age": 15,
    "marks":[85,85,90,80,90]
},
"charles":{
    "age": 15,
    "marks":[89,85,96,86,90]
},
"prince":{
    "age": 15,
    "marks":[89,55,90,86,50]
},
"diana":{
    "age": 15,
    "marks":[85,85,95,76,90]
}
}
name = input("enter students name")
for i in classroom.keys():
    if name == i:
        mark = classroom[i]["marks"]
        total = sum(mark)
        print("total marks scored by {} is {}".format(name,total))
