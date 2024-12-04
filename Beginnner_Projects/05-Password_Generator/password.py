import random
import string
import pyperclip  # Install using: pip install pyperclip

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special_chars=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12, include_uppercase=True, include_digits=True, include_special_chars=True):
    passwords = [generate_password(length, include_uppercase, include_digits, include_special_chars) for _ in range(num_passwords)]
    return passwords

def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Password copied to clipboard:", text)

if __name__ == "__main__":
    # Example usage of generating and copying a single password
    password = generate_password(length=16, include_uppercase=True, include_digits=True, include_special_chars=True)
    copy_to_clipboard(password)
    print("Generated Password:", password)

    # Example usage of generating multiple passwords
    num_passwords = 5
    passwords_list = generate_multiple_passwords(num_passwords, length=12, include_uppercase=True, include_digits=True, include_special_chars=True)
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords_list):
        print(f"Password {i+1}: {password}")

    # Copy the first password to the clipboard
    copy_to_clipboard(passwords_list[0])
