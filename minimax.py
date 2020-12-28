# A simple Python3 program to find 
# maximum score that 
# maximizing player can get 
import math 

def repoChangeName():
  return max(3,2)

def minimax (curDepth, nodeIndex, 
             maxTurn, scores,  
             targetDepth): 
  
    # base case : targetDepth reached ##ITERATES 3 TIMES MAX
    if (curDepth == targetDepth):  
        return scores[nodeIndex] 
      
    if (maxTurn): #shorthand for if maxTurn == True
        return max(minimax(curDepth + 1, nodeIndex * 2,  
                    False, scores, targetDepth),  
                   minimax(curDepth + 1, nodeIndex * 2 + 1,  
                    False, scores, targetDepth)) 
      
    else: 
        return min(minimax(curDepth + 1, nodeIndex * 2,  
                     True, scores, targetDepth),  
                   minimax(curDepth + 1, nodeIndex * 2 + 1,  
                     True, scores, targetDepth)) 
      
# Driver code 
scores = [3, 5, 2, 9, 12, 5, 23, 23] 
  
treeDepth = math.log(len(scores), 2) #number of paths
  
print("The optimal value is : ", end = "") 
print(minimax(0, 0, True, scores, treeDepth)) 
  
# This code is contributed 
# by rootshadow


## MY QUESTIONS:

#1. How come finding the logarithm of the # of possible results (length of Score list)
#   and the number of "children" in a perfect binary tree (2) EQUALS the
#   number of possible paths?

#2. What exactly does this program solve in the big picture - optimal value for WHAT?

#ANSWERED QUESTIONS
#Why do we take the log of the length of the Score list, and 2? ANSWER: I assume 2
#has something to do with a perfect binary tree.
#Is this value, what we raise 2 to, the number of permutations?
#When I draw a pb tree with 8 results, there are 3 steps.
# What is an "optimal value"? I still don't understand what this program is looking for
