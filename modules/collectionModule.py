from collections import Counter, defaultdict, namedtuple

# Counter
repeated_nums = [1,1,1,1,1,2,2,2,2,2,3,3,4,4,4,5,5]
repeated_letters = 'aaaaaaaaaabbbbbbbbbbbccccccccccccdddde'
sentence = 'This is a sentence made by many many words'
sentence_splitted = sentence.lower().split(' ')

most_common_repeated_nums = Counter(repeated_nums).most_common()
three_most_common_repeated_letters = Counter(repeated_letters).most_common(3)

print(Counter(repeated_nums))
print(Counter(repeated_letters))
print(Counter(sentence_splitted))
print(most_common_repeated_nums)
print(three_most_common_repeated_letters)

# defaultdict
my_dict = defaultdict(lambda: 0)
my_dict['a'] = 1

print(my_dict['a'])
print(my_dict['unixestant_key'])

# namedtuple
Dog = namedtuple('Dog', ['name', 'breed', 'age'])
linda = Dog(name='Linda', breed='dog type', age=1.5)
print(linda, linda.name, linda[1])