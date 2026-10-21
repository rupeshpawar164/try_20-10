def adding(*args):
    result = 0
    for i in args:
        result += i
    return result

print(adding(10,20,30,40,50))

def print1_TO_n(n):
    for i in range(n):
        print(i, end=" ")

print1_TO_n(19)
print1_TO_n(19)
