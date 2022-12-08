#Noah Tanner
#Chapter 1 Challenge Problems
#December 2022

#Palindrome word detector, modified to detect space, punctuation, and mixed capitalization

import re 

def palindrome_method_two(word):
    #make a copy of original word
    copy = word

    #lower case the word
    word = word.lower()
    
    #strip punctuation
    word = re.sub('[,. !]', '', word)

    if word[::1] == word:
        print("{} is a palindrome".format(copy))
    if word[::1] != word:
        print("{} is NOT a palindrome".format(copy))

#Tests
print('Test 1:')
word = "A man, a plan, a canal. panama!"
results_1 = palindrome_method_two(word)

