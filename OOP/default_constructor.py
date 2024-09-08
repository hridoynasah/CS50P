class Student:
    "This class is about default constructor."
    def __init__(self) :
        print("This is a default constructor.")
        print("Which is called automatically.")
        print("At the time of object creation.")
        "This is a default constructor."

def main():
    student = Student()
    print(Student.__doc__)

if __name__ == "__main__":
    main()