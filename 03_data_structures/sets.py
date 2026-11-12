# Sets  no duplicates, unorderd

# numbers = {1,2,2,3,3,4,5}

# print(numbers)
# print(type(numbers))
# print(len(numbers))

# numbers = {10,20,30}

# numbers.add(40)
# numbers.remove(20)

# print(numbers)

# # intersection - returns only elements exist in both sets

# x = {1,2,3,4}
# y = {3,4,5,6}

# print(x.intersection(y))


# union - combines all unique elements from two sets

a = {1,2,3,4}
b = {3, 4, 5,6}

c = a.union(b)

print(c)

# // Difference - returns elements that exist in the first set but not the second

x = {1,2,3,4}
y = {3, 4, 5,6}

z = a.difference(b)

print(z)
print(a.symmetric_difference(b))


