# a list of dictionaries to hold the hogwarts students name, House & Patronus
students = [
            {"Name":"Hermione", "House":"Gryffindor", "Patronus":"Otter"},

            {"Name":"Harry", "House":"Gryffindor", "Patronus":"Stag"},

            {"Name":"Ron", "House":"Gryffindor", "Patronus":"Jack Russel Terrier"},

            {"Name":"Draco", "House":"Slytherin", "Patronus":None}
]

# a for loop to print out all of the students names along with the rest of their info
for student in students:
    print(student["Name"], student["House"], student["Patronus"], sep=', ')