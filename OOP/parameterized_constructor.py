class Student:
    def __init__(self, name, age, address):
        self.address = address
        self.name = name
        self.age = age


def main():
    student = Student("Hridoy Hasan", 23, None)
    print(student.name)
    print(student.age)
    print(student.address)





if __name__ == "__main__":
    main()