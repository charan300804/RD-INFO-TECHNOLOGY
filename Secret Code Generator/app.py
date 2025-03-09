import string  # Importing the string module to access predefined sets of characters

def caesar_cipher(text, shift, mode='encode'):
    """
    Function to encode or decode a message using the Caesar cipher.
    
    :param text: The input message (string) to be encoded or decoded.
    :param shift: The number of positions each letter should be shifted (integer).
    :param mode: Determines whether to 'encode' (default) or 'decode' the message.
    :return: The transformed (encoded or decoded) message.
    """

    # Storing all lowercase letters in a variable for reference
    alphabet = string.ascii_lowercase  
    
    # If the mode is 'decode', we reverse the shift direction
    if mode == 'decode':
        shift = -shift  
    
    # Initializing an empty string to store the resulting message
    result = ""

    # Iterating through each character in the input text
    for char in text:
        # Checking if the character is a letter in the alphabet (ignoring punctuation, numbers, spaces)
        if char.lower() in alphabet:
            is_upper = char.isupper()  # Checking if the original character is uppercase

            # Finding the new index by shifting and ensuring it wraps around using modulo
            new_index = (alphabet.index(char.lower()) + shift) % 26
            new_char = alphabet[new_index]  # Getting the new shifted letter
            
            # Preserving the original case of the letter
            result += new_char.upper() if is_upper else new_char
        else:
            result += char  # Keeping non-alphabetic characters unchanged
    
    # Returning the final transformed message
    return result


def get_valid_shift():
    """
    Function to get a valid shift number from the user.
    
    Ensures that the input is an integer and prompts the user again if the input is invalid.
    
    :return: A valid integer representing the shift amount.
    """
    while True:  # Infinite loop to keep asking until a valid input is received
        try:
            # Prompting the user for input and converting it to an integer
            shift = int(input("Enter the shift number: "))
            return shift  # Return the valid shift value if successful
        except ValueError:
            # Handle cases where the input cannot be converted to an integer
            print("Invalid input! Please enter a valid integer.")

def handle_input(prompt):
    """
    Function to safely handle user input.
    
    This function is designed to handle standard input operations and also account 
    for environments where standard input may be restricted (such as certain sandboxes).
    
    :param prompt: The message to display when asking for input.
    :return: The user's input as a string, or "3" if an error occurs.
    """
    try:
        return input(prompt)  # Attempt to get user input
    except OSError:
        # Handles cases where input cannot be received (e.g., sandbox restrictions)
        return "3"  # Defaulting to "3" (exit option) to prevent program crash


def main():
    """
    Main function to run the Secret Code Generator program.
    
    Provides a user menu to choose between encoding, decoding, or exiting.
    Uses a loop to keep running until the user chooses to exit.
    """
    while True:  # Infinite loop to keep the program running until the user exits
        print("\nSecret Code Generator")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")

        # Handling user input to choose an option
        choice = handle_input("Choose an option (1/2/3): ")

        if choice == '1':  # User chooses to encode a message
            message = handle_input("Enter the message to encode: ")
            shift = get_valid_shift()
            print("Encoded Message:", caesar_cipher(message, shift, 'encode'))
        
        elif choice == '2':  # User chooses to decode a message
            message = handle_input("Enter the message to decode: ")
            shift = get_valid_shift()
            print("Decoded Message:", caesar_cipher(message, shift, 'decode'))
        
        elif choice == '3':  # User chooses to exit the program
            print("Exiting the program. Goodbye!")
            break  # Exits the loop, terminating the program
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")  # Handles invalid input

if __name__ == "__main__":
    main()
