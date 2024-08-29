class Solution:
    # time complexity = o(S)=~o(n), S is the total number of characters in all strings combined
    # space complexity = o(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Check if the input list is empty. If so, return an empty string
        if not strs:
            return res  # Return empty string if the list is empty

        # Start with the first string in the list as the initial prefix
        prefix = strs[0]

        # Iterate over the remaining strings in the list from strs[1] to end of strs
        for s in strs[1:]:
            # While the current string does not start with the prefix
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Shorten the prefix by one character from the end, [:-1] removes charachter from the end and [:1] from start
                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""

        return prefix




'''
dryrun:
Setup:
   strs = ["flower", "flow", "flight"]
   
   prefix=flower
   
for s in strs[1:]:
iteration 1: strs[1]=flow
  flow.startwith(flower) ? No, remove last letter from prefix
  prefix=flowe
  flow.startwith(flowe) ? No, remove last letter from prefix
  prefix=flow
  flow.startwith(flow)? yes 
  
  prefix=flow
iteration 2: strs[2]=flight
 flight.startwith(flow) ? No, remove last letter from prefix
  prefix=flo
  flight.startwith(flo) ? No, remove last letter from prefix
  prefix=fl
  flight.startwith(fl) ? yes, 
  prefix=fl
  
reached to the end of list of strs
return prefix
  Answer =>prefix="fl"
'''