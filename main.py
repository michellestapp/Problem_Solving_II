# Task 1: Reverse a String
# (HINT: Review the Algorithms + Problem Solving Lecture!)
# Write code that takes a string as input and returns the string reversed
# i.e. “Hello” will be returned as “olleH”

def reverse_a_word():
    reversed_word = ''
    word = input(" Enter a word to be reversed: ")

    num_index = len(word) - 1

    for index in range(num_index, -1, -1):
        reversed_word += word[index]

    print(reversed_word)
    

reverse_a_word()
