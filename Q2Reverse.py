def reverse_word():
    # Accept user input
    word = input("Enter a word: ")

    # Loop through the word in reverse order and print each letter
    for letter in reversed(word):
        print(letter)

# Call the function
reverse_word()