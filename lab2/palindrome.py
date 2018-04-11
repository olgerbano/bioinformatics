def is_palindrome(word):

    letters = list(word)    
    is_palindrome = True
    i = 0

    while len(letters) > 0 and is_palindrome:       
        if letters[0] != letters[(len(letters) - 1)]:
            is_palindrome = False
        else:
            letters.pop(0)
            if len(letters) > 0:
                letters.pop((len(letters) - 1))

    return is_palindrome

def is_palindrome2(word):
    return word == word[::-1];

word = input("enter word: ")

if is_palindrome(word):
    print("Is palindrome");
else:
    print("Is not palindrome");

if is_palindrome2(word):
    print("Is palindrome");
else:
    print("Is not palindrome");
