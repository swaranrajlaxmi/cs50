import importlib


# prompt user for text
text = input("Text: ")
TextLength = len(text)
# initialise parameters
sentences =letters = 0
words = 1
# count for letters, words, and sentences in the text
for i in range(TextLength):
    if (text[i].isalpha()):
        letters += 1
    elif (text[i].isspace()):
        words += 1
    elif (text[i] == "." or text[i] == "?" or text[i] == "!"):
        sentences += 1
print(letters)
print(words)
print(sentences)
# calculate coleman liau index
L = (letters / words) * 100
S = (sentences / words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)
if (index >= 16):
    print("Grade 16+")
elif (index <=1):
    print("Before Grade 1")
else:
    print(f"Grade {index}")



