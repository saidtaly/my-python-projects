# Define the function to create a new string where each alternate character is uppercase and the others are lowercase
def alternate_case(string):
    # Create an empty string to hold the modified string
    result = ""
    # Iterate over each character in the input string and keep track of its index using the enumerate function
    for i, char in enumerate(string):
        # If the index of the character is even, make it uppercase using the upper method
        if i % 2 == 0:
            result += char.upper()
        # If the index of the character is odd, make it lowercase using the lower method
        else:
            result += char.lower()
    # Return the modified string
    return result

# Define the function to create a new string where each alternate word is uppercase and the others are lowercase
def alternate_word_case(string):
    # Split the input string into individual words using the split method
    words = string.split()
    # Create an empty list to hold the modified words
    result = []
    # Iterate over each word in the list of words and keep track of its index using the enumerate function
    for i, word in enumerate(words):
        # If the index of the word is even, make it lowercase
        if i % 2 == 0:
            result.append(word.lower())
        # If the index of the word is odd, make it uppercase
        else:
            result.append(word.upper())
    # Join the modified words together using the join method with a space delimiter
    # to create the modified string, and return it
    return " ".join(result)

# Prompt the user to enter a string input using the input function and store it in a variable
input_string = input("Enter a string: ")
# Call the alternate_case function with the input string as an argument and print the modified string
print("Alternate case: ", alternate_case(input_string))
# Call the alternate_word_case function with the input string as an argument and print the modified string
print("Alternate word case: ", alternate_word_case(input_string))
