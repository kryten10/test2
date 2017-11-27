from string import ascii_lowercase
print(ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz

def main():
    dict_of_letters = dict()
    infile = open("nk.txt")
    for line in infile:
        for letter in line:
            if letter.lower() in ascii_lowercase:
                if letter in dict_of_letters:
                    dict_of_letters[letter] += 1
                else:
                    dict_of_letters[letter] = 1
    infile.close()
    print(dict_of_letters)

main()

