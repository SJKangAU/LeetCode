class solution:
    def romanToInt(self, s:str) -> int:
        m = {
            "I" : 1, 
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            }
        
        number = 0

        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")
        for char in s:
            number += m[char]
        return number
    
#https://leetcode.com/problems/roman-to-integer/submissions/1135134102/