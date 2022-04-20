# Jack Micher
# CSIT 200
# 10/29/20

from binary_search_tree import TreeMap
import timeit

class Term:
    """ Term class that stores a search term's weight and name """
    def __init__(self, query, weight):
        self._query = query
        self._weight = weight
        if self._query is None or self._query == '': # Check for an empty query and raise an error if true
            raise TypeError("No query input")
        if self._weight < 0: # Check to see if the weight is under 0 and raise an error if true
            raise ValueError("Query weight is negative")
    
    def get_weight(self):
        return self._weight
    
    def __eq__(self, other):
        if self._query == other:
            return True
        return False
    
    def __lt__(self, other):
        if self._query <= other:
            return True
        return False
    
    def __str__(self):
        rtrnstr = str(float(self._weight)) + " " + self._query
        return rtrnstr

def build_tree(filename):
    rtrnbst = TreeMap()
    with open(filename, 'r', encoding='utf-8') as file:
        filelines = file.readlines()[1:] # make list of all lines and exclude the first one
        for line in filelines: # iterate through each line in text file
            linestr = line.split(None, 1) # split the weight and string into a length 2 list
            linestr[1] = linestr[1].strip('\n') # remove line breaks, specifically newline \n
            rtrnbst[linestr[1]] = linestr[0] # insert into the tree with word as key and weight as value
    return rtrnbst

def all_matches(tree, prefix, resultlimit):
    
    start = timeit.default_timer() # Record start time
    
    endchar = prefix[-1] # Get last character of search term
    incendchr = chr(ord(endchar) + 1) # Incremement last character of prefix (ex. m to n)
    maxstr = prefix[0:-1] + incendchr
    matchlist = tree.find_range(prefix, maxstr) # Find range of words that has the same prefix as search prefix
    termlist = []
    
    for pair in matchlist:
        termlist.append(Term(pair[0], int(pair[1]))) # Assign weight, pair to Term item and append to termlist
    
    termlist.sort(key=Term.get_weight, reverse=True) # Sort termlist by weight
    
    print("Results:")
    limitcount = 0
    
    for pair in termlist: # Iterate through the term list
        print(pair) # Print word and weight
        limitcount += 1 # Keep track of total amount of results outputted
        if limitcount >= resultlimit: # If total amount outputted equals user number of requested results
            break
    
    end = timeit.default_timer() # Record end time
    
    totaltime = round((end-start) * 1000) # Get total time of operation of all_matches in ms
    print("Query took " + str(totaltime) + " ms")

def main():
    
    print("Enter file: ", end='')
    filestr = input()
    
    print("Enter number of results to show: ", end='')
    intinput = int(input())
    
    searchstr = None
    
    le_tree = build_tree(filestr) # Given files are wiktionary.txt and cities.txt
    
    while searchstr != '':

        print("Enter search: ", end='')
        searchstr = input()
        
        if searchstr == '':
            continue
        
        all_matches(le_tree, searchstr, intinput)

main()