import random
import string

# Function to generate a random password
def generate_password(length=12):
    if length < 8:
        print("It's recommended to have a password length of at least 8 characters for better security.")
    
    # Define possible characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters from the list
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Main program
def main():
    print("Password Generator")
    length = int(input("Enter the desired password length (minimum 8 characters): "))
    
    # Generate password
    password = generate_password(length)
    print(f"Your generated password is: {password}")

# Run the program
if __name__ == "__main__":
    main()
