# Jack Micher
# 9/10/2020
# CS/IT 200-03

'''
    Python File for CS/IT 200 Lab 0
    Part 1: Testing dynamic_array.py methods
        __getitem__
        __setitem__
        pop()
        __eq__
'''

import dynamic_array                           # Import the dynamic_array module

testArray = dynamic_array.DynamicArray()       # Create new dynamic array: testArray

print("Current testArray:")
print(testArray)                               # Print the currently empty testArray

testArray.append(5)                            #
testArray.append(2)                            # Add 5, 2, and 7 to the end of testArray (in that order)
testArray.append(7)                            # (testing append())

print("Current testArray:")
print(testArray)                               # Print the modified testArray

print("Index 1 of testArray:")                 # Using __getitem__ in testArray to get value at index 1
print(testArray[1])
print("Index -1 of testArray:")                # Trying negative value with __getitem__ in testArray
print(testArray[-1])                           # Using this index should return 7
print("Index -3 of testArray:")
print(testArray[-3])
print("Index 0 of testArray:")
print(testArray[0])

testArray[0] = 'epic'                          # Testing __setitem__, replacing first index value

print("Current testArray:")
print(testArray)

print("Removing last value in testArray:")
print(testArray.pop())                         # Testing pop() method, removing & returning last index value

print("Current testArray:")
print(testArray)

print('--------------------------------------')

twostArray = dynamic_array.DynamicArray()      # Creating new array to test __eq__ with

twostArray.append('epic')
twostArray.append(2)

print("New array, twostArray:")
print(twostArray)

if testArray == twostArray:                    # Testing __eq__ with comparison operator ==
    print("Both testArray and twostArray are equal")
else:
    print("testArray and twostArray aren't equal")

print('--------------------------------------')

threestArray = dynamic_array.DynamicArray()

threestArray.append('intentionally')
threestArray.append('not')
threestArray.append('equal')

print("New array, threestArray:")
print(threestArray)

if testArray == threestArray:                  # Testing __eq__ with comparison operator ==
    print("Both testArray and threestArray are equal")
else:
    print("testArray and threestArray aren't equal")
