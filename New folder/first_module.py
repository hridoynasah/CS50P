print(__name__)  # Output: __main__
print(f"First module's name: {__name__}")

def main():
    print("Main function is calling.") 

if __name__ == "__main__": # If this is running directly by python    
    main() # It will not call if I don't run this file form first_module.py 