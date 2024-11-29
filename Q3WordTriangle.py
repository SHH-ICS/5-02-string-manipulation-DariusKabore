def word_triangle():
    word = input("Enter word ")
    for i in range(1, len(word) + 1):
        print(word[:i])

word_triangle()