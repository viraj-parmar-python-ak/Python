# def my_generator():
#     for i in range(10):
#         yield i

# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for i in range(9):
#     print(next(gen))





# using multiple generators to find odd adn even numbers
def numbers_generator(n):
    for i in range(n):
        yield i

def filter_evens(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

def filter_odds(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

even_numbers = filter_evens(numbers_generator(10))
odd_numbers = filter_odds(numbers_generator(10))

print("Even numbers:")
for even_num in even_numbers:
    print(even_num)

print("Odd numbers:")
for odd_num in odd_numbers:
    print(odd_num)
