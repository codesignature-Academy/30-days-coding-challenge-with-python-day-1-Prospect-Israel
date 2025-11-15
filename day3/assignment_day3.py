print("---STUDENT ADMISSION CHECKER---")

score = int(input("Enter Jamb Score: "))
department = input("Applied Department: ")
# department = ("Anatomy", "Medicine and surgery", "law", "Accounting")
departments = {
  "Anatomy": 250, 
  "Medicine and surgery": 300, 
  "law": 270, 
  "Accounting" : 230,
  }


if department in departments:
  cutoff = departments[department]
  
  if score >= cutoff:
    dept = department.title()
    print(f"congrats, you were admmited into {dept}")
  
  else:
    dept = department.title()
    print(f"sorry, you were not admited into {dept}")

else:
  print("ïnvalid department")

