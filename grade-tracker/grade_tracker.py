first_dict = {
    "abraham" : 90,
    "ahmer" : 70
}
print("Welcome to the Student Grades Tracker!")

def name():
    s_name = input("Enter New Student's Name: ").strip().lower()
    s_grade = int(input("Enter Studet's Grade: "))

    first_dict[s_name]= s_grade #go to first_dict and add s_name and s_grade
    print("Student added successfully.")
    print(first_dict)

def grade():
    while True:   #In case user put the wrong name, ask students name infinite times.
        s_name2 = input("Enter Existing Student's Name: ").strip().lower()

        if s_name2 in first_dict:   #check whether student exist in dict or not. [LINE 2]
            s_grade2 = int(input("Add Updated Grades: "))   #line 4: if student exist. it will ask for updated score
            first_dict[s_name2] = s_grade2
            print("Grade Updated Successfully.")
            print(first_dict)
            break
        else:
            print("Wrong Name. Enter Name Again.")   #CONTINUE [LINE 2]: if not, then it will ask the name agai.

def view_all():
    print(first_dict)

def search():
    while True: # In case user put wrong name, it will again ask the name
        tell = input("Tell Name of Existing Student: ")
        if tell in first_dict:
            print(f"{tell}'s score: {first_dict[tell]}") #if name is in the keys of first dict
            break
        else:
            print("Student Doesnt Exist. Ask Again.")

def exit():
    print("Exiting... Thank you for using the Student Grades Tracker!")

ask = int(input("Chose an option\n1. Add New Student\n2. Update Marks\n3. View Marks of all\n4. Search for a student\n5. Exit\n"))
    
if ask == 1:
    name()
elif ask == 2:
    grade()
elif ask == 3:
    view_all()
elif ask == 4:
    search()
elif ask == 5:
    exit()
else:
    print("Kindly Only Choose From The Given Options.")

