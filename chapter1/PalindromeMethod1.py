#Noah Tanner
#Chapter 1 Challenge Problems
#November 2022

#Palindrome Word Detector, slice method

def slice_palindrome(n):
    if n[::-1] == n:
        print('{} is a palindrome'.format(n))
    else: 
        print('{} is not a palindrome'.format(n))

#Test
print('first test:')
n = 'madam'
results_1 = slice_palindrome(n)
print(results_1)

print('second test:')
n = 'tacocat'
results_2 = slice_palindrome(n)
print(results_2)

print('third test:')
n = 'venezuela'
results_3 = slice_palindrome(n)
print(results_3)