# # Task 1: Reverse a String
# # (HINT: Review the Algorithms + Problem Solving Lecture!)
# # Write code that takes a string as input and returns the string reversed
# # i.e. “Hello” will be returned as “olleH”

# def reverse_a_word():
#     reversed_word = ''
#     word = input(" Enter a word to be reversed: ")

#     num_index = len(word) - 1

#     for index in range(num_index, -1, -1):
#         reversed_word += word[index]

#     print(reversed_word)
    

# reverse_a_word()

# # Task 2: Capitalize a Letter

# # Write code that takes a string as input and capitalize the first letter of each word.
# #  Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

# def cap_first_letter():
#     completed_sentence = ''
#     sentence = input(" Enter a sentence string with no capitals:  ")

#     words_in_sentence = sentence.split()
#     for word in words_in_sentence:
       
#        completed_sentence += word.capitalize() + ' '

#     print(completed_sentence)


# cap_first_letter()


# Task 3: Palindrome
# A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	


# Write code that takes a user input and checks to see if it is a Palindrome and reports the result

# def palindrome_one():
#     is_palindrome = 'True'
#     word = input(" Enter a word to be checked as a palindrome: ")

#     index = len(word) - 1

#     index_one = 0
#     index_two = index

#     while index_one in range(index):
        
#         if word[index_one] == word[index_two]:
#             index_one += 1
#             index_two -= 1          
#             is_palindrome = 'True'
#         else:
#             is_palindrome = 'False'
#             break
    
#     if is_palindrome == 'True':
#         print(f"  {word} is a palindrome! ")
#     else:
#         print(f"  {word} is not a palindrome")
#     print(word)


# palindrome_one()

# def palindrome_two():
#     reversed_word = ''
#     word = input(" Enter a word to verify if it is a palindrome: ")

#     num_index = len(word) - 1

#     for index in range(num_index, -1, -1):
#         reversed_word += word[index]

#     if word == reversed_word:
#         print(f"  {word} is a palindrome! ")
#     else:
#         print(f"  {word} is not a palindrome")

# palindrome_two()

# Task 4 : Compress a string of characters
# For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

def compress_string():
    my_string = input(" Enter a string of letters: ")
    new_string = ''

    num_index = len(my_string) - 1
    num_repeats = 1
    compare_index = 1
    index = 0


    while index < num_index:
        while my_string[index] == my_string[compare_index]:
            num_repeats += 1
            compare_index += 1
            if compare_index > num_index:
                break
        new_string += (str(num_repeats) + my_string[index])

       
        num_repeats = 1
        index = compare_index
        compare_index = index + 1
       

    print(new_string)    



compress_string()