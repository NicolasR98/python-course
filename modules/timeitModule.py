import timeit

def func_one(n: int):
    return [str(num) for num in range(n)]

def func_two(n: int):
    return list(map(str, range(n)))

statement_1 = 'func_one(1000)'
statement_2 = 'func_two(1000)'

setup_1 = """
def func_one(n: int):
    return [str(num) for num in range(n)]
"""
setup_2 = """
def func_two(n: int):
    return list(map(str, range(n)))
"""

result_1 = timeit.timeit(stmt=statement_1, setup=setup_1, number=10000)
result_2 = timeit.timeit(stmt=statement_2, setup=setup_2, number=10000)

print(f'Result 1: {result_1}s')
print(f'Result 2: {result_2}s')