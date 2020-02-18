file = open('../_datasets/moby_dick.txt', mode='r')

print(file.read())
print(file.closed)
file.close()


print(file.closed)
