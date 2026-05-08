

import random
import string

def password_generator():
    print("🔐 Password Generator")

    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    while True:
        length = int(input("\nPassword length (8-32): ") or 12)
        if 8 <= length <= 32:
            break
        print("❌ Length must be 8-32 characters!")

    num_passwords = int(input("Number of passwords (1-10): ") or 1)

    print(f"\n🔑 Generated Passwords:")
    print("=" * 50)

    for i in range(num_passwords):
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"{i+1}. {password}")

# Run generator
password_generator()
