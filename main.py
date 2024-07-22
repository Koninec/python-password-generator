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

def main():
    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
    password = generate_password(length, use_letters, use_digits, use_punctuation)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()