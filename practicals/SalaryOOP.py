class Employee:
    def __init__(self, empId, empSalary):
        self.empId = empId
        self.empSalary = empSalary
        
    def displayDetails(self):
        print(f"Employee Id: {self.empId}")
        print(f"Employee salary: {self.empSalary}")
        
emp1 = Employee(1,50000)
emp2 = Employee(2,55000)

emp1.displayDetails()
emp2.displayDetails()