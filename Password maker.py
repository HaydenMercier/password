import os

def generate_password(x, y, z, a, b):
    possible_ascii = []
    password = ""
    if x:
        possible_ascii.extend(range(52, 61))
    if y:
        possible_ascii.extend(range(33, 47))
        possible_ascii.extend(range(58, 64))
        possible_ascii.extend(range(123, 126))
    if z:
        possible_ascii.extend(range(65, 90))
    possible_ascii.extend(range(97, 122))
    for _ in range(os.urandom(1)[0] % (b - a + 1) + a):
        password += chr(possible_ascii[os.urandom(1)[0] % len(possible_ascii)])
    return password

allow_numbers = input("Allow numbers: ").lower() in ["yes", "true"]
allow_special_chars = input("Allow special characters: ").lower() in ["yes", "true"]
allow_capital_chars = input("Allow capital letters: ").lower() in ["yes", "true"]
min_length = int(input("Minimum Length: "))
max_length = int(input("Maximum Length: "))

print(generate_password(allow_numbers, allow_special_chars, allow_capital_chars, min_length, max_length))