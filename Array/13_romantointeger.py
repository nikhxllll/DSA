class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
        'I': 1,    # 1
        'V': 5,    # 5
        'X': 10,   # 10
        'L': 50,   # 50
        'C': 100,  # 100
        'D': 500,  # 500
        'M': 1000  # 1000
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res
    

    
    # hashset is used