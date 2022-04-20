# Jack Micher
# 11/12/20
# CS/IT 200-03
# Lab 10 Sorting

from sorting import *
import random
import timeit

def main():
    userinput = ''
    listgen = [] # the BASE list, will not be sorted in testing
    listtosort = []
    
    print("-----Commands-----\ngeneratelist  testsort  baselist  lastsort  help  exit")
    while userinput != "exit":
        print(">", end=' ')
        userinput = input().lower()
        
        if userinput == "generatelist": # user chooses to generate a base sorted list or random list for testing
            print("Enter length of list:")
            userlen = int(input())
            
            validtype = False
            while validtype is False: # loop until user selects a valid option
                print("Enter type of list (random, sorted, backsorted):")
                usertype = input().lower()
                
                validtype = True
                if usertype == "random":
                    listgen = [random.randrange(0, userlen*10) for i in range(userlen)] # generate base list filled with random integers within range of 0 to length*10
                    print("Random base list generated.")
                elif usertype == "sorted":
                    listgen = list(range(userlen)) # generate base list filled with integers in order from 0 to length-1
                    print("Sorted base list generated.")
                elif usertype == "backsorted":
                    listgen = list(range(userlen)) # generate base list filled with integers counting down from length to 0
                    print("Sorted base list generated.")
                else:
                    print("Please enter a valid type")
                    validtype = False
        
        if userinput == "testsort":
            listtosort = listgen[:]
            validtype = False
            
            while validtype is False: # loop until user selects a valid option
                print("Enter type of sort (selection, insertion, bubble, merge, quick):")
                usertype = input().lower()
                
                starttime = timeit.default_timer()
                
                validtype = True
                if usertype == "selection":
                    selection_sort(listtosort)
                elif usertype == "insertion":
                    insertion_sort(listtosort)
                elif usertype == "bubble":
                    bubble_sort(listtosort)
                elif usertype == "merge":
                    merge_sort(listtosort)
                elif usertype == "quick":
                    quick_sort(listtosort)
                else:
                    print("Please enter a valid sort.")
                    validtype = False
                
                endtime = timeit.default_timer()
            
            timems = round((endtime-starttime) * 1000)
            timesec = round(endtime-starttime)
            print("Sort time: " + str(timesec) + " seconds or " + str(timems) + " milliseconds.")
        
        if userinput == "baselist":
            print(listgen)
        
        if userinput == "lastsort":
            print(listtosort)
        
        if userinput == "help":
            print("This program allows the user to test the time of sorting algorithms based off a user generated base list.")
            print("The base list is NOT modified when testing using the sorting algorithms.")
            print("Command Descriptions:")
            print("generatelist: Create a new base list.")
            print("testsort: Choose a sort method to test the base list with.")
            print("baselist: Print out the base list.")
            print("lastsort: Print out the list after the last sort operation")
            print("help: Hello there!")
            print("exit: Exit the program")
        
if __name__ == "__main__":
    main()