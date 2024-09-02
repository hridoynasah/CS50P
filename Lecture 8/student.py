def main():    
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    # We can use dictionary to return both name, and house.
    # But python support multiple return.
    name = input("Name: ")
    house = input("House: ")
    # Return tupple 
    return (name, house)


if __name__ == "__main__":
    main()
