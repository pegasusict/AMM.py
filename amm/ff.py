#!/bin/python3
"""
    :author:Mattijs Snepvangers
    :version:0.0.0
"""

# list
x = [1, 3, 5]
x[0] = 99  # replace
x.insert(0, 99)  # push
x.remove(99)  # remove first occurence  of value

## set
x = {'Hello', 'World'}
# DOES NOT HOLD ORDER

## tuple
# a tuple can not be altered after creation
x = (1, "hi")

## dictionairy
# keys must be unique, dict is unordered
x = {"a": 1, "b": 2}
x["b"] = 99  # update
x["c"] = 876  # insert

### ternary operator
marks = 75
grade = "failed" if marks < 50 else "Passed"

### None equals null in other languages


### loops
# for loop
for i in range(0, 101, 5):
    print(i)

y = [1, 435, 234, 87623, 3467]
for i, data in enumerate(y):
    print(i, data)

# while loop
z = [1, 3, 5, 7, 9, 11]
index = 0
while index < len(z):
    print(z[index])
    index += 1

## min & max
values = [978, 78, 123, 135, 76, 213, 657, -123, 78, -34, 356, 234, -12, 45, 653]
# minimum, maximum = values[0], values[0]

# for item in values:
# if item < minimum: minimum = item
minimum = min(values)
maximum = max(values)
print(minimum, maximum)

### insertion
values = [978, 78, 123, 135, 76, 213, 657, -123, 78, -34, 356, 234, -12, 45, 653]
for i in range(0, len(values)):
    min_index = i

    for index in range(i, len(values)):
        if values[index] < values[min_index]:
            min_index = index

    print("Min = ", min_index, values[min_index])

    temp = values[i]
    values[i] = values[min_index]
    values[min_index] = temp
    print(values)
