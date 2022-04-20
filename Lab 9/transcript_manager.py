# Jack Micher
# 11/12/20
# CS/IT 200-03
# Lab 9 Transcript Manager

from red_black_tree import RedBlackTreeMap
from course import Course

def calcgpa(letter): # Method to calculate a grade string and return a GPA float, based on 4.0 scale
    
    grade = letter.upper()
    gpa = 0.0
    if grade == 'A':
        gpa = 4.0
    elif grade == 'A-':
        gpa = 3.7
    elif grade == 'B+':
        gpa = 3.3
    elif grade == 'B':
        gpa = 3.0
    elif grade == 'B-':
        gpa = 2.7
    elif grade == 'C+':
        gpa = 2.3
    elif grade == 'C':
        gpa = 2.0
    elif grade == 'C-':
        gpa = 1.7
    elif grade == 'D+':
        gpa = 1.3
    elif grade == 'D':
        gpa = 1.0
    elif grade == 'D-':
        gpa = 0.7
    elif grade == 'F':
        gpa = 0.0
    
    return gpa
    
def main():
    currtranscript = RedBlackTreeMap()
    menuinput = ''
    
    print("-------- Transcript Manager Main Menu --------")
    print("Commands:\nadd\tlookup\tshowall\tload\tsave\thelp\texit")
    
    while menuinput != "exit":
        print("Enter command:")
        menuinput = input().lower()
        # print(menuinput)
        
        if menuinput == "help": # Re-state the available commands
            print("Commands:\nadd\tlookup\tshowall\tgetgpa\tload\tsave\thelp\texit")
        
        if menuinput == "add": # Add a course to the transcript with specifications from the user
            print("ADD COURSE")
            addinfo = []
            print("Enter course code: ", end='') # goes first in course item
            addinfo.append(input().upper())
            print("Enter course name: ", end='') # goes second in course item
            addinfo.append(input())
            print("Enter course credits: ", end='')
            addinfo.append(input())
            print("Enter course grade: ", end='')
            addinfo.append(input())
            print("Enter course semester: ", end='')
            addinfo.append(input())
            print("Enter course instructor: ", end='')
            addinfo.append(input())
            newcourse = Course(addinfo[0],addinfo[1],addinfo[2],addinfo[3],addinfo[4],addinfo[5])
            currtranscript[newcourse.getcode()] = newcourse
        
        if menuinput == "lookup": # Find a course in the transcript
            print("COURSE LOOKUP\nEnter Course Code: ", end='')
            searchcourse = currtranscript[input().upper()]
            print("Code\tCredits\tGrade\tSemester\tInstructor\t\tCourse Name")
            print("------------------------------------------------------------------------------")
            print(searchcourse)
        
        if menuinput == "showall": # Show every course currently entered in the transcript
            print("ALL COURSES ON CURRENT TRANSCRIPT")
            print("Code\tCredits\tGrade\tSemester\tInstructor\t\tCourse Name")
            print("------------------------------------------------------------------------------")
            for coursecode in currtranscript:
                print(currtranscript[coursecode])
        
        if menuinput == "getgpa": # get GPA of all courses on the transcript
            print("Calculating Total GPA...")
            sumgpa = 0.0
            for key in currtranscript:
                sumgpa += calcgpa(currtranscript[key].getgrade())
            totalgpa = sumgpa/len(currtranscript)
            print("Total GPA: {:.3f}".format(totalgpa))
        
        if menuinput == "fieldgpa": # Ask the user for a field course code prefix (ex. CS, ENGL) to find the total GPA of courses in that field
            print("Enter field course code prefix (ex. CS, ENGL): ", end='')
            prefix = input()
            prefixnext = prefix[0:-1] + chr(ord(prefix[-1]) + 1) # Get string based off of prefix, but have it be alphabetically ahead (Ex. prefix is CS, makes CT)
            fielditer = currtranscript.find_range(prefix, prefixnext)
            
            sumgpa = 0.0
            fieldcount = 0
            for course in fielditer:
                sumgpa += calcgpa(course[1].getgrade())
                fieldcount += 1
            totalgpa = sumgpa/fieldcount
            print("Field GPA: {:.3f}".format(totalgpa))
            
        if menuinput == "load": # Load transcript pickle
            print("Type exact file name to load (case-sensitive with suffix, ex: 'examplefile.dat'): ", end='')
            filename = input()
            try:
                currtranscript = currtranscript.load_tree(filename)
            except:
                print("Invalid file name.")

        if menuinput == "save": # Save transcript as pickle
            print("Type name to save file as (will be saved as .dat): ", end='')
            usrinput = input()
            usrinput += ".dat"
            currtranscript.save_tree(usrinput)
            
if __name__ == "__main__":
    main()