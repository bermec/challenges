''' Fine control, iter'''
import sys

iterable = ['Spring', 'summer', 'Autumn', 'Winter']
iterator = iter(iterable)
print(next(iterator))

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError('iterable is empty')

print(first(['1st', '2nd', '3rd']))
print(first(set()))


