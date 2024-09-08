class Student:
    # name = ""
    # id = 0
    # cgpa = 0
    # Default constructor
    def __init__(self, name, id, cgpa):
        self.name = name
        self.cgpa = cgpa
        self.id = id

def main():
    name = input("Name: ")
    Id = int(input("ID: "))
    cgpa = float(input("Cgpa: "))
    student = Student(name, Id, cgpa)
    print(f"Name: {name}, Id: {Id}, Cgpa: {cgpa}")

if __name__ == "__main__":
    main()