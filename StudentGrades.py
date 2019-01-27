ListStudents = ["Ronan", "Tom", "Liam", "Ross", "Tim"]
ListGrades = ["A", "B", "C", "D", "E"]
ListPercentages = ["100", "80", "65", "45", "23"]

print("{0:15} {1:15} {2:15}".format("Student", "Grade", "Percentage (%)"))
for i, index in enumerate(ListStudents):
    print("{0:15} {1:15} {2:15}".format(ListStudents[i], ListGrades[i], ListPercentages[i]))