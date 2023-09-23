class Solution(object):
    def isValid(self, s):
        todo = dict(('()', '[]', '{}'))
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            elif len(stack) == 0 or i != todo[stack.pop()]:
                return False
        return len(stack) == 0