

# def normalFunction():
#     i=0
#     while i<5:
#         i+=1
#     return i

# print(normalFunction())


def yieldFunction():
    i=0
    while i<5:
        i+=1
        yield i

for i in yieldFunction():
    print(i)

