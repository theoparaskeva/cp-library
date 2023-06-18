# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, 
# and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. 
# If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

from typing import List

class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []
        for x in range(len(ast)):
            ### if asteroid is postitive we append
            if ast[x] > 0:
                stack.append(ast[x])
                
            ### if asteroid is negative
            else:
                ### if we have an item on the stack and it is positive, 
                # if current asteroid is larger we pop the destroyed asteroid on the stack
                while stack and stack[-1] > 0 and abs(ast[x]) > stack[-1]:
                    stack.pop()
            
                ### if there is nothing on the stack or top of stack is also negative we append the negative asteroid
                if not stack or stack[-1] < 0:
                    stack.append(ast[x])
                ### if asteroids are equal they are both destroyed 
                # so we pop the top of the stack and do not append the negative asteroid
                elif stack[-1] == -ast[x]:
                    stack.pop()
            

        return stack

