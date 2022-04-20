# Jack Micher
# 10/8/20
# CS/IT 200-03

import linked_binary_tree

class TwentyGame(linked_binary_tree.LinkedBinaryTree):
    
    def __init__(self):
        """
        Create a new instance of the question game tree where it distinguishes a cat and snake with a question about legs
        The left leaf of a node is the YES answer and the right leaf is the NO answer
        """
        super().__init__()
        self._add_root("Does it have legs?")
        self._add_left(self.root(), "cat")
        self._add_right(self.root(), "snake")
    
    def get_node_element(self, p):
        node = self._validate(p)
        return node._element
    
    def new_question(self, q, correct, cleaf):
        """
        q = New question string (new element)
        correct = Correct animal answer (new element)
        cleaf = The leaf that the game currently points to (position)
        Takes the correct animal answer and adds it to a left child, takes the element of the leaf and copies it to a right child
        Replaces the now current non-leaf node element with the question string (_replace)
        """
        self._add_left(cleaf, correct)
        self._add_right(cleaf, self.get_node_element(cleaf))
        self._replace(cleaf, q)




def play_game():
    newgame = TwentyGame()
    
    try:
        newgame = newgame.load_tree('gametree.dat')
    except:
        print("Invalid save data found, using default data")
    
    contgame = 1 # Flag for continuing game
    
    while contgame == 1:
        currnode = newgame.root() # Start at root position of question tree
        
        print("Think of an animal, I will guess it.") # Game starts here
        print("Input 'Yes' or 'No' to the questions I ask.")
        
        contgame = 2
        
        while contgame == 2:
            
            if newgame.is_leaf(currnode) == False: # Check if current node at position is not a leaf
                print(newgame.get_node_element(currnode)) # Print out a question for the user to answer
                userinput = input()
                userstr = userinput.lower()
                
                if userstr == 'yes':
                    currnode = newgame.left(currnode)
                elif userstr == 'no':
                    currnode = newgame.right(currnode)
                else:
                    print("Please input a valid answer ('Yes' or 'No')")
            else:                                                            # If the current node IS a leaf
                print("Is it a " + newgame.get_node_element(currnode) + "?") # Ask if the animal at this node is correct
                userinput = input()
                userstr = userinput.lower()
                
                if userstr == 'yes': # Win condition
                    print("I win!")
                elif userstr == 'no': # If no, ask for a question, then call new_question using the new question, the animal, and the current node
                    print("I give up, what is it?")
                    userinput = input()
                    print("Please type a question whose answer is yes for " + userinput + " and no for " + newgame.get_node_element(currnode))
                    userques = input()
                    newgame.new_question(userques, userinput, currnode)
                else:
                    print("Please input a valid answer ('Yes' or 'No')")
                
                print("Continue?")
                userinput = input()
                userstr = userinput.lower()
                if userstr == 'yes': # Goes back to upper loop to initiate start of game
                    contgame = 1
                elif userstr == 'no': # Breaks out of the loop
                    contgame = 0
                    print("Good-bye.")
                else:
                    print("Please input a valid answer ('Yes' or 'No')")
                
                newgame.save_tree('gametree.dat') # Saves every loop

play_game() # Call to the method containing the game

    