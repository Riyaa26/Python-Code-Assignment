def count_character_frequency(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

# Example usage
input_string = "hello world"
frequency = count_character_frequency(input_string)

# Print the frequency dictionary
print(frequency)
