import random
import string

def generate_password(length):
    if length < 4:
        print("⚠️ Password length should be at least 4 characters.")
        return None

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    # Ensure at least one character from each type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        if password:
            print(f"\n✅ Generated Password: {password}\n")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
