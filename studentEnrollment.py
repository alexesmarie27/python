
class Student:

  def _init_(self, fname, lname, grade):
    self.fname = fname
    self.lname = lname
    self.grade = grade
    self.classes = []

  def displayStudent(self):
    print "Name: ", self.fname, " ", self.lname, "\nGrade: ", self.grade, "\n"

  def enroll(self, className):
    if className in self.classes:
      print ("You are already enrolled in that class\n")
    else:
      self.classes.append(className)

  def dropClass(self, className):
    if className not in self.classes:
      print ("You are not enrolled in that class. You cannot drop.")
    else:
      self.classes.remove(className)

class Class:

  def _init_(self, className):
        self.className = className

classes = ["CS 1050", "MATH 4100", "GEOL 1000"]

for c in classes:
    print("Listed are the available classes: \n")
    print(c, "\n")

input("Please choose a class to enroll\n")
