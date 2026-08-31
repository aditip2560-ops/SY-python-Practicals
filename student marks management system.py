print("=====STUDENT MARKS MANAGEMENT SYSTEM=====")

marks=[65,75,85,95]

marks.append(96)
marks.pop(2)
marks[0]=55

print("updated list:",marks)
print("highest value:",max(marks))
print("average:",sum(marks)/len(marks))
