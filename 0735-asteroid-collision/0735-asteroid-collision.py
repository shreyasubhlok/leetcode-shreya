class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]
        
        for a in asteroids:
            currAsteroid=a
            
            while len(stack)!=0 and currAsteroid<0 and stack[-1]>0:
                if abs(currAsteroid)>stack[-1]:
                    stack.pop()
                elif abs(currAsteroid)==stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(currAsteroid)
                
        return stack
