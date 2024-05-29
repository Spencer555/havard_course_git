people =[
    {"name": "harry", "House":"Gryffindor"},
    {"name": "Cho", "House":"Ravenclaw"},
    {"name": "Draco", "House": "Slytherin"}
]

# if we try to use the normal sort we would get an error so u have to tell the sort how u want it to sort it

# so assuming we want to sort by name we write a func that takes a person and returns the only the name field and pass it to the sort
# def f(person):
#     return person["name"]

# people.sort(key=f)

# we write it in lamba as this 
# it takes a person and returns the name
people.sort(key=lambda person: person["name"])

print(people)