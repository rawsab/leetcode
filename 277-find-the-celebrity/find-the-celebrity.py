"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):

        suspect = 0

        for i in range(1, n):   # range(1, n) avoids knows(0, 0)
            
            # if knows(suspect, i) is true, suspect cannot be the celebrity
            
            # if knows(suspect, i) is false, then i cannot be the celebrity,
            # so we don't update the suspect
            
            if Celebrity.knows(suspect, i):
                suspect = i
        
        for j in range(n):
            if j == suspect:
                continue 

            # suspect is not the celebrity if:
            # - celebrity knows someone
            # - someone doesn't know the celebrity

            if Celebrity.knows(suspect, j) or not Celebrity.knows(j, suspect):
                return -1

        return suspect
