# Jack Micher
# 9/3/2020
# CS/IT 200-03

'''
    Python File for CS/IT 200 Lab 0
    Part 1: Methods
        difference
        sum_even_cubes
        has_duplicate
        list_product
'''

def difference(numslist):
    listmax = numslist[0]
    listmin = numslist[0]
    
    # Goes through entire input list once to determine max and min
    for i in range(len(numslist)):
        if numslist[i] > listmax:
            listmax = numslist[i]
        if numslist[i] < listmin:
            listmin = numslist[i]
    
    return listmax - listmin

def sum_even_cubes(numin):
    
    sumof = 0
    # Loop sums cubes of the even numbers inbetween 0 and the user's input
    for i in range(0,numin,2):
        sumof += i ** 3
    
    return sumof

def has_duplicate(userlist):
    
    # For each item in the list, the nested loops will compare the current item
    # with every other item on the list
    for i in range(len(userlist)):
        for j in range(len(userlist)):
            if i != j:
                if userlist[j] == userlist[i]:
                    return True
    
    return False

def list_product(list1, list2):
    newlist = []
    for i in range(len(list1)):
        newlist.append(list1[i] * list2[i])
    return newlist

def main():
    # Testing difference()
    listawesoo = [4,2,7,7,8]
    print("Testing difference() with " + str(listawesoo))
    print("Result: " + str(difference(listawesoo)))
    
    # Testing sum_even_cubes()
    
    print("Testing sum_even_cubes() with 6")
    print("Result: " + str(sum_even_cubes(6)))
    print("Testing sum_even_cubes() with 9")
    print("Result: " + str(sum_even_cubes(9)))
    
    # Defining a few lists to test methods
    testlist1 = [1,2,1,2]
    testlist2 = [5,5,4,5]
    testlist3 = [2,3,4,5]
    
    # Testing has_duplicate()
    print("Testing has_duplicate() with " + str(testlist1))
    print("Result: " + str(has_duplicate(testlist1)))
    print("Testing has_duplicate() with " + str(testlist3))
    print("Result: " + str(has_duplicate(testlist3)))
    
    # Testing list_product()
    print("Testing list_product() with " + str(testlist1) + " and " + str(testlist2))
    print("Result: " + str(list_product(testlist1,testlist2)))
    
if __name__ == '__main__':
    main()
