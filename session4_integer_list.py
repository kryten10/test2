int_list = list()
newint = input("input an integer or 'q' to quit: ")
while newint != 'q':
    int_list.append(int(newint))
    newint = input("input an integer or 'q' to quit: ")
int_list.sort()
for e in int_list:
    print(e)