import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_punctuation=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    if not characters:
        print("No character types selected. Defaulting to letters and digits.")
        characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def main():
    while True:
        length = get_positive_integer("Enter the desired password length: ")
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
        password = generate_password(length, use_letters, use_digits, use_punctuation)
        print(f"Generated password: {password}")
        
        repeat = input("Generate another password? (y/n): ").lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()