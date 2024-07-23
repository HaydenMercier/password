import os
allchars = []
upperletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowerletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
special_characters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "/", "?"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
password = ""
minsize = int(input("Minimum Length: "))
maxsize = int(input("Maximum Length: "))
allow_numbers = input("Allow numbers: ").lower() in ["yes", "true"]
allow_special_characters = input("Allow special characters: ").lower() in ["yes", "true"]
allow_capital_letters = input("Allow capital characters: ").lower() in ["yes", "true"]
if allow_numbers:
    allchars.extend(numbers)
if allow_special_characters:
    allchars.extend(special_characters)
if allow_capital_letters:
    allchars.extend(upperletters)

allchars.extend(lowerletters)

for _ in range(os.urandom(1)[0] % (maxsize - minsize + 1) + minsize):
    password += allchars[os.urandom(1)[0] % len(allchars)]

print(password)