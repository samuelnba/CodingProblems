def strStr():
    haystack = "aaaaa"
    needle = "bba"

    if needle in haystack:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
    return -1

# 62.85%