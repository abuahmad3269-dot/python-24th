word = input("Enter a string: ").lower()
vowels = 0
consonants = 0

for ch in word:
    if ch in "aeiou":
        vowels = vowels + 1
    elif ch >= "a" and ch <= "z":
        consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)


