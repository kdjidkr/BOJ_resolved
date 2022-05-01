def reverseString(s:list()) -> None:
    start = 0
    end = len(s)-1
    
    while start < end:
        s[start],s[end] = s[end],s[start]
        start += 1
        end -= 1
        
    print(s)