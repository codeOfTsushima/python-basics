class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def getSalary(self):
        return self.__salary
    
    def get_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid Salary amount!")
        
emp = employee("Parthip", 200000)
print(f"Employee Name: {emp.name}")