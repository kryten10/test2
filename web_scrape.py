import urllib.request


from string import ascii_lowercase

def main():
    dict_of_letters = dict()
    infile = urllib.request.urlopen('https://www.bbc.co.uk/news/')
    f = infile.read().decode()
    for line in f:
        for letter in line:
            if letter.lower() in ascii_lowercase:
                if letter in dict_of_letters:
                    dict_of_letters[letter] += 1
                else:
                    dict_of_letters[letter] = 1
    print(dict_of_letters)

main()
