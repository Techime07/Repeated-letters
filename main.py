word = list(input("Word: "))
new_list = []

for a in word:
    if a not in new_list:
        new_list.append(a)
        print(new_list)
