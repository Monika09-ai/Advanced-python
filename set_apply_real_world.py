maths_students={"nitu","monika","mohit","rohit","ram","karishma","keshav","sumit","kartik","aryan","vishnu"}
science_students={"monika","karishma","radha","ravi","rasha","tamur","nikhil","sneha","kartik","keshav","prabhu"}

all_students=maths_students.union(science_students)
print("Union(maths or science):",all_students)

both_subjects=maths_students.intersection(science_students)
print("intersection(both subjects common students):",both_subjects)

symmetric_students = maths_students.symmetric_difference(science_students)
print("symmetric(not common students in both of subjects):",symmetric_students)

maths_students.add("soham")
science_students.add("salu")
print("new added students in maths:",maths_students)
print("new added students in science:",science_students)

maths_students.add("ram")
science_students.add("tamur")
print("removed the student in maths:",maths_students)
print("removed the student in science:",science_students)



      
      
      
      
      
      
      
      
      
      
      
      
