from functools import reduce

numbers = [5, 12, 7, 20, 3, 18, 2, 15, 9, 30, 11, 6]


def greater_than_ten(nums):
    for num in nums:
        if num > 10:
            yield num


def square_numbers(nums):
    for num in nums:
        yield num**2

step1 = greater_than_ten(numbers)
step2 = square_numbers(step1)

step3 = list(filter(lambda x: x%2==0, step2))

step4 = map(lambda x: f'value = {x}', step3)

# print(list(step4))

sum_numbers_step5 = reduce(lambda x,y: x + y, step3)
max_number_step5b = reduce(lambda x,y: x if x>y else y, step3)

def multiples_of_three(n):
    count = 0
    num = 3
    while count < n:
        yield num
        num += 3
        count += 1

print(list(multiples_of_three(10)))



def word_generator(text):
    for word in text.split():
        yield word

text1 = 'hello bye what do you want skdrjgffqf'
print(list(text1))

result = map(
    lambda x: x.upper(),
    filter(lambda x: len(x) > 4, text1.split()))

print(list(result))

