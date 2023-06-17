# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in range(len(tokens)):
            ### if item is an operator, we take the two last seen numbers and perform the operation
            if tokens[x] == "+":
                p = stack.pop() + stack.pop()
                ### by popping we remove the last two items and then append the new value
                stack.append(p)
            elif tokens[x] == "*":
                m = stack.pop() * stack.pop()
                stack.append(m)
            elif tokens[x] == "-":
                ### in the case of divide and subtract, we want to perform the operation in the order that numbers appeared, 
                # hence we assign the pops to a and b and perform op backwards 
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif tokens[x] == "/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            
            else:
                stack.append(int(tokens[x]))
        

        ### should only be one item in stack
        return stack[0]
        
       