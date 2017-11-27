pal_maybe = str(input("Enter word to check if palindrome"))
is_palindrome = True
for i in range(0, len(pal_maybe) // 2):
    if pal_maybe[i] != pal_maybe[[len] - 1 -i]:
        is_palindrome = False
        break

    if is_palindrome:
        print("palindrome")
    else:
        print("no palindrome")