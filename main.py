from dotenv import load_dotenv
import os
import math
str1 = "ABCABC"
str2 = "ABC"

load_dotenv()

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    
    gcd_len = math.gcd(len(str1), len(str2))
    return str1[:gcd_len]

print(gcdOfStrings(str1, str2))


