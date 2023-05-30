# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        ### every character has to have a closing character meaning s has to be equal to be valid
        if len(s) % 2 != 0: 
            return False
        
        stack = []
        

        for x in s:
            ### if an opening bracket we append to stack
            if x == "(" or x == "{" or x == "[":
                stack.append(x)
            ### we only pop if the corresponding opening bracket is the last item in stack
            ##  this means that all brackets are closed in the correct manner
            elif x == ")" and len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            elif x == "}" and len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            elif x == "]" and len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            ### if this isn't the case we append anyway
            else:
                stack.append(x)

        ### a valid string will be equal to zero after all appends and pops
        return True if len(stack) == 0 else False
        