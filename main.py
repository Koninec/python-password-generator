import random
import string

def generate_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

def get_character_set(use_letters, use_digits, use_punctuation, custom_chars):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    if custom_chars:
        characters += custom_chars
    if not characters:
        print("No character types selected. Defaulting to letters and digits.")
        characters = string.ascii_letters + string.digits
    return characters

def password_strength(password):
    length = len(password)
    unique_chars = len(set(password))
    strength = "Weak"
    if length >= 8 and unique_chars > 4:
        strength = "Moderate"
    if length >= 12 and unique_chars > 6:
        strength = "Strong"
    return strength

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    while True:
        length = get_positive_integer("Enter the desired password length: ")
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
        custom_chars = input("Enter any custom characters to include (or press Enter to skip): ")
        characters = get_character_set(use_letters, use_digits, use_punctuation, custom_chars)
        password = generate_password(length, characters)
        print(f"Generated password: {password}")
        print(f"Password Strength: {password_strength(password)}")
        
        repeat = input("Generate another password? (y/n): ").lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()