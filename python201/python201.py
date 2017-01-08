## Contents:
##
## argparse
## collections (replacements for tuple, list, dict)
## contextlib (Context Mangers)
## functools (Partials, function overloading, caching)
## importlib (Importing)
## iterators and generators
## itertools (Create your own iterators)
## re (Regex)
## typing (Type Hinting)
## map/filter
## Unicode, encoding/decoding strings
## benchmarking
## websites/scraping web data
## Python APIs
## client/server, FTP
## doctest/unittest/mock
## tox/nose/pytest

# import argparse
#
# def get_args():
#     """"""
#     parser = argparse.ArgumentParser(
#         description='A simple argument parser',
#         epilog='This is where you might put example usage'
#     )
#     return parser.parse_args()
#
# if __name__ == '__main__':
#     get_args()
# # python python201.py -h

# # getting args
# import argparse
#
# def get_args():
#     """"""
#     parser = argparse.ArgumentParser(
#         description='A simple argument parser',
#         epilog='This is where you might put example usage'
#     )
#
#     # required argument
#     parser.add_argument('-x', action='store', required=True,
#         help='Help text for option X')
#
#     # optional arguments
#     parser.add_argument('-y', help='Help text for option Y', default=False)
#     parser.add_argument('-z', help='Help text for option Z', type=int)
#     # the key for this arg is 'execute', not 'a'
#     parser.add_argument('-a', '--execute', action='store',
#         help='For executing order 66')
#
#     print(parser.parse_args())
#
# if __name__ == '__main__':
#     get_args()

# # mutually exclusive args
# import argparse
#
# def get_args():
#     """"""
#     parser = argparse.ArgumentParser(
#         description='A simple argument parser',
#         epilog = 'This is where oyu might put exmple usage'
#     )
#
#     # x and y can't run at the same time
#     group = parser.add_mutually_exclusive_group()
#     group.add_argument('-x', '--execute', action='store',
#         help='Help text for option X')
#     group.add_argument('-y', help='Help text for option Y', default=False)
#
#     parser.add_argument('-z', help='Help text for option Z', type=int)
#
#     print(parser.parse_args())
#
# if __name__ == '__main__':
#     get_args()

# # collections
# # A ChainMap groups multiple dicts or other mappings
# # together to create a single, updateable view.
# import argparse
# import os
#
# from collections import ChainMap
#
# def main():
#     app_defaults = {'username':'admin', 'password':'admin'}
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-u', '--username')
#     parser.add_argument('-p', '--password')
#     args = parser.parse_args()
#     # argparse can't get a dictionary object of it's arguments, so use a dict comprehension
#     # vars(variable) gets variable.__dict__
#     # locals() == a dictionary of the variables in the current scope
#     # vars() behaves like locals()
#     command_line_arguments = {key:value for key, value in vars(args).items() if value}
#
#     # The ChainMap  goes through each map, and returns the first value it finds
#     # So CLI's will override os.environ's will override app_defaults
#     chain = ChainMap(command_line_arguments, os.environ, app_defaults)
#
#     print(chain['username'])
#
# if __name__ == '__main__':
#     main()
#     os.environ['username'] = 'test'
#     main()

# # Counter
# # Counter is a subclass of python's dict.
# >>> counter = Counter('superfluous')
# >>> counter
# Counter({'u': 3, 's': 2, 'e': 1, 'r': 1, 'p': 1, 'l': 1, 'o': 1, 'f': 1})
# >>> counter['u']
# 3

# # defaultdict
# # a defaultdict will "default" a value if that key has not been set yet.
# # also a subclass of python's dict. Accepts a default_factory as its primary arg.
# # usually a Python type, like int or list.
# # regular python Dict which counts words:
# sentence = 'The red fox jumped over the fence and ran to the zoo for food'
# words = sentence.split(' ')
#
# reg_dict = {}
# for word in words:
#     if word in reg_dict:
#         reg_dict[word] += 1
#     else:
#         reg_dict[word] = 1
#
# print(reg_dict)
#
# # not with defaultdict
# from collections import defaultdict
#
# sentence = 'The red fox jumped over the fence and ran to the zoo for food'
# words = sentence.split(' ')
#
# d = defaultdict(int)
# for word in words:
#     # automatically assigns 0 as the value for any new key
#     d[word] += 1
#
# print(d)

# # group payments by account number
# from collections import defaultdict
#
# my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
#     (345, 222.66), (678, 300.25), (1234, 35.67)]
#
# reg_dict = {}
# for acct_num, value in my_list:
#     if acct_num in reg_dict:
#         reg_dict[acct_num].append(value)
#     else:
#         reg_dict[acct_num] = [value]
#
# print(reg_dict)
#
# my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
#     (345, 222.66), (678, 300.25), (1234, 35.67)]
#
# d = defaultdict(list)
# for acct_num, value in my_list:
#     d[acct_num].append(value)
#
# print(d)

# # deque ('deck') == double-ended queue
# # supports memory efficient appends and pops from either side
# # if you need fast appends and pops, use a deque. if you need fast random access,
# # use a list.
# from collections import deque
#
# def get_last(filename, n=5):
#     """
#     Returns the last n lines from the file
#     """
#     try:
#         with open(filename) as f:
#             # bound deque to n lines, so when new lines are added,
#             # old ones are popped off.
#             return deque(f, n)
#     except OSError:
#         print('Error opening file: {}'.format(filename))
#         raise

# # namedtuple: something like a struct (groups a list of variables under one name)
# from collections import namedtuple
#
# # a subclass of a tuple, but with named fields
# Parts = namedtuple('Parts', 'id_num desc cost amount')
# auto_parts = Parts(id_num='1234', desc='Ford Engine',
#     cost=1200.00, amount=10)
# print(auto_parts.id_num)

# OrderedDict: a dict, but ordered!

# # context managers let you set something up and tear it down automatically
# # they work using __enter__ and __exit__
# import sqlite3
#
# class DataConn:
#     """"""
#
#     def __init__(self, db_name):
#         """Constructor"""
#         self.db_name = db_name
#
#     def __enter__(self):
#         """
#         Open the db connection
#         """
#         self.conn = sqlite3.connect(self.db_name)
#         return self.conn
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """
#         Close the connection
#         """
#         self.conn.close()
#         if exc_val:
#             raise
#
# if __name__ == '__main__':
#     db = 'test.db'
#     with DataConn(db) as conn:
#         cursor = conn.cursor()

# from contextlib import contextmanager
#
# # decorate file_open, letting us do 'with file_open'
# @contextmanager
# def file_open(path):
#     try:
#         f_obj = open(path, 'w') # 2. create the file obj
#         yield f_obj # 3. pause here 5. resume here
#     except OSError:
#         print('We had an error!')
#     finally:
#         print('Closing file')
#         f_obj.close() # 6. finish execution here
#
# if __name__ == '__main__':
#     with file_open('test.txt') as fobj: # 1. call the file object creation
#         fobj.write('Testing context managers') # 4. write something

# from contextlib import contextmanager
#
# @contextmanager
# def closing(db):
#     try:
#         yield db.conn()
#     finally:
#         db.close()

# # functools act on or return other functions
# import urllib.error
# import urllib.request
#
# from functools import lru_cache # adds caching to the function it decorates
#
# @lru_cache(maxsize=24)
# def get_webpage(module):
#     """
#     Gets the specified Python module web page
#     """
#     webpage = 'https://docs.python.org/3/library/{}.html'.format(module)
#
#     try:
#         with urllib.request.urlopen(webpage) as request:
#             return request.read()
#     except urllib.error.HTTPError:
#         return None
#
# # running this multiple times will speed up the results, as they are cached
# if __name__ == '__main__':
#     modules = ['functools', 'collection', 'os', 'sys']
#     for module in modules:
#         page = get_webpage(module)
#         if page:
#             print('{} module page found'.format(module))

# # functool.partial
# import wx # doesn't play nice with anaconda
#
# from functools import partial
#
# class MainFrame(wx.Frame):
#     """
#     This app shows a group of buttons
#     """
#
#     def __init__(self, *args, **kwargs):
#         """Constructor"""
#         super(Mainframe, self).__init__(parent=None, title='Partial')
#         panel = wx.Panel(self)
#
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         btn_labels = ['one', 'two', 'three']
#         for label in btn_labels:
#             btn = wx.Button(panel, label=label)
#             btn.Bind(wx.EVT_BUTTON, partial(self.onButton, label=label))
#             sizer.Add(btn, 0, wx.ALL, 5)
#
#         panel.SetSizer(sizer)
#         self.Show()
#
#     def onButton(self, event, label):
#         """
#         Event handler called when a button is pressed
#         """
#         print('You pressed: ' + str(label))
#
# if __name__ == '__main__':
#     app = wx.App(False)
#     frame = MainFrame()
#     app.MainLoop()

# from functools import partial
#
# def add(x, y):
#     """"""
#     return x + y
# def multiply(x, y):
#     """"""
#     return x * y
# def run(func):
#     """"""
#     print(func())
# def main():
#     """"""
#     a1 = partial(add, 1, 2)
#     m1 = partial(multiply, 5, 8)
#     run(a1)
#     run(m1)
#
# if __name__ == "__main__":
#     main()

# from functools import singledispatch
#
# @singledispatch # this function dispatches to the other functions, depending on type
# def add(a, b):
#     raise NotImplementedError('Unsupported type')
#
# @add.register(int)
# def _(a, b):
#     print('First arg is or type ', type(a))
#     print(a + b)
#
# @add.register(str)
# def _(a, b):
#     print('First arg is of type ', type(a))
#     print(a + b)
#
# @add.register(list)
# def _(a, b):
#     print('First arg is of type', type(a))
#     print(a + b)
#
# if __name__ == '__main__':
#     add(1, 2)
#     add('Python', 'Programming')
#     add([1,2,3], [5,6,7])

# from functools import singledispatch
# from decimal import Decimal
#
# @singledispatch
# def add(a, b):
#     raise NotImplementedError('Unsupported type')
#
# # stacking these decorators means this function handles both floats and Decimals
# @add.register(float)
# @add.register(Decimal)
# def _(a,b):
#     print('First arg is of type ', type(a))
#     print(a + b)
#
# if __name__ == '__main__':
#     add(1.23, 5.5)
#     add(Decimal(10.5), Decimal(10.789))

# def another_function(func):
#     """
#     A function that accepts another function
#     """
#
#     def wrapper():
#         """
#         A wrapping function
#         """
#         val = 'The result of %s is %s' % (func(), eval(func()))
#
#         return val
#
#     return wrapper
#
# @another_function
# def a_function():
#     """
#     A pretty useless function
#     """
#     return '1 + 1'
#
# if __name__ == '__main__':
#     # the decorating function overwrites the original function
#     print(a_function.__name__)
#     print(a_function.__doc__)

# from functools import wraps
#
# def another_function(func):
#     """
#     A function that accepts another function
#     """
#
#     @wraps(func)
#     def wrapper():
#         """
#         A wrapping function
#         """
#         val = 'The result of %s is %s' % (func(), eval(func()))
#
#         return val
#
#     return wrapper
#
# @another_function
# def a_function():
#     """
#     A pretty useless function"""
#     return '1 + 1'
#
# if __name__ == '__main__':
#     # the decorating function does NOT overwrite the original function
#     print(a_function.__name__)
#     print(a_function.__doc__)

# # optional imports
# try:
#     # For Python 3
#     from http.client import responses
# except ImportError: # For Python 2.5-2.7
#     try:
#         from httplib import responses # NOQA
#     except ImportError: # For Python 2.4
#         from BaseHTTPServer import BaseHTTPRequestHandler as _BHRH
#         responses = dict([(k, v[0]) for k, v in _BHRH.responses.items()])

# # importing into a local scope
# # pretty much never used, can save time if importing a big module into
# # a rarely-used function
# import sys # global scope
#
# def square_root(a):
#     # This import is only in the local scope
#     import math
#     return math.sqrt(a)
#
# def my_pow(base_num, power):
#     # this will fail
#     return math.pow(base_num, power)
#
# if __name__ == '__main__':
#     print(square_root(49))
#     print(my_pow(2, 3))

# # dynamic imports, importing a module when you have it as a string
# import importlib
#
# def dynamic_import(module):
#     return importlib.import_module(module)
#
# if __name__ == '__main__':
#     module = dynamic_import('foo')
#     module.main()
#
#     module_two = dynamic_import('bar')
#     module_two.main()

# # creating an iterator (has __iter__ and __next__)
# class MyIterator:
#
#     def __init__(self, letters):
#         """
#         Constructor
#         """
#         self.letters = letters
#         self.position = 0
#
#     def __iter__(self):
#         """
#         Returns itself as an iterator
#         """
#         return self
#
#     def __next__(self):
#         """
#         Returns the next letter in the sequence or raises StopIteration
#         """
#         if self.position >= len(self.letters):
#             raise StopIteration
#         letter = self.letters[self.position]
#         self.position += 1
#         return letter
#
# if __name__ == '__main__':
#     i = MyIterator('abcd')
#     for item in i:
#         print(item)

# # an infinite iterator
# class Doubler:
#     """
#     An infinite iterator which prints square numbers
#     """
#
#     def __init__(self):
#         """
#         Constructor
#         """
#         self.number = 0
#
#     def __iter__(self):
#         """
#         Returns itself as an iterator
#         """
#         return self
#
#     def __next__(self):
#         """
#         Doubles the number each time next is called and returns it.
#         """
#         self.number += 1
#         return self.number * self.number
#
# if __name__ == '__main__':
#     doubler = Doubler()
#     count = 0
#
#     # This will run infinitely without the 'break'
#     for number in doubler:
#         print(number)
#         # if count > 5:
#         #     break
#         # count += 1

# # generators
# # a function that saves its state after each 'yield'
# # does not create whole list in memory, but on demand.
# # a generator is really a type of iterator, because you can call __next__ on it
# def doubler_generator():
#     number = 2
#     while True:
#         yield number
#         number *= number
#
# if __name__ == '__main__':
#     doubler = doubler_generator()
#     print(next(doubler))
#     print(next(doubler))
#     print(next(doubler))
#     print(type(doubler))

# # itertools
# from itertools import count
# for i in count(10): # start counting at 10
#     if i > 20:
#         break
#     else:
#         print(i)
#
# from itertools import islice
# for i in islice(count(10), 5): # stop after 5 iterations
#     print(i)
#
# from itertools import cycle # cycle through stuff indefinitely
# count = 0
# for item in cycle('abc'):
#     if count > 7:
#         break
#     print(item)
#     count += 1

# from itertools import accumulate
#
# print(list(accumulate(range(10)))) # sums of 1 to 10
#
# import operator
#
# print(list(accumulate(range(1, 5), operator.mul))) # 1 to 4 factorial

# # flattening lists into one list
# from itertools import chain
#
# list_1 = [1,2,3]
# list_2 = [4, 5, 6]
#
# my_list = list(chain(list_1, list_2)) # faster than list_1 + list_2?
# print(my_list)
#
# my_list = list(chain.from_iterable([list_1, list_2])) # same thing but passing
#     # args as a list
# print(my_list)

# # create multiple iterators
# from itertools import tee
# data = 'abcde'
# iter1, iter2 = tee(data)
# for item in iter1:
#     print(item)
# for item in iter2:
#     print(item)

# # zip up two iterables into a list of tuples
# # if the iterables passed may be infinite, wrap the function with islice
# # to limite the number of calls.
# from itertools import zip_longest
# for item in zip_longest('abcd', 'xy', fillvalue='BLANK'):
#     print(item)

# # create a list of tuple combinations
# from itertools import combinations
# print(list(combinations('abcd', 2)))
#
# from itertools import combinations_with_replacement
# print(list(combinations_with_replacement('wxyz', 2)))

# # create cartesian product
# from itertools import product
# arrays = [(0, 1), (2, 3), (4, 5)]
# cp = list(product(*arrays))
# print(cp)

# # permutations
# from itertools import permutations
# print(list(permutations('abcd', 2)))

# # regex
# import re
#
# text = 'abcdfghijk'
# parser = re.search('a[b-f]*f', text)
# print(parser)
# print(parser.group())

# import re
#
# text = 'The ants go marching one by one'
#
# strings = ['the', 'one']
#
# for string in strings:
#     match = re.search(string, text)
#     if match:
#         print('Found "{}" in "{}"'.format(string, text))
#         text_pos = match.span()
#         print(text_pos)
#         print(text[match.start():match.end()])
#     else:
#         print('Did not find "{}"'.format(string))

# import re
# silly_string = 'the cat in the hat'
# pattern = 'the'
# print(re.findall(pattern, silly_string))
#
# for match in re.finditer(pattern, silly_string):
#     s = "Found '{group}' at {begin}:{end}".format(
#         group=match.group(), begin=match.start(),
#         end=match.end())
#     print(s)

# # type hinting - declaring function arguments and returned objects
# # to have a certain type.
# # This is not binding
# def some_function(number:int, name:str) -> None: # expects an int and a string, and is expected to return None
#     print('%s entered %s' % (name, number))

# # no type hinting
# def process_data(my_list, name):
#     if name in my_list:
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     my_list = ['Mike', 'Nick', 'Toby']
#     print(process_data(my_list, 'Mike'))
#     print(process_data(my_list, 'John'))

# # type hinting
# def process_data(my_list: list, name:str) -> bool:
#     return name in my_list
#
# if __name__ == '__main__':
#     my_list = ['Mike', 'Nick', 'Toby']
#     print(process_data(my_list, 'Mike'))
#     print(process_data(my_list, 'John'))

# # type hints can be built-in classes, abstract base classes, user defined classes, and types in the 'types' module
# # create our own class and add a hint
# class Fruit:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
# def salad(fruit_one: Fruit, fruit_two: Fruit) -> list:
#     print(fruit_one.name)
#     print(fruit_two.name)
#     return [fruit_one, fruit_two]
#
# if __name__ == '__main__':
#     f = Fruit('orange', 'orange')
#     f2 = Fruit('apple', 'red')
#     salad(f, f2)

# you can also create aliases of classes:
# Animal = str # Animal now stands for str
#
# def zoo(animal: Animal, number: int) -> None:
#     print('The zoo has {} {}'.format(number, animal))
#
# if __name__ == '__main__':
#     zoo('Zebras', 10)

# # type hinting in overloaded functions
# from functools import singledispatch
#
# @singledispatch
# def add(a, b):
#     raise NotImplementedError('Unsuppoted type')
#
# @add.register(int)
# def _(a:int, b:int) -> int:
#     print('First arg is of type ', type(a))
#     print(a + b)
#     return a + b
#
# @add.register(str)
# def _(a:str, b:str) -> str:
#     print('First arg is of type ', type(a))
#     print(a + b)
#     return a + b
#
# @add.register(list)
# def _(a:list, b:list) -> list:
#     print('First arg is of type ', type(a))
#     print(a + b)
#     return a + b
#
# if __name__ == '__main__':
#     add(1, 2)
#     add('1', '2')
#     add([1], [2])

# # "any" accepts an iterable and returns true if any elemnt in iterable is True
# print(any([0,0,0,1])) # True
# # "all" returns true if they're all true
# print(all([0,0,1])) # False
# print(all([1,1,1])) # True
# # testing whether a list of widgets are shown when they shouldnt be:
# widget_one = ''
# widget_two = ''
# widget_three = 'button'
# widgets_exist = any([widget_one, widget_two, widget_three])
# if widgets_exist:
#     raise Exception

# # enumerate shows the index position and the element
# my_string = 'abcdefg'
# for pos, letter in enumerate(my_string):
#     print(pos, letter)

# # eval takes a string and basically runs them
# var = 10
# source = 'var * 2'
# print(eval(source)) # 20

# # filter takes a function and an iterable and returns an iterator for those
# # elements within the iterable for which the passed in function returns True.
# def less_than_10(x):
#     return x < 10 # Returns True if x < 10, False otherwise
#
# my_list = [1, 2, 3, 10, 11, 12]
# filtered_iterable = filter(less_than_10, my_list) # Iterable with 1, 2, 3 in it
# for item in filtered_iterable:
#     print(item)
# # itertools also has "filterfalse", whic returns an iterable where the function
# # returns False

# # map takes a function and an iterable, and returns an iterator that applies
# # the function to each item in the iterable
#
# def doubler(x):
#     return x * 2
#
# my_list = [1, 2, 3, 4, 5]
# map_iterator = map(doubler, my_list) # Iterator holding 2, 4, 6, 8, 10 # also a generator
# for item in map_iterator:
#     print(item)

# # zip takes a series of iterables and returns an iterator of tuples
# keys = ['a', 'b', 'c']
# values = [5, 6, 7]
# zip_iterator = zip(keys, values)
# print(zip_iterator)
# # print(list(zip_iterator))
# print(dict(zip_iterator))

# # unicode
# string = 'abc' + chr(255)
# print(string)
# u = chr(40960) + 'abc' + chr(1972)
# print(u)
# print(u.encode('ascii', 'ignore'))
# print(u.encode('ascii', 'replace'))

# # benchmarking
# def my_function():
#     try:
#         1 / 0
#     except ZeroDivisionError:
#         pass
#
# if __name__ == '__main__':
#     import timeit
#     setup = 'from __main__ import my_function'
#     print(timeit.timeit('my_function()', setup=setup))

# # creating a function decorator for timing
# import random
# import time
#
# def timerfunc(func):
#     """
#     A timer decorator
#     """
#
#     def function_timer(*args, **kwargs):
#         """
#         A nested function for timing other functions
#         """
#         start = time.time()
#         value = func(*args, **kwargs) # runs the passed function
#         end = time.time()
#         runtime = end - start
#         msg = "The runtime for {func} took {time} seconds to complete"
#         print(msg.format(func=func.__name__, time=runtime))
#         return value
#
#     return function_timer
#
# @timerfunc
# def long_runner():
#     for x in range(5):
#         sleep_time = random.choice(range(1,5))
#         time.sleep(sleep_time)
#
# if __name__ == '__main__':
#     long_runner()

# # creating a timing "context manager class"
# import random
# import time
#
# class MyTimer():
#
#     def __init__(self):
#         self.start = time.time()
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         end = time.time()
#         runtime = end - self.start
#         msg = 'The function took {time} seconds to complete'
#         print(msg.format(time=runtime))
#
# def long_runner():
#     for x in range(5):
#         sleep_time = random.choice(range(1,5))
#         time.sleep(sleep_time)
#
# if __name__ == '__main__':
#     with MyTimer():
#         long_runner()

# import cProfile
#
# cProfile.run('[x for x in range(1500)]')
# # python -m cProfile test.py

# # run with python -m memory_profiler python201.py
# @profile
# def mem_func():
#     lots_of_numbers = list(range(1500))
#     x = ['letters'] * (5 ** 10)
#     del lots_of_numbers
#     return None
#
# if __name__ == '__main__':
#     mem_func()
