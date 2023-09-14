def lengthOfLongestSubstring(s: str) -> int:
    substring=''
    longest_substring=0
    i=0
    while (i<len(s)):
        if s[i] not in substring:
            substring=substring+s[i]
            longest_substring=max(longest_substring, len(substring))
        
        elif s[i] in substring:
            substring=substring[substring.index(s[i])+1: len(substring)]
            substring=substring+s[i]
            longest_substring=max(longest_substring, len(substring))
        i+=1
    return(longest_substring)             

print(lengthOfLongestSubstring("loolololo"))   



