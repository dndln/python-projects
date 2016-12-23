# import ipdb

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#
#     print(i)
#     i += 1

###

# try:
#     1 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")

###

# my_dict = {'a':1, 'b':2, 'c':3}
#
# try:
#     value = my_dict['a']
# except KeyError:
#     print('A KeyError occurred.')
# else:
#     print('No error occurred.')
# finally:
#     print('The finally statement ran. This will run whether or '
#         'not an error was raised.')

###

# handle = open('test.txt', 'r')
# # data = handle.read()
# data = handle.readlines() # returns a list of lines
# print(data)
# handle.close()

# handle = open('test.txt', 'r')
# for line in handle:
#     print(line)
# handle.close()

# handle = open('test.txt', 'r')
# while True:
#     data = handle.read(1024)
#     print(data)
#     if not data:
#         break

# # read binary file
# handle = open('test.pdf', 'rb')

# handle = open('output.txt', 'w')
# handle.write('this is a test.')
# handle.close()

# # once the "with" code block is left, the file handle
# # will be closed.
# with open('test.txt') as file_handler:
#     for line in file_handler:
#         print(line)

# try:
#     file_handler = open('test.txt')
#     for line in file_handler:
#         print(line)
# except IOError:
#     print('An IOError has occurred.')
# finally:
#     file_handler.close()

## using `"with" removes the need for the "finally" statement.
# try:
#     with open('test.txt') as file_handler:
#         for line in file_handler:
#             print(line)
# except IOError:
#     print('An IOError has occurred.')

# # the names *args and **kwargs are just convention.
# def many(*bill, **ted):
#     print(bill)
#     print(ted)
# # >>> python101.many(1,2,3,name='mike',job='programmer')
# # (1, 2, 3)
# # {'job': 'programmer', 'name': 'mike'}
# # *args turns into a tuple, **kwargs turns into a dict.
#
# # DRY: Don't Repeat Yourself.
# # If you start writing repeated code, put it in a function!

# # Capitalise the first letter of a class.
# # "object" is what the class is inheriting from.
# # In Python, everything is an object, so they inherit from
# # the "object" class.
# # "object" is the base class, so everything has the same
# # methods the "object" class has, by default.
# class Vehicle(object):
#     """docstring"""
#
#     def __init__(self):
#         """Constructor"""
#         pass
#
# a = object()
# dir(a)
# help(a.__getattribute__)

# # If we inherit from "object", we can just say:
# class Vehicle:

## a method has to have at least one argument (self).

# class Vehicle(object):
#     """docstring"""
#
#     def __init__(self, color='blue', doors=4, tires=4, vtype='car'):
#         # all docstrings and methods show up when I call
#         # help(vehicleinstance)
#         """Constructor"""
#         self.color = color
#         self.doors = doors
#         self.tires = tires
#         self.vtype = vtype
#
#     def brake(self):
#         """
#         Stop the car
#         """
#         return ('{} braking'.format(self.vtype))
#
#     def drive(self):
#         # shows up when I call help(vehicleinstance.drive)
#         """
#         Drive the car
#         """
#         return ("I'm driving a {0} {1}!".format(self.color, self.vtype))
#
# # Subclassing the "Vehicle" class lets me instantiate a
# # new "car" without any arguments.
# # using the default methods and values is inheritance.
# class Car(Vehicle):
#     """
#     The Car class
#     """
#
#     def brake(self):
#         """
#         Override brake method
#         """
#         return 'The car class is braking slowly!'

# if __name__ == '__main__':
#     car = Car()
#     print(car.brake())
#     print(car.drive())
#
#     truck = Vehicle('red', 3, 6, 'truck')
#     print(truck.brake())
#     print(truck.drive())

## dir() will return a list of names in the current scope.
# import pandas as pd
# dir(pd)

# import csv
#
# def csv_reader(file_obj):
#     """
#     Read a csv file using csv.reader
#     """
#     reader = csv.reader(file_obj)
#     for row in reader:
#         print(" ".join(row))
#
# if __name__ == '__main__':
#     csv_path = 'TB_data_dictionary_2016-12-21.csv'
#     with open(csv_path, 'r') as file_obj:
#         csv_reader(file_obj)

# import csv
# def csv_dict_reader(file_obj):
#     """
#     Read a csv file using csv.DictReader
#     """
#     reader = csv.DictReader(file_obj, delimiter=',')
#     for line in reader:
#         print(line['first_name'])
#         print(line['last_name'])
#
# if __name__ == '__main__':
#     with open('data.csv') as file_obj:
#         csv_dict_reader(file_obj)

# import csv
#
# def csv_writer(data, path):
#     """
#     Write data to a CSV file path
#     """
#     with open(path, 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file, delimiter=',')
#         for line in data:
#             writer.writerow(line)
#
# if __name__ == '__main__':
#     data = ['first_name,last_name,city'.split(','),
#         # spaces will cause spaces in the cells
#         ' Tyrese, Hirthe, Strackeport'.split(','),
#         'Jules,Dicki,Lake Nickolasville'.split(','),
#         'Dedric,Medhurst,Stiedemann'.split(',')]
#     path = 'output.csv'
#     csv_writer(data, path)

# import csv
#
# def csv_dict_writer(path, fieldnames, data):
#     """
#     Writes a CSV file using DictWriter
#     """
#     with open(path, 'w', newline='') as out_file:
#         writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
#         writer.writeheader()
#         for row in data:
#             writer.writerow(row)
#
# if __name__ == '__main__':
#     data = ['first_name,last_name,city'.split(','),
#         'Tyrese,Hirthe,Strackeport'.split(','),
#         'Jules,Dicki,Lake Nickolasville'.split(','),
#         'Dedric,Medhurst,Stiedemann'.split(',')]
#     my_list = []
#     fieldnames = data[0]
#     for values in data[1:]:
#         inner_dict = dict(zip(fieldnames, values))
#         my_list.append(inner_dict)
#
#     path = 'dict_output.csv'
#     csv_dict_writer(path, fieldnames, my_list)

# import configparser
#
# def createConfig(path):
#     """
#     Crate a config file
#     """
#     config = configparser.ConfigParser()
#     config.add_section('Settings')
#     config.set('Settings', 'font', 'Courier')
#     config.set('Settings', 'font_size', '10')
#     config.set('Settings', 'font_style', 'Normal')
#     config.set('Settings', 'font_info',
#         # 'You are using {0} at {1} pt'.format(font, font_size)) # this line doesn't work
#         'You are using %(font)s at %(font_size)s pt')
#
#     with open(path, 'w') as config_file:
#         config.write(config_file)
#
# if __name__ == '__main__':
#     path = 'settings.ini'
#     createConfig(path)

# import configparser
# import os
# import ipdb
#
# def crud_config(path):
#     """
#     Create, read, update, delete config
#     """
#     if not os.path.exists(path):
#         createConfig(path)
#
#     config = configparser.ConfigParser()
#     config.read(path)
#
#     # read some values from the config
#     font = config.get('Settings', 'font')
#     font_size = config.get('Settings', 'font_size')
#
#     # change a value in the config
#     config.set('Settings', 'font_size', '12')
#
#     # delete a value from the config
#     config.remove_option('Settings', 'font_style')
#
#     # write changes back to config file
#     with open(path, 'w') as config_file:
#         config.write(config_file)
#
# if __name__ == '__main__':
#     path = 'settings.ini'
#     crud_config(path)

# import configparser
# import os
#
# def create_config(path):
#     """
#     Create a config file
#     """
#     config = configparser.ConfigParser()
#     config.add_section('Settings')
#     config.set('Settings', 'font', 'Courier')
#     config.set('Settings', 'font_style', 'Normal')
#     config.set('Settings', 'font_size', '10')
#     # this doesn't work
#     # config.set('Settings', 'font_info',
#     #     'You are using {} at {} pt.format(font, font_size)')
#     config.set('Settings', 'font_info',
#         'You are using %(font)s at %(font_size)s pt')
#
#
#     with open(path, 'w') as config_file:
#         config.write(config_file)
#
# def get_config(path):
#     """
#     Returns the config object
#     """
#     if not os.path.exists(path):
#         create_config(path)
#
#     config = configparser.ConfigParser()
#     config.read(path)
#     return config
#
# def get_setting(path, section, setting):
#     """
#     Print out a setting
#     """
#     config = get_config(path)
#     value = config.get(section, setting)
#     msg = '{section} {setting} is {value}'.format(
#         section=section, setting=setting, value=value)
#     print(msg)
#     return value
#
# def update_setting(path, section, setting, value):
#     """
#     Update a setting
#     """
#     config = get_config(path)
#     config.set(section, setting, value)
#     with open(path, 'w') as config_file:
#         config.write(config_file)
#
# def delete_setting(path, section, setting):
#     """
#     Delete a setting
#     """
#     config = get_config(path)
#     config.remove_option(section, setting)
#     with open(path, 'w') as config_file:
#         config.write(config_file)
#
# if __name__ == '__main__':
#     path = 'settings.ini'
#     font = get_setting(path, 'Settings', 'font')
#     font_size = get_setting(path, 'Settings', 'font_size')
#     font_info = get_setting(path, 'Settings', 'font_info')
#     update_setting(path, 'Settings', 'font_size', '12')
#     delete_setting(path, 'Settings', 'font_style')

# import configparser
# import os
#
# def interpolation_demo(path):
#     if not os.path.exists(path):
#         create_config(path)
#
#     config = configparser.ConfigParser()
#     config.read(path)
#
#     print(config.get('Settings', 'font_info'))
#     print(config.get('Settings', 'font_info', vars={'font':'Arial', 'font_size':'100'}))
#
# if __name__ == '__main__':
#     path = 'settings.ini'
#     interpolation_demo(path)

# import logging
#
# # add filemode='w' to overwrite the log file instead of appending
# logging.basicConfig(filename='sample.log', level=logging.INFO)
#
# logging.debug('This is a debug message')
# logging.info('Informational message')
# logging.error('An error has happened!')

# import logging
#
# logging.basicConfig(filename='sample.log', level=logging.INFO)
# # use .getLogger to return a logger object names 'ex'
# log = logging.getLogger('ex')
#
# try:
#     raise RuntimeError
# except RuntimeError:
#     log.exception('Error!')
# # output:
# # ERROR:ex:Error!
# # Traceback (most recent call last):
# #   File "python101.py", line 401, in <module>
# #     raise RuntimeError
# # RuntimeError

# import logging
# import otherMod
#
# def main():
#     """
#     The main entry point of the application
#     """
#     logging.basicConfig(filename='mySnake.log', level=logging.INFO)
#     logging.info('Program started')
#     result = otherMod.add(7, 8)
#     logging.info('Done!')
#
# if __name__ == '__main__':
#     main()

import logging
import otherMod2

def main():
    """
    The main entry point of the application
    """
    logger = logging.getLogger('exampleApp')
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler('new_snake.log')

    formatter = logging.Formatter('''%(asctime)s - %(name)s - %(levelname)s -
        %(message)s''')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info('Program started')
    result = otherMod2.add(7, 8)
    logger.info('Done!')

if __name__ == '__main__':
    main()
