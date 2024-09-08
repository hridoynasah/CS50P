class Student:
    
    # Instance variable or Attribute 
    name = ""
    house = ""


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():

    # Creating object of class
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    
    # returning the object
    return student

if __name__ == "__main__":
    main()