# Roman to Integer

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 

Original
Python3
 **Example 1:** 

```
Input: s = "III"
Output: 3
Explanation: III = 3.

```

 **Example 2:** 

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

```

 **Example 3:** 

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

```

 

 **Constraints:** 

- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

## Solution

**Language:** Python  
**Runtime:** 10 ms (beats 19.82%)  
**Memory:** 19.1 MB (beats 78.20%)  
**Submitted:** 2026-11-11T18:43:23.681Z  

```py
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        
        while i < len(s):
           
            two_letters = s[i:i+2]
            
            # 1. Check the 6 special 2-letter pairs first
            if two_letters == "IV":
                total += 4
                i += 2  # Skip both letters
            elif two_letters == "IX":
                total += 9
                i += 2
            elif two_letters == "XL":
                total += 40
                i += 2
            elif two_letters == "XC":
                total += 90
                i += 2
            elif two_letters == "CD":
                total += 400
                i += 2
            elif two_letters == "CM":
                total += 900
                i += 2
                
            # 2. Otherwise, check the single letter
            else:
                one_letter = s[i]
                if one_letter == 'I':
                    total += 1
                elif one_letter == 'V':
                    total += 5
                elif one_letter == 'X':
                    total += 10
                elif one_letter == 'L':
                    total += 50
                elif one_letter == 'C':
                    total += 100
                elif one_letter == 'D':
                    total += 500
                elif one_letter == 'M':
                    total += 1000
                i += 1  # Move forward by 1 letter
                
        return total

```

---

[View on LeetCode](https://leetcode.com/problems/roman-to-integer/)