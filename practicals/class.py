class students:
    def __init__(self, rollNo,name):
        self.rollNo = rollNo
        self.name = name
        
    def displayDetails(self):
        print(f"Roll no: {self.rollNo}")
        print(f"Name: {self.name}")
            
student1 = students(101,"Messi")
student2 = students(102,"Neymar")

student1.displayDetails()
student2.displayDetails()