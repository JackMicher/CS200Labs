import lab4_queue
import stacks
import copy

def read_dictionary(filename):
    """Reads the file containing the list of words and stores it in wordlist"""
    wordlist = dict() # This will contain all of the words
    
    file = open(filename, 'r')
    for line in file:
        word = line.strip()
        length = len(word)
        if length in wordlist:
            wordlist[length].append(word)
        else:
            wordlist[length] = [word]
    
    return wordlist
    
def build_ladder(start, end):
    """
    Finds the shortest word ladder that connects start and end words.
    Returns None if such a ladder does not exist.
    """
    
    wordlist = read_dictionary('dictionary.txt') # Contains all of the allowed words
    
    used = set() # This will be a set of words that you have used while you searched
    
    word_ladders = lab4_queue.Queue() # This is your queue of stacks that will hold all of the word ladders in progress
    
    if len(start) != len(end):
        return
    
    current_word = start
    current_stack = stacks.ArrayStack()
    current_stack.push(current_word)
    
    while current_word != end:
        
        for i in wordlist[len(start)]: # For word 'i' of every word with equal length to the starting word
            diff_counter = 0
            
            for k in range(len(i)): # Check word 'i' with the current word to see how many different characters there are
                if i[k] != current_word[k]:
                    diff_counter += 1
            
            if diff_counter == 1 and i not in used: # If the difference in characters is 1 and the word has not been matched yet
                add_stack = copy.deepcopy(current_stack)
                add_stack.push(i)
                word_ladders.enqueue(add_stack)
                used.add(i)
        
        current_stack = word_ladders.dequeue()
        current_word = current_stack.top()
        
    
    # print(word_ladders)
    
    
    
def main():
    build_ladder('fox', 'fit')

main()
    
    
