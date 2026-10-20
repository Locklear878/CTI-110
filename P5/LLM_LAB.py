import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    """
    Generates a random password based on the user's specific functional requirements.
    """
    # Core entity base: lower-case letters are always included
    character_pool = string.ascii_lowercase
    
    # Conditionally expand character pool based on criteria
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    # Error isolation: Check if pool is somehow empty or length is invalid
    if not character_pool or length < 1:
        return "Error: Invalid criteria provided."

    # Generate random sequence from pool
    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("--- 🔐 Password Generator App ---")
    
    # User inputs with basic validation
    try:
        length = int(input("Enter desired password length (e.g., 8-32): "))
        if length <= 0:
            print("❌ Length must be a positive integer.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
        return

    # Gather booleans for password components
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Call generator and output results
    generated_password = generate_password(length, use_uppercase, use_numbers, use_special)
    
    print("\n========================================")
    print(f"🔑 Your Secure Password: {generated_password}")
    print("========================================")

if __name__ == "__main__":
    main()
