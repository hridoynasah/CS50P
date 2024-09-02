def main():
    student = getStudent()
    if student[0] == "Padma":
        student[1] = "India"
    print(f"{student[0]} from {student[1]}")

def getStudent():
    name = input("Name: ")
    house = input("House: ")
    # returning a list : List is mutable
    return [name,house]

if __name__ == "__main__":
    main()