def main():
    enter_ints = list(input("enter some integers: "))
    print("unique numbers are: ", eliminatedups(enter_ints))

def eliminatedups(lst):
    result = []
    for i in lst:
        if not(i in result):
            result.append(i)
        return result

main()