# notes
# for a valid parenthesis, there will be a symmetrical middle 
# each type of parenthes is only closed by its mirror
# the middle must be valid and the parenthesis outside it and so forth
# we can add parenthesis to a stack, and when they are closed in order
# we can remove
# By using a hash map, can make tie the correct open bracket to its closed counter
# If there are remains in stack after the iteration, then it is invalid
# if not, return true
# since we check all elements, only once big O will big O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Hmap= {")":"(", "}":"{", "]":"[" }
        for i in s:
            if i in Hmap:
                if stack[0] and stack[-1] == Hmap[i]:
                    stack.pop()
                else: 
                    return false
            else: 
                stack.append(i)
        return True if not stack else False
                    



    






        
