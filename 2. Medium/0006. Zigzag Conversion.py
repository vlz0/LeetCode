class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
            
        result = [''] * numRows
        row, jump = 0, 1

        for char in s:
            result[row] += char
            if row == 0:
                jump = 1
            elif row == numRows - 1:
                jump = -1
            row += jump
        
        return ''.join(result)
