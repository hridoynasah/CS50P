def main():
    student = getStudent()
    if student["name"] == "Padma":
        student["house"] = "India"
    print(f"{student['name']} from {student['house']}")

def getStudent():
    # Create empty dictonary : dictionary is mutable
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    # returning a dictionary
    return student

if __name__ == "__main__":
    main()