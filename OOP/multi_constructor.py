class Student:
    def __init__(self):
        print("This is first default constructor.")
    
    def __init__(self):
        print("This is second default constructor.")

def main():
    # Second default constructor will get the priority
    student = Student()




if __name__ == "__main__":
    main()