"""
Write a function that computes the volume of a sphere given its radius.
"""
from math import pi

def vol(rad): 
    return (4 * pi * rad ** 3) / 3

print(vol(2))

"""
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""

def ran_check(num, low, high):
    return low <= num <= high

print(ran_check(5,2,7))
print(ran_check(8,2,7))
print(ran_check(1,2,7))

"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output : 
    No. of Upper case characters : 4
    No. of Lower case Characters : 33

"""
text = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(text):
    lower = 0
    upper = 0

    for letter in text:
        if not letter.isalpha():
            continue
        if letter.isupper():
            upper += 1
        else:
            lower += 1
    return f'No. of Upper case characters : {upper}\nNo. of Lower case Characters : {lower}'


print(up_low(text))

"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""

def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

"""
Write a Python function to multiply all the numbers in a list.
"""

def multiply(nums):
    result = 1
    for num in nums:
        result = result * num

    return result

print(multiply([1,2,3,-4]))

"""
Write a Python function that checks whether a word or phrase is palindrome or not.
"""

def palindrome(text):
    normalized_text = text.replace('', '')

    print(normalized_text)
    return normalized_text == normalized_text[::-1]

print(palindrome('madam'))
print(palindrome('racecar'))
print(palindrome('nurses run'))
print(palindrome('helleh'))

"""
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
"""
import re
import string

def isPanagram(str1, alphabet = string.ascii_lowercase):
    normalized_chars = re.sub('\W', '', str1)
    unique_chars = set(normalized_chars.lower())
    sorted_chars = sorted(unique_chars)

    return sorted(alphabet) == sorted_chars

print(isPanagram('The quick brown fox jumps over the lazy dog'))
print(isPanagram('Jackdaws love my big sphinx of quartz...'))
print(isPanagram('Grumpy wizards make toxic brew for the evil queen and Jack!.'))
print(isPanagram('This is not a panagram!!!!'))