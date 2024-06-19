def to_title_case(input_string):
    words = input_string.split()
    title_case_string = ' '.join(word.capitalize() for word in words)
    return title_case_string

input_string = "hello world how are you"
title_case_output = to_title_case(input_string)
print(title_case_output)
