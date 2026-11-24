word = input("Enter a word: ").lower()
check = ""

for ch in word:
    check = ch + check

if check == word:
    print("Palindrome")
else:
    print("Not a palindrome")

