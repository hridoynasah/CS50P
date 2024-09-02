def main():
    student = getStudent()
    if student["name"] == "Padma":
        student["house"] = "India"
    print(f"{student['name']} from {student['house']}")

def getStudent():
    # Create empty dictonary : dictionary is mutable
    
    name = input("Name: ")
    house = input("House: ")
    # returning a dictionary
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()