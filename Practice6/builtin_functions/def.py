
l = [11,21,41,51,34,12]


a = sum(list(map(lambda x: x % 10 == 1, l)))
print(a)