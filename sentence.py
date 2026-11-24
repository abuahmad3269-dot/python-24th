sentence = input("Enter a sentence: ")
word = ""

for ch in sentence:
    if ch == " ":
        if word != "":
            print(word)
            word = ""
    else:
        word = word + ch

if word != "":
    print(word)

