import random
import string

def generate_random_password(length):
    """Generate a random password of the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Random Password Generator!")

    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
                continue
            password = generate_random_password(length)
            print("Generated Password:", password)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
