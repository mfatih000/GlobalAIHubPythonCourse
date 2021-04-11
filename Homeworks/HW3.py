#Homework 3


students = {}
number_of_students = int(input("How Many Students Took The Exams? : "))
count = 0
while True:
    std_num = input("Which Student? : ")
    std_name = input("Student Name : ")
    std_surname = input("Student Surname : ")
    student_number = int(input("Student Number : "))
    midterm = int(input("Midterm Point : "))
    project = int(input("Project Point : "))
    final = int(input("Final Point: "))
    students.update({
        std_num: {
            "name": std_name,
            "surname": std_surname,
            "number":student_number,
            "midterm": midterm,
            "project": project,
            "final": final
        }
    })
    count += 1


    if count == number_of_students :
        break

points = {}
information = students.values()
print(information, len(information))
names = []
surnames = []
numbers = []
passingGrades = []
counter = 0
for i in information:
    passingGrade = i["midterm"] * (0.3) + i["project"] * (0.3) + i["final"] * (0.4)
    passingGrades.append(passingGrade)
    names.append(i["name"])
    surnames.append(i["surname"])
    numbers.append(i["number"])

information_list = list(zip(names, surnames, numbers, passingGrades))
def print_them(information_list):
    grades=[]
    for each in information_list:
        grades.append(each[3])
    grades.sort()
    length = len(grades)
    print("grades are ",grades)
    print("Name\tSurname\tNumber\tPassingGrade\n")
    while length>0:

        for line in information_list:
            if length == 0:
                break
            if grades[0] == line[3]:

                for element in line:
                    print(str(element),end='\t')
                print()
                grades.remove(grades[0])
                length-=1

print_them(information_list)
