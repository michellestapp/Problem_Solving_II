# Task 1: Reverse a String
# (HINT: Review the Algorithms + Problem Solving Lecture!)
# Write code that takes a string as input and returns the string reversed
# i.e. “Hello” will be returned as “olleH”

# def reverse_a_word():
#     reversed_word = ''
#     word = input(" Enter a word to be reversed: ")

#     num_index = len(word) - 1

#     for index in range(num_index, -1, -1):
#         reversed_word += word[index]

#     print(reversed_word)
    

#reverse_a_word()

# Task 2: Capitalize a Letter

# Write code that takes a string as input and capitalize the first letter of each word.
#  Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

def cap_first_letter():
    completed_sentence = ''
    sentence = input(" Enter a sentence string with no capitals:  ")

    words_in_sentence = sentence.split()
    for word in words_in_sentence:
       
       completed_sentence += (word.capitalize() + ' ')
       
    print(completed_sentence)


cap_first_letter()
