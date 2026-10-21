def adding(*args):
    result = 0
    for i in args:
        result += i
    return result

print(adding(10,20,30,40,50))