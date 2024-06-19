import string

def remove_punctuation(input_string):
    translator = str.maketrans("", "", string.punctuation)
    cleaned_string = input_string.translate(translator)
    return cleaned_string

input_string = "Hello, world! This is a test string."
cleaned_output = remove_punctuation(input_string)
print(cleaned_output)
