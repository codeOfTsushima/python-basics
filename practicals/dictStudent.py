students = {
    101: "Kartik",
    102: "Messi",
    103: "Neymar"
}
rollNo = 102
print(f"Student with roll number {rollNo}:{students[rollNo]}")

students[104] = "Ronaldo"
print("Added new student")

for roll,name in students.items():
    print(f"Roll Number: {roll}, Name: {name}")