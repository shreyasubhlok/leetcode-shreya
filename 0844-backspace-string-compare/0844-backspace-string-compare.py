class Solution:
    '''
        # Time = o(n+m)~=o(n),n is the length of s and m is the length of t
        #Space Complexity: O(1)
        This is more efficient solution as compare to using stacks. But using stacks is also             accepted.
    '''
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        backspaceSCount = 0
        backspaceTCount = 0
        while i >= 0 or j >= 0:
            # Process the string s for backspaces
            while i >= 0:
                if s[i] == '#':
                    backspaceSCount = backspaceSCount + 1
                    i = i - 1
                elif backspaceSCount > 0:
                    i = i - 1
                    backspaceSCount = backspaceSCount - 1
                else:
                    break # Exit loop if no backspaces need to be applied

            # Process the string t for backspaces
            while j >= 0:
                if t[j] == '#':
                    backspaceTCount = backspaceTCount + 1
                    j = j - 1
                elif backspaceTCount > 0:
                    j = j - 1
                    backspaceTCount = backspaceTCount - 1
                else:
                    break # Exit loop if no backspaces need to be applied

            #print(f"Comparing strings : {s[i]} and {t[j]} ")
            # Compare the current characters of both strings if within valid indices
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False # Return False if characters do not match

            # Check if one string is exhausted while the other still has characters
            if (i>=0) != (j>=0):
                return False  #Return False if one string is not fully processed

            i = i - 1
            j = j - 1

        return True     # If all characters match after processing backspaces, return True
    
    
    
    

    '''
     Approach 2 using stacks
     Time = o(n+m)~=o(n),n is the length of s and m is the length of t
     Space =o(n+m)~=o(n), worst case both stacks hold all characters from the strings.
    '''
    def backSpaceCompareUsingStacks(self, s, t):
        stackS = []  # Stack to process characters in string s
        stackT = []  # Stack to process characters in string t
        for char in s:
            if char != "#":
                stackS.append(char)
            else:
                if stackS:
                    stackS.pop()  # pop from the stack only when it is not empty

        for char in t:
            if char != "#":
                stackT.append(char)
            else:
                if stackT:
                    stackT.pop()  # pop from the stack only when it is not empty

        # Return True if both stacks are equal, otherwise return False
        if stackS == stackT:
            return True
        else:
            return False

        '''
        if not stackT: checks whether the stack is empty before popping. However, the condition should be if stackS: to pop from the stack only when it is not empty
        '''