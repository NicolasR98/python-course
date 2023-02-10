"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
but returns the greater if one or both numbers are odd
"""
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min([a,b])
    else:
        return max([a,b])

print('lesser_of_two_evens(2,4)', lesser_of_two_evens(2,4)) # 2
print('lesser_of_two_evens(2,5)', lesser_of_two_evens(2,5)) # 5

"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
"""

def animal_crackers(text):
    list_of_words = text.split(' ')
    return list_of_words[0][0] == list_of_words[1][0]

print("animal_crackers('Levelheaded Llama')", animal_crackers('Levelheaded Llama')) # True
print("animal_crackers('Crazy Kangaroo')", animal_crackers('Crazy Kangaroo'))       # False

"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
If not, return False
"""

def makes_twenty(n1,n2):
    num_list = [n1, n2]
    if 20 in num_list: return True
    else: return sum(num_list) == 20

print('makes_twenty(20, 10)', makes_twenty(20, 10)) # True
print('makes_twenty(12, 8)', makes_twenty(12, 8))  # True
print('makes_twenty(2, 3)', makes_twenty(2, 3))   # False

"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""

def old_macdonald(name):
    text_list = list(name)
    text_list[0] = text_list[0].upper()
    text_list[3] = text_list[3].upper()

    return ''.join(text_list)

print("old_macdonald('macdonald')", old_macdonald('macdonald'))   # MacDonald

"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
"""

def master_yoda(text):
    list_of_words = text.split(' ')
    list_of_words.reverse()

    return ' '.join(list_of_words)

print("master_yoda('I am home')", master_yoda('I am home'))     # home am I
print("master_yoda('We are ready')", master_yoda('We are ready'))  # ready are We

"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
"""

def almost_there(num):
    return (90 <= num <=110) or (190 <= num <= 210)

print('almost_there(90)', almost_there(90))    # True
print('almost_there(104)', almost_there(104))   # True
print('almost_there(150)', almost_there(150))   # False
print('almost_there(209)', almost_there(209))   # True

"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""

def has_33(nums):
    for index in range(len(nums)):
        if nums[index:index + 2] == [3,3]:
            return True
    return False

            

print('has_33([1, 3, 3])', has_33([1, 3, 3]))           # True
print('has_33([1, 3, 1, 3])', has_33([1, 3, 1, 3]))     # False
print('has_33([3, 1, 3])', has_33([3, 1, 3]))           # False

"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
"""

def paper_doll(text):
    return ''.join([letter * 3 for letter in text])


print("paper_doll('Hello')", paper_doll('Hello'))
print("paper_doll('Mississippi')", paper_doll('Mississippi'))

"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
"""

def blackjack(a,b,c):
    given_nums = [a,b,c]
    given_nums_sum = sum([a,b,c])
    
    if 11 in given_nums: given_nums_sum -= 10
    if given_nums_sum > 21: return 'BUST'
    
    return given_nums_sum

print('blackjack(5,6,7)', blackjack(5,6,7))
print('blackjack(9,9,9)', blackjack(9,9,9))
print('blackjack(9,9,11)', blackjack(9,9,11))

"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 
(every 6 will be followed by at least one 9). Return 0 for no numbers.
"""

def summer_69(nums):
    checkIfContinue = False
    result = []

    for num in nums:
        if num == 9:
            checkIfContinue = False
            continue
        elif num == 6:
            checkIfContinue = True
            continue
        elif checkIfContinue == True: continue

        result.append(num)
    
    return sum(result)

print("summer_69([1, 3, 5])", summer_69([1, 3, 5]))
print("summer_69([4, 5, 6, 7, 8, 9])", summer_69([4, 5, 6, 7, 8, 9]))
print("summer_69([2, 1, 6, 9, 11])", summer_69([2, 1, 6, 9, 11]))

"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
"""

def spy_game(nums):
    result = []
    expected = [0,0,7]
    for num in nums:
        if num in [0,7]: 
            result.append(num)
            if result == [0,0,7]: return True
    return result == expected

print('spy_game([1,2,4,0,0,7,5])', spy_game([1,2,4,0,0,7,5]))
print('spy_game([1,0,2,4,0,5,7])', spy_game([1,0,2,4,0,5,7]))
print('spy_game([1,7,2,0,4,5,0])', spy_game([1,7,2,0,4,5,0]))

