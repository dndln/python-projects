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

# # hashing
# import hashlib
#
# md5 = hashlib.md5() # create an instance of an md5 as object
# md5.update(b'Python rocks!') # Must encode unicode objects into bytes
# print(md5.digest())
# print(md5.hexdigest())
# sha = hashlib.sha1(b'Hello Python').hexdigest()
# print(sha)

# # salting
# # use bcrypt or scrypt for real world applications
# import hashlib
# import binascii
#
# dk = hashlib.pbkdf2_hmac(hash_name='sha256',
#     password=b'bad_password34',
#     salt=b'bad_salt',
#     iterations=100000)
# print(binascii.hexlify(dk))

# # conda install pycrypto
# from Crypto.PublicKey import RSA
# code = 'nooneknows'
# key = RSA.generate(2048)
# encrypted_key = key.exportKey(passphrase=code, pkcs=8)
# with open('/home/andy/Desktop/my_private_rsa_key.bin', 'wb') as f:
#     f.write(encrypted_key)
# with open('/home/andy/Desktop/my_public_rsa_key.pem', 'wb') as f:
#     f.write(key.publickey().exportKey())

# # conda install cryptography
# from cryptography.fernet import Fernet
# cipher_key = Fernet.generate_key()
# print(cipher_key)
# cipher = Fernet(cipher_key)
# text = b'My super secret message'
# print(text)
# encrypted_text = cipher.encrypt(text)
# print(encrypted_text)
# decrypted_text = cipher.decrypt(encrypted_text)
# print(decrypted_text)

# # super
# class MtParentClass():
#     def __init__(self, x, y):
#         pass
#
# class SubClass(MyParentClass):
#     def __init__(self, x, y):
#         super().__init__(x, y)

# # Method Resolution order (which parent method is called first?)
# class X:
#     def __init_(self):
#         print('X')
#         super().__init__()
#
# class Y:
#     def __init_(self):
#         print('Y')
#         super().__init__()
#
# class Z(X, Y):
#     pass
#
# z = Z()
# print(Z.__mro__)
# # (<class '__main__.Z'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>)
# # 'X' and 'Y' are not printed though?

# class Base:
#     var = 5
#     def __init__(self):
#         pass
#
# class X(Base):
#     def __init__(self):
#         print('X')
#         super().__init__()
#
# class Y(Base):
#     var = 10
#     def __init__(self):
#         print('Y')
#         super().__init__()
#
# class Z(X, Y):
#     pass
#
# z = Z()
# print(Z.__mro__)
# print(super(Z, z).var) # checks if var is defined in X, then Y, the Base, then object.
# # the order it checks is the "method resolution order".

# # descriptors
# class MyDescriptor():
#     """
#     A simple demo desciptor
#     """
#     def __init__(self, initial_value=None, name='my_var'):
#         self.var_name = name
#         self.value = initial_value
#
#     def __get__(self, obj, objtype):
#         print('Getting', self.var_name)
#         return self.value
#
#     def __set__(self, obj, value):
#         msg = 'Setting {name} to {value}'
#         print(msg.format(name=self.var_name, value=value))
#         self.value = value
#
# class MyClass():
#     desc = MyDescriptor(initial_value='Mike', name='desc')
#     normal = 10
#
# if __name__ == '__main__':
#     c = MyClass()
#     print(c.desc)
#     print(c.normal)
#     c.desc = 100
#     print(c.desc)

# # using a descriptor to do validation
# from weakref import WeakKeyDictionary
#
# class Drinker:
#     def __init__(self):
#         self.req_age = 21
#         self.age = WeakKeyDictionary()
#
#     def __get__(self, instance_obj, objtype):
#         return self.age.get(instance_obj, self.req_age)
#
#     def __set__(self, instance, new_age):
#         if new_age < 21:
#             msg = '{name} is too young to legally imbibe'
#             raise Exception(msg.format(name=instance.name))
#         self.age[instance] = new_age
#         print('{name} can legally drink in the USA'.format(name=instance.name))
#
#     def __delete__(self, instance):
#         del self.age[instance]
#
# class Person:
#     drinker_age = Drinker()
#
#     def __init__(self, name, age):
#         self.name = name
#         self.drinker_age = age
#
# p = Person('Miguel', 30)
# p = Person('Niki', 13)

# # local scope assignment
# x = 10
# def my_func(a, b):
#     print(x)
#     print(z)
#
# my_func(1, 2)
# # 'z' is not defined

# def my_func(a, b):
#     x = 5
#     print(x)
#
# if __name__ == '__main__':
#     x = 10
#     my_func(1, 2) # prints 5
#     print(x) # prints 10

# def func():
#     global x
#     print(x)
#     x = 5
#     print(x)
#
# if __name__ == '__main__':
#     x = 10
#     func() # prints 10 and 5
#     print(x) # x is still 5 outside the function -> don't modify globals inside a function

# # nonlocal scope - allows you to assign variables to outer scopes, but not global scope
# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#     return incrementer
#
# c = counter()
# print(c)
# print(c())
# print(c())
# print(c())
# print(c())

# # Web Scraping
# # scraping a blog:
# # right click and inspect element on what you want to scrape
# import requests
# from bs4 import BeautifulSoup
# import pprint
# import ipdb
#
# url = 'http://blog.pythonlibrary.org/'
#
# def get_articles():
#     """
#     Get the articles from the front page of the blog
#     """
#     req = requests.get(url)
#     html = req.text # pull the html out as a string using the 'text' property
#     # soup and pages are iterable
#     soup = BeautifulSoup(html, 'html.parser') # turns the long html string into an object
#     pages = soup.findAll('h1') # get all the <h1> headers
#
#     # dictionary comprehension to extract href (url) and text (title)
#     articles = {i.a['href']: i.text.strip() for i in pages if i.a}
#     for article in articles:
#         s = '{title}: {url}'.format(
#             title=articles[article],
#             url=article)
#         pprint.pprint(s)
#
#     return articles
#
# if __name__ == '__main__':
#     articles = get_articles()

# # scraping twitter
# # inspect element shows we need the 'li' tag and the 'js-stream-item' class
# # written on 20170114, may be out of date (had to edit the code in the textbook)
# import requests
# from bs4 import BeautifulSoup
# import ipdb
#
# url = 'https://twitter.com/mousevspython'
# req = requests.get(url)
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
# tweets = soup.findAll('li', 'js-stream-item') # found by 'inspecting element' in browser
# for item in range(len(soup.find_all('p', 'TweetTextSize'))):
#     # <p class="TweetTextSize TweetTextSize--26px js-tweet-text tweet-text" data-aria-label-part="0" lang="en">
#     # can use .text instead of .get_text()
#     tweet_text = tweets[item].find('p').get_text() # only 1 'p' in each tweet
#     print(tweet_text)
#     dt = tweets[item].find('a', 'tweet-timestamp')
#     timestamp = dt['title']
#     print('This was tweeted on ' + timestamp)

# # Writing a web crawler
# # "conda install scrapy"
# # 'scrapy startproject blog_scrapter' in bash
# # look in 'blog_scraper/blog_scraper/items.py' and 'blog_scraper/blog_scraper/spiders/blog.py'
# # cd blog_scraper
# # scrapy crawl mouse
# # scrapy crawl mouse -o articles.csv -t csv

# # Web APIs
# # Python wrapper for the Twitter API
# # pip install tweepy
# import tweepy
#
# key = 'random_key'
# secret = 'random_secret'
# access_token = 'access_token'
# access_secret = 'super_secret'
#
# auth = tweepy.OAuthHandler(key, secret) # create authentication handler
# auth.set_access_token(access_token, access_secret) # set access token
# api = tweepy.API(auth) # create a Twitter API object
#
# my_tweets = api.user_timeline()
# for tweet in my_tweets:
#     print(tweet.text)
#
# # updating status with api
# api.update_status('I just tweeted using Python')
# api.update_with_media(filename, 'I can tweet files with Python')

# # reddit
# # pip install praw (Python Reddit Api Wrapper)
# # requires client_id, so the following is untested
# import praw
#
# red = praw.Reddit(user_agent='pyred')
# red.get_top()
# print(red.get_top())
# for i in red.get_top():
#     print(i)
#
# python = red.getsubreddit('python')
# submissions = python.get_hot(limit=5)
# print(submissions)
# for submission in submissions:
#     print(submission)
#
# id = '4q21xb'
# submission = red.get_submission(submission_id=id)
# comments = submission.comments
# print(comments)
# print(comments[0].author)
# print(comments[0].body)

# # Wikipedia
# # pip install wikipedia
# import wikipedia
#
# print(wikipedia.search('Python'))
# print(wikipedia.summary('Python (programming language)'))

# import wikipedia
#
# def print_wikipedia_results(word):
#     """
#     Searches for pages that match the specified word
#     """
#     results = wikipedia.search(word)
#
#     for result in results:
#         # ipdb.set_trace()
#         try:
#             page = wikipedia.page(result)
#         except wikipedia.exceptions.DisambiguationError:
#             print('DisambiguationError')
#             continue
#         except wikipedia.exceptions.PageError:
#             print('PageError for result: ' + result)
#             continue
#
#         print(page.summary)
#
# if __name__ == '__main__':
#     print_wikipedia_results('wombat')

# # working with FTP
# from ftplib import FTP
# ftp = FTP('ftp.cse.buffalo.edu') # create an instance of FTP by passing url
# print(ftp.login())
#
# # connecting with non-standard port
# from ftplib import FTP
# ftp = FTP()
# HOST = 'ftp.cse.buffalo.edu'
# PORT = 12345
# ftp.connect(HOST, PORT)

# # downloading a file from FTP server
# from ftplib import FTP
# ftp = FTP('ftp.debian.org')
# ftp.login()
# ftp.cwd('debian') # same thing as cd
# out = '/home/andy/Desktop/README'
# with open(out, 'wb') as f:
#     ftp.retrbinary('RETR ' + 'README.html', f.write)

# # download all the file with a file listing
# # need to 'mkdir /home/andy/Desktop/ftp_test'
# import ftplib
# import os
#
# ftp = ftplib.FTP('ftp.debian.org')
# ftp.login()
# ftp.cwd('debian')
# filenames = ftp.nlst() # get a list of directory
#
# for filename in filenames:
#     host_file = os.path.join('/home/andy/Desktop/ftp_test', filename)
#     try:
#         with open(host_file, 'wb') as local_file:
#             ftp.retrbinary('RETR ' + filename, local_file.write)
#     except ftplib.error_perm:
#         pass
#
# ftp.quit()

# # uploading files to FTP
# # storlines -> text files
# # storbinary -> binary files
# import ftplib
#
# def ftp_upload(ftp_obj, path, ftype='TXT'):
#     """
#     A function for uploading files to an FTP server
#     """
#     if ftype='TXT':
#         with open(path) as fobj:
#             ftp.storlines('STOR ' + path, fobj)
#     else:
#         with open(path, 'rb') as fobj:
#             ftp.storbinary('STOR ' + path, fobj, 1024)
#
# if __name__ == '__main__':
#     ftp = ftplib.FTP('host', 'username', 'password')
#     ftp.login()
#
#     path = '/path/to/something.txt'
#     ftp.upload(ftp, path)
#
#     pdf_path = '/path/to/something.pdf'
#     ftp_upload(ftp, pdf_path, ftype='PDF')
#
#     ftp.quit()

# # urllib (lower level than requests)
# import urllib.request
#
# url = urllib.request.urlopen('https://www.google.com/')
# print(url.geturl())
# header = url.info()
# print(header.as_string())
# print(url.read())

# import urllib.request
# url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbView\
# er.zip'
# response = urllib.request.urlopen(url)
# data = response.read()
# with open('/home/andy/Desktop/test.zip', 'wb') as fobj:
#     fobj.write(data)

# # parsing url strings
# from urllib.parse import urlparse
#
# result = urlparse('https://duckduckgo.com/?q=python+stubbing&t=canonical&ia=\
# qa')
# print(result)
# print(result.netloc)
# print(result.geturl())
# print(result.port)

# # submitting a web form
# import urllib.request
# import urllib.parse
#
# data = urllib.parse.urlencode({'q': 'Python'})
# print(data)
# url = 'http://duckduckgo.com/html/'
# full_url = url + '?' + data
# response = urllib.request.urlopen(full_url)
# with open('/home/andy/Desktop/results.html', 'wb') as f:
#     f.write(response.read())

# # reading robots.txt
# import urllib.robotparser
#
# robot = urllib.robotparser.RobotFileParser()
# robot.set_url('http://arstechnica.com/robots/txt')
# robot.read()
# print(robot.can_fetch('*', 'http://arstechnica.com/'))
# print(robot.can_fetch('*', 'http://arstechnica.com/cgi-bin/'))

# # coverage run test_mymath.py
# # coverage report -m
# # coverage html

# Concurrency
# asyncio, threading, multiprocessing, concurrent.futures

# # a bad coroutine example
# import asyncio
# import os
# import urllib.request # urllib is not asynchronous
#
# # this function is a coroutine, but isn't asynchronous
# async def download_coroutine(url):
#     """
#     A coroutine to download the specified url
#     """
#     request = urllib.request.urlopen(url)
#     filename = os.path.basename(url)
#
#     with open(filename, 'wb') as file_handle:
#         while True:
#             chunk = request.read(1024)
#             if not chunk:
#                 break
#             file_handle.write(chunk)
#     msg = 'Finished downloading {filename}'.format(filename=filename)
#     return msg
#
# async def main(urls):
#     """
#     Creates a group of coroutines and waits for them to finish
#     """
#     coroutines = [download_coroutine(url) for url in urls]
#     completed, pending = await asyncio.wait(coroutines)
#     for item in completed:
#         print(item.result())
#
# if __name__ == '__main__':
#     urls = ['http://www.irs.gov/pub/irs-pdf/f1040.pdf',
#         'http://www.irs.gov/pub/irs-pdf/f1040a.pdf',
#         'http://www.irs.gov/pub/irs-pdf/f1040ez.pdf',
#         'http://www.irs.gov/pub/irs-pdf/f1040es.pdf',
#         'http://www.irs.gov/pub/irs-pdf/f1040sb.pdf']
#
#     event_loop = asyncio.get_event_loop()
#     try:
#         event_loop.run_until_complete(main(urls)) # run the main coroutine, which
#         # runs the download_coroutine coroutine (chained coroutine)
#     finally:
#         event_loop.close()

# # better coroutine example
# # pip install aiohttp
# import aiohttp
# import asyncio
# import async_timeout
# import os
#
# async def download_coroutine(session, url):
#     with async_timeout.timeout(10):
#         async with session.get(url) as response:
#             filename = os.path.basename(url)
#             with open(filename, 'wb') as f_handle:
#                 while True:
#                     chunk = await response.content.read(1024)
#                     if not chunk:
#                         break
#                     f_handle.write(chunk)
#             return await response.release()
#
# async def main(loop):
#     urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
#
#     async with aiohttp.ClientSession(loop=loop) as session:
#         for url in urls:
#             await download_coroutine(session, url)
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main(loop))


# # multithreading
# # multithreading is best for file I/O, using multiple cores is bad because of the GIL
# # printing to stdout can be jumbled
# import threading
#
# def doubler(number):
#     """
#     A function that can be used by a thread
#     """
#     print(threading.currentThread().getName() + '\n')
#     print(number * 2)
#     print()
#
# if __name__ == '__main__':
#     for i in range(5):
#         my_thread = threading.Thread(target=doubler, args=(i,))
#         my_thread.start()


# # using logging (which is thread safe)
# import logging
# import threading
#
# def get_logger():
#     logger = logging.getLogger('threading_example')
#     logger.setLevel(logging.DEBUG)
#
#     fh = logging.FileHandler('threading.log')
#     fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
#     formatter = logging.Formatter(fmt)
#     fh.setFormatter(formatter)
#
#     logger.addHandler(fh)
#     return logger
#
# def doubler(number, logger): # pass the logger in, otherwise end up with lots of logging singletons
#     """
#     A function that can be used by a thread
#     """
#     logger.debug('doubler function executing')
#     result = number * 2
#     logger.debug('doubler function ended with: {result}'.format(result=result))
#
# if __name__ == '__main__':
#     logger = get_logger()
#     thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
#     for i in range(5):
#         my_thread = threading.Thread(
#             target=doubler, name=thread_names[i], args=(i, logger))
#         my_thread.start()

# # subclassing threading.Thread
# import logging
# import threading
#
# class MyThread(threading.Thread):
#
#     def __init__(self, number, logger):
#         threading.Thread.__init__(self)
#         self.number = number
#         self.logger = logger
#
#     def run(self):
#         """
#         Run the thread
#         """
#         logger.debug('Calling doubler')
#         doubler(self.number, self.logger)
#
# def get_logger():
#     logger = logging.getLogger('threading_example')
#     logger.setLevel(logging.DEBUG)
#
#     fh = logging.FileHandler('threading_class.log')
#     fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
#     formatter = logging.Formatter(fmt)
#     fh.setFormatter(formatter)
#
#     logger.addHandler(fh)
#     return logger
#
# def doubler(number, logger):
#     """
#     A function that can be used by a thread
#     """
#     logger.debug('doubler function executing')
#     result = number * 2
#     logger.debug('doubler function ended with: {}'.format(
#         result))
#
# if __name__ == '__main__':
#     logger = get_logger()
#     thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
#     for i in range(5):
#         thread = MyThread(i, logger)
#         thread.setName(thread_names[i])
#         thread.start()

# # adding a lock
# import threading
#
# total = 0
# lock = threading.Lock()
#
# def update_total(amount):
#     """
#     Updates the total by the given amount
#     """
#     global total
#     lock.acquire()
#     try:
#         total += amount
#     finally:
#         lock.release()
#         print(total)
#
# if __name__ == '__main__':
#     for i in range(0, 10):
#         my_thread = threading.Thread(
#             target=update_total, args=(5,))
#         my_thread.start()

# # using a Timer
# import subprocess
# from threading import Timer
#
# kill = lambda process: process.kill()
# cmd = ['ping', 'www.google.com']
# ping = subprocess.Popen(
#     cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
# # waits 5 seconds before calling thread
# my_timer = Timer(5, kill, [ping])
#
# try:
#     my_timer.start()
#     stdout, stderr = ping.communicate()
# finally:
#     my_timer.cancel()
#
# print(str(stdout))

# # communication between threads
# import threading
# from queue import Queue
#
# def creator(data, q):
#     """
#     Creates data to be consumed and waits for the consumer
#     to finish processing
#     """
#     print('Creating data and putting it on the queue')
#     for item in data:
#         evt = threading.Event()
#         q.put((item, evt))
#         print('Waiting for data to be doubled')
#         evt.wait()
#
# def my_consumer(q):
#     """
#     Consumes some data and works on it
#     In this case, all it does is double th input
#     """
#     while True:
#         data, evt = q.get()
#         print('data found to be processed: {}'.format(data))
#         processed = data * 2
#         print(processed)
#         evt.set()
#         q.task_done()
#
# if __name__ == '__main__':
#     q = Queue()
#     data = [5, 10, 13, -1]
#     thread_one = threading.Thread(target=creator, args=(data, q))
#     thread_two = threading.Thread(target=my_consumer, args=(q,))
#     thread_one.start()
#     thread_two.start()
#
#     q.join()

# # spawning multiple processes to avoid the GIL (instead of threads)
# # threads share memory, processes don't.
# import os
# from multiprocessing import Process
#
# def doubler(number):
#     """
#     A doubling function that can be used by a process
#     """
#     result = number * 2
#     proc = os.getpid()
#     print('{0} doubled to {1} by process id: {2}'.format(
#         number, result, proc))
#
# if __name__ == '__main__':
#     numbers = [5, 10, 15, 20, 25]
#     procs = []
#
#     for index, number in enumerate(numbers):
#         proc = Process(target=doubler, args=(number,)) # create a Process
#         procs.append(proc)
#         proc.start() # start the process
#
#     for proc in procs:
#         proc.join() # wait for a process to terminate

# # naming processes
# import os
# from multiprocessing import Process, current_process
#
# def doubler(number):
#     """
#     A doubling function that can be used by a process
#     """
#     result = number * 2
#     proc_name = current_process().name
#     print('{0} doubled to {1} by process id: {2}'.format(
#         number, result, proc_name))
#
# if __name__ == '__main__':
#     numbers = [5, 10, 15, 20, 25]
#     procs = []
#     proc = Process(target=doubler, args=(5,))
#
#     for index, number in enumerate(numbers):
#         proc = Process(target=doubler, args=(number,)) # create a Process
#         procs.append(proc)
#         proc.start() # start the process
#
#     proc = Process(target=doubler, name='Test', args=(2,))
#     proc.start()
#     procs.append(proc)
#
#     for proc in procs:
#         proc.join() # wait for a process to terminate

# # using multiprocessing's Lock
# from multiprocessing import Process, Lock
#
# def printer(item, lock):
#     """
#     Prints out the item that was passed in
#     """
#     lock.acquire() # next process waits for this lock to release
#     try:
#         print(item)
#     finally:
#         lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     items = ['tango', 'foxtrot', 10]
#     for item in items:
#         p = Process(target=printer, args=(item, lock))
#         p.start()

# # adding logging to multiprocessing
# import logging
# import multiprocessing
# from multiprocessing import Process, Lock
#
# def printer(item, lock):
#     """
#     Prints out the item that was passed in
#     """
#     lock.acquire()
#     try:
#         print(item)
#     finally:
#         lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     items = ['tango', 'foxtrot', 10]
#     multiprocessing.log_to_stderr()
#     logger = multiprocessing.get_logger()
#     logger.setLevel(logging.INFO)
#     for item in items:
#         p = multiprocessing.Process(target=printer, args=(item, lock))
#         p.start()

# # The Pool class represents a pool of worker processes
# import multiprocessing
#
# def doubler(number):
#     return number * 2
#
# if __name__ == '__main__':
#     numbers = [5, 10, 20]
#     pool = multiprocessing.Pool(processes=3) # create 3 worker processes
#     print(pool.map(doubler, numbers)) # map a function and an iterable to each process

# from multiprocessing import Pool
#
# def doubler(number):
#     return number * 2
#
# if __name__ == '__main__':
#     pool = Pool(processes=3)
#     result = pool.apply_async(doubler, (25,))
#     print(result.get(timeout=1)) # get the result

# # communicating between processes with Queues and Pipes
# import multiprocessing
#
# sentinel = -1
#
# def creator(data, q):
#     """
#     Creates data to be consumed and waits for the consumer
#     to finish processing
#     """
#     print('Creating data and putting it on the queue')
#     for item in data:
#         q.put(item) # queue looks like [5, 10, 13, -1]
#
# def my_consumer(q):
#     """
#     Consumes some data and works on it
#
#     In this case, all it does is double the input
#     """
#     while True:
#         data = q.get() # gets the first item from the queue
#         print('data found to be processd: {}'.format(data))
#         processed = data * 2
#         print(processed)
#
#         if data is sentinel:
#             break
#
# if __name__ == '__main__':
#     q = multiprocessing.Queue()
#     data = [5, 10, 13, -1] # without -1 (sentinel) at the end, process won't stop running
#     process_one = multiprocessing.Process(target=creator, args=(data, q))
#     process_two = multiprocessing.Process(target=my_consumer, args=(q,))
#     process_one.start()
#     process_two.start()
#
#     q.close() # prevent any more tasks being added
#     q.join_thread()
#
#     process_one.join() # call join() on the processes rather than the Queue
#     process_two.join()

# # asynchronously executing callables (an abstraction layer on top of
# #   threading and multiprocessing (removes flexibility)
# # "future" means a pending result (describe the result of a process before it's finished)
# import os
# import urllib.request
# from concurrent.futures import ThreadPoolExecutor
# from concurrent.futures import as_completed
#
# def downloader(url):
#     """
#     Downloads the specified URL and saves it to disk
#     """
#     req = urllib.request.urlopen(url)
#     filename = os.path.basename(url)
#     ext = os.path.splitext(url)[1]
#     if not ext:
#         raise RuntimeError('URL does not contain an extension')
#
#     with open(filename, 'wb') as file_handle:
#         while True:
#             chunk =  req.read(1024)
#             if not chunk:
#                 break
#             file_handle.write(chunk)
#     msg = 'Finished downloading {filename}'.format(filename=filename)
#     return msg
#
# def main(urls):
#     """
#     Create a thread pool and download specified urls
#     """
#     with ThreadPoolExecutor(max_workers=5) as executor: # instantiate the thread pool
#         futures = [executor.submit(downloader, url) for url in urls]
#         for future in as_completed(future): # as_completed yields futures as they finish/are cancelled
#             print(future.result())
#
# if __name__ == '__main__':
#     urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
#     main(urls)

# # deadlocks
# # this code actually doesn't deadlock when tested, just doesn't print anything
# from concurrent.futures import ThreadPoolExecutor
#
# def wait_forever():
#     """
#     This function will wait forever if there's only one thread assigned to the pool
#     """
#     my_future = executor.submit(zip, [1, 2, 3], [4, 5, 6])
#     result = my_future.result()
#     print(result)
#
# if __name__ == '___main__':
#     executor = ThreadPoolExecutor(max_workers=1)
#     executor.submit(wait_forever)

# # avoiding deadlock
# # This does output the zipped lists
# from concurrent.futures import ThreadPoolExecutor
#
# def wait_forever():
#     """
#     This function will wait forever if there's only one thread assigned to the pool
#     """
#     my_future = executor.submit(zip, [1, 2, 3], [4, 5, 6])
#
#     return my_future
#
# if __name__ == '__main__':
#     executor = ThreadPoolExecutor(max_workers=3)
#     fut = executor.submit(wait_forever)
#
#     result = fut.result()
#     print(list(result.result()))
