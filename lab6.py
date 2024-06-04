
from functools import reduce


def task1(numbers):
    return sum(numbers)


def task2(data):
    return len(data)


def task3(numbers):
    return sorted(numbers, reverse=True)[0]


def task4(data):
    return data[0]["name"]


def task5(data):
    return sorted(data, key=lambda x: len(x[0]))[-1][-1]


def task6(lists):
    return reduce(lambda x, y: x * y, [num for sublist in lists for num in sublist if num % 2 == 0])


def task7(tuples):
    return sum([t[1] for t in tuples])
