bar = 'Hello_World'

# If I want to get all the chars from an index
print(bar[5:]) # _World

## If I want to get all the chars until certain index (not included)
print(bar[:5])  # Hello

## If I want to get between indexes
print(bar[4:7])  # o_W

## All the str
print(bar[::])  # Hello_World

## By steps
print(bar[::2])  # HloWrd

## Reverse str
print(bar[::-1])  # dlroW_olleH

## Split str by 'x'
print(bar.split('_'))