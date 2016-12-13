#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0
   mCount = 0
   cCount = 0

   def __init__(self, name, salary, title):
      self.name = name
      self.salary = salary
      self.title = title
      Employee.empCount += 1
      if title=="Manager":
          Employee.mCount += 1
      if title=="Clerk":
          Employee.cCount += 1


   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary, "Title :", self.title

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000, "Clerk")
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000, "Manager")
"This would create third object of Employee class"
emp3= Employee("Daisy", 1000000, "Manager")
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print "Total Employee %d" % Employee.empCount
print "Total Manager %d" % Employee.mCount
print "Total Clerk %d" % Employee.cCount
