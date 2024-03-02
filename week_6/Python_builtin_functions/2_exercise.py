mylist = input()
low = list(filter(lambda x: x.isupper(), mylist))
up = list(filter(lambda x: x.islower(), mylist))
print(f"{len(low)} - lowercase letters\n{len(up)} - uppercase letters")
