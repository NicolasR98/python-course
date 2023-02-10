"""
First assesment

Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
"""

st = 'Print only the words that start with s in this sentence'
st_list = st.split(' ')

for word in st_list:
    if word[0] == 's':
        print(word)

"""
Second assesment

Use range() to print all the even numbers from 0 to 10.
"""

even_nums = [num for num in range(0,11) if num % 2 == 0]
even_nums2 = list(range(0,11,2))

print(even_nums, even_nums2)
for num in even_nums: print(num)

"""
Third assesment

Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
"""

nums_dividible_by_three = [num for num in range(1,51) if num % 3 == 0]

print(nums_dividible_by_three)

"""
Fourth assesment

Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
"""

st = 'Print every word in this sentence that has an even number of letters'
st_word_list = st.split(' ')
for word in st_word_list:
    if (len(word) % 2 == 0): 
        print(f'EVEN! {word}')

"""
Fifth assesment

Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" 
instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples 
of both three and five print "FizzBuzz".
"""

for num in range(1,101):
    if num % 3 == 0  and num % 5 == 0: 
        print(f'FizzBuzz - {num}')
        continue
    elif num % 3 == 0: 
        print(f'Fizz - {num}')
    elif num % 5 == 0: 
        print(f'Buzz - {num}')
    else: print(num)

"""
Fifth assesment

Use List Comprehension to create a list of the first letters of every word in the string below:
"""
st = 'Create a list of the first letters of every word in this string'

list_of_firsts_letters = [word[0] for word in st.split(' ')]

print(list_of_firsts_letters)
