word = input("Enter a word: ").lower()
if word == word[::-1]:
    print("This word is a palindrome (reads same backwards).")
else:
    print("This word is not a palindrome.")
