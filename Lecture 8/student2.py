def main():
    name, house = get_Student()
    print(f"{name} from {house}")

def get_Student():
    name = input("Name: ")
    house = input("House: ")
    # This is tuple: tuple is immutable
    return (name, house)

if __name__ == "__main__":
    main()