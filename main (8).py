class Student:
  def __init__(self,name,rollnumber,cgpa):
    self.name=name
    self.rollnumber=rollnumber
    self.cgpa=cgpa
def sortstudents(studentlist):
  sortedstudents=sorted(studentlist,key=lambda student:student.cgpa,reverse=True)
  return sortedstudents
student1=Student("Sam","s123",3.7)
student2=Student("Saran","s124",3.8)
student3=Student("Hari","s125",3.9)
student4=Student("Karthick","s126",4.0)
students=[student1,student2,student3,student4]
sortedstudents=sortstudents(students)
for student in sortedstudents:
  print(f"Name:{student.name},Rollnumber:{student.rollnumber},CGPA:{student.cgpa}")