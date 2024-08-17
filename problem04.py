# Vowel or Consonant:
# Write a Python program that takes a single character as input and checks whether
# it is a vowel or a consonant.

char = input("Enter a single  alphabet: ")
char = char.lower()
vowels = ['a','e','i','o','u']
isCheck = False
for i in vowels:
    if i == char:
        isCheck = True
        break
if isCheck:
    print("Its a vowel letter")
else:
    print("its a consonants")