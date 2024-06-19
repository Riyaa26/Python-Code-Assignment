def q16(string):
    freq_dict = {}
    for char in string:
        if char in freq_dict :
            freq_dict[char] += 1 
        else:
            freq_dict[char] = 1
    return freq_dict 

 string = str(input("enter a string : "))
 freq = q16(string)
 print(freq)
