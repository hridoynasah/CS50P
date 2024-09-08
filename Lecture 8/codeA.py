# Default Constructor
class Student:
    name = "" # Instance variable 
    n = -1
    # default constructor
    def __init__(self):
        print("This is a default consturctor.")
        print("And this is called automatically.")
        
def main():
    student = Student()
    print(f"{student.name} & {student.name}")

if __name__ == ("__main__"):
    main()