"""
Inheritance: https://www.hackerrank.com/challenges/inheritance/problem
"""
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName,lastName,idNum)
        self.scores = scores
        
    def calculate(self):
        grade_sum = 0
        for i in self.scores:
            grade_sum += i
        avarage_grade = grade_sum / len(self.scores)
        if 100>= avarage_grade >= 90 :
            return "O"
        elif 90 > avarage_grade >= 80:
            return "E"
        elif 80 > avarage_grade >= 70:
            return "A"
        elif 70 > avarage_grade >= 55:
            return "P"
        elif 55 > avarage_grade >= 40:
            return "D"
        else:
            return "T"
            
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
