## Contents:
##     opening/reading binary files
##     *args, **kwargs
##     Classes and Subclasses (inheritance)
##     the 'csv' module
##     parsing configurations with ConfigParser
##     logging with logging
##     sending emails with smtplib
##     running bash commands with subprocess
##     multithreading with threading
##     downloading pdfs online with urllib.request
##     datetimes with datetime, datetimes with time
##     xml with xml.dom.minidom
##      creating and editing xml with ElementTree
##      Debugging with pdb
##      Decorators
##      The lambda statement
##      profiling code to find bottlenecks
##      testing

## creating module and package
## publising to PyPI
## eggs
## wheels
## py2exe (doesn't work on python 3)
## bb_freeze (doesn't work on python 3, or OSX)
## cx_Freeze
## PyInstaller
## GUI2Exe
## Create an installer with InnoSetup

# configobj: better version of ConfigParser
# lxml: more XML
# pylint/pyflakes: code analysers
# requests: better version of urllib
# SQLAlchemy
# virtualenv

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

# import logging
# import otherMod2
#
# def main():
#     """
#     The main entry point of the application
#     """
#     logger = logging.getLogger('exampleApp')
#     logger.setLevel(logging.INFO)
#
#     # create the logging file handler
#     fh = logging.FileHandler('new_snake.log')
#
#     formatter = logging.Formatter('''%(asctime)s - %(name)s - %(levelname)s -
#         %(message)s''')
#     fh.setFormatter(formatter)
#
#     # add handler to logger object
#     logger.addHandler(fh)
#
#     logger.info('Program started')
#     result = otherMod2.add(7, 8)
#     logger.info('Done!')
#
# if __name__ == '__main__':
#     main()

# import smtplib
#
# HOST = "mySMTP.server.com"
# SUBJECT = 'Test email from Python'
# TO = 'mike@someAddress.org'
# FROM = 'python@mydomain.com'
# text = 'Python 3.5 fules them all!'
#
# BODY = '\r\n'.join((
#     'From: {}'.format(FROM),
#     'To: {}'.format(TO),
#     'Subject: {}'.format(SUBJECT),
#     '',
#     text
#     ))
#
# server = smtplib.SMTP(HOST)
# server.sendmail(FROM, [TO], BODY)
# server.quit()


# # Sending multiple emails with TO, CC, BCC
# import os
# import smtplib
# import sys
#
# from configparser import ConfigParser
#
# def send_email(subject, body_text, to_emails, cc_emails, bcc_emails):
#     """
#     Send an email
#     """
#     base_path = os.path.dirname(os.path.abspath(__file__))
#     config_path = os.path.join(base_path, 'email.ini')
#
#     if os.path.exists(config_path):
#         cfg = ConfigParser()
#         cfg.read(config_path)
#     else:
#         print('Config not found! Exiting!')
#         sys.exit(1)
#
#     host = cfg.get('smtp', 'server')
#     from_addr = cfg.get('smtp', 'from_addr')
#
#     BODY = "\r\n".join((
#         "From: %s" % from_addr,
#         "To: %s" % ', '.join(to_emails),
#         "CC: %s" % ', '.join(cc_emails),
#         "BCC: %s" % ', '.join(bcc_emails),
#         "Subject: %s" % subject ,
#         "",
#         body_text
#         ))
#     emails = to_emails + cc_emails + bcc_emails
#
#     server = smtplib.SMTP(host)
#     server.sendmail(from_addr, emails, BODY)
#     server.quit()
#
# if __name__ == '__main__':
#     emails = ["mike@somewhere.org"]
#     cc_emails = ["someone@gmail.com"]
#     bcc_emails = ["schmuck@newtel.net"]
#
#     subject = "Test email from Python"
#     body_text = "Python rules them all!"
#     send_email(subject, body_text, emails, cc_emails, bcc_emails)

# import sqlite3
#
# conn = sqlite3.connect('mydatabase.db')
#
# cursor = conn.cursor()
#
# # create a table
# cursor.execute('''CREATE TABLE albums(
#     title text,
#     artist text,
#     release_date text,
#     publisher text,
#     media_type text
#     )
#     ''')

# import subprocess
#
# subprocess.call('gedit')
# subprocess.call(['ping', 'www.google.com'])
#
# program = 'gedit'
# subprocess.Popen(program)
# subprocess.Popen(['ls', '-a1'])

# import subprocess
#
# args = ['ls', '-l']
# process = subprocess.Popen(args, stdout=subprocess.PIPE)
# data = process.communicate()
# for line in data:
#     print(line)

# import sys
#
# print(sys.argv)

# # call exit.py
# import subprocess
#
# code = subprocess.call(['python', 'exit.py'])
# print(code)
# # code returns a 0, so it ran exit.py successfully

# # The threading module
# import random
# import time
# # from threading import Thread
# import threading
#
# class MyThread(threading.Thread):
#     """
#     A threading example
#     """
#
#     # This overrides the threading.Thread() init, so it needs to call
#     # threading.Thead.__init__(self) first
#     def __init__(self, name):
#         """Initialise the thread"""
#         threading.Thread.__init__(self)
#         self.name = name
#
#     # This overrides threading.Thread().run()
#     def run(self):
#         """Run the thread"""
#         amount = random.randint(3, 7)
#         time.sleep(amount) # Thread sleeps for a random amount of time before printing
#         msg = '{} is running'.format(self.name)
#         print(msg)
#
# def create_threads():
#     """
#     Create a group of threads
#     """
#     for i in range(5):
#         name = 'Thread #{}'.format(i+1)
#         my_thread = MyThread(name)
#         my_thread.start()
#
# if __name__ == '__main__':
#     create_threads()

# # Multithreaded downloading pdf forms from the U.S. Internal Renevue Service
# import os
# import urllib.request
# import threading
#
# class DownloadThread(threading.Thread):
#     """
#     A threading example that can download a file
#     """
#
#     def __init__(self, url, name):
#         """Initialise the thread"""
#         threading.Thread.__init__(self)
#         self.name = name
#         self.url = url
#
#     def run(self):
#         """Run the thread"""
#         handle = urllib.request.urlopen(self.url)
#         fname = os.path.basename(self.url)
#         with open(fname, 'wb') as f_handler:
#             while True:
#                 chunk = handle.read(1024)
#                 if not chunk:
#                     break
#                 f_handler.write(chunk)
#         msg = '{} has finished downloading {}!'.format(self.name, self.url)
#         print(msg)
#
# def main(urls):
#     """
#     Run the program
#     """
#     for item, url in enumerate(urls):
#         name = 'Thread {}'.format(item+1)
#         thread = DownloadThread(url, name)
#         thread.start()
#
# if __name__ == '__main__':
#     urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
#     main(urls)

# # Rewriting the download script to use Queues in cases where we want concurrency
# import os
# import threading
# import urllib.request
# from queue import Queue
#
# class Downloader(threading.Thread):
#     """Threaded File Downloader"""
#
#     def __init__(self, queue):
#         """Initialise the thread"""
#         threading.Thread.__init__(self)
#         self.queue = queue # queue is a type('Queue')
#
#     def run(self):
#         """Run the thread"""
#         while True:
#             # get the url from the queue
#             url = self.queue.get()
#
#             # download the file
#             self.download_file(url)
#
#             # send a signal to the queue that the job is done
#             self.queue.task_done()
#
#     def download_file(self, url):
#         """Download the file"""
#         handle = urllib.request.urlopen(url)
#         fname = os.path.basename(url) # get the flename from the url,
#             # so we know what to save it as on the local drive
#         with open(fname, 'wb') as f:
#             while True:
#                 chunk = handle.read(1024)
#                 if not chunk: break
#                 f.write(chunk)
#
# def main(urls):
#     """
#     Run the program
#     """
#     queue = Queue()
#
#     # create a thread fool and give them a queue
#     for i in range(5):
#         t = Downloader(queue)
#         t.daemon = True
#         t.start()
#
#     # give the queue some data
#     for url in urls:
#         queue.put(url)
#
#     # wait for the queue to finish
#     queue.join()
#
# if __name__ == '__main__':
#     urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
#         "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
#     main(urls)

# # datetime
# import datetime
#
# datetime.date.today() # Only has year, month, day
# # datetime.date(2014, 3, 5)
# datetime.datetime.today()
# # datetime.datetime(2014, 3, 5, 17, 56, 10, 737000)
# datetime.datetime.now()
# # datetime.datetime(2014, 3, 5, 17, 56, 15, 418000)

# import datetime
#
# now = datetime.datetime.now()
# # datetime.datetime(2016, 12, 26, 21, 6, 3, 224132)
# then = datetime.datetime(2014, 2, 26)
# delta = now - then
# delta.days
# # 1034
# delta.seconds
# # 75985
# type(delta)
# # <class 'datetime.timedelta'>
# seconds = delta.total_seconds()
# seconds
# # 89413585.573098
# hours = seconds / 3600
# minuts = (seconds % 3600) / 60

# import time
#
# # the start of history (the epoch)
# print(time.gmtime(0))
# # time.time() gets current seconds from the epoch
# print(time.time())
# # time.ctime() converts time in seconds from the epoch into a string representing local time
# print(time.ctime(time.time()))
# # time.ctime() uses time.time() by default if no argument is passed
# print(time.ctime())

# import time
#
# for x in range(0, 5):
#     # useful when waiting for a file to finish closing or a database commit to finish
#     time.sleep(2)
#     print('Slept for 2 seconds')

# import time
#
# # UTC time, as a struct
# print(time.gmtime())
# # Local time (dst flag = 1 if daylight saving is on), as a struct
# print(time.localtime())
# # convert struct into string
# # need to pass the format, and a time tuple unlike datetime.strftime()
# print(time.strftime('%Y-%m-%d.%H:%M:%S', time.localtime()))

# import xml.dom.minidom
# import urllib.request
#
# class ApptParser(object):
#
#     def __init__(self, url, flag='url'):
#         self.list = []
#         self.appt_list = []
#         self.flag = flag
#         self.rem_value = 0
#         xml = self.getXml(url)
#         self.handleXml(xml)
#
#     def getXml(self, url):
#         try:
#             print(url)
#             f = urllib.request.urlopen(url)
#         except:
#             f = url
#
#         doc = xml.dom.minidom.parse(f)
#         node = doc.documentElement
#         if node.nodeType == xml.dom.Node.ELEMENT_NODE:
#             print('Element name: {}'.format(node.nodeName))
#             for (name, value) in node.attributes.items():
#                 print('    Attribute Name: {}    Value: {}'.format(name, value))
#
#         return node
#
#     def handleXml(self, xml):
#         rem = xml.getElementsByTagName('zAppointments')
#         appointments = xml.getElementsByTagName('appointment')
#         self.handleAppts(appointments)
#
#     def getElement(self, element):
#         return self.getText(element.childNodes)
#
#     def handleAppts(self, appts):
#         for appt in appts:
#             self.handleAppt(appt)
#             self.list = []
#
#     def handleAppt(self, appt):
#         begin = self.getElement(appt.getElementsByTagName('begin')[0])
#         duration = self.getElement(appt.getElementsByTagName('duration')[0])
#         subject = self.getElement(appt.getElementsByTagName('subject')[0])
#         location = self.getElement(appt.getElementsByTagName('location')[0])
#         uid = self.getElement(appt.getElementsByTagName('uid')[0])
#
#         self.list.append(begin)
#         self.list.append(duration)
#         self.list.append(subject)
#         self.list.append(location)
#         self.list.append(uid)
#
#         if self.flag == 'file':
#
#             try:
#                 state = self.getElement(appt.getElementsByTagName('state')[0])
#                 self.list.append(state)
#                 alarm = self.getElement(appt.getElementsByTagName('alarmTime')[0])
#                 self.list.append(alarm)
#             except Exception as e:
#                 print(e)
#
#         self.appt_list.append(self.list)
#
#     def getText(self, nodelist):
#         rc = ''
#         for node in nodelist:
#             if node.nodeType == node.TEXT_NODE:
#                 rc = rc + node.data
#         return rc
#
# if __name__ == '__main__':
#     appt = ApptParser('appt.xml')
#     print(appt.appt_list)

# import xml.dom.minidom as minidom
#
# def getTitles(xml):
#     """
#     Print out all titles found in xml
#     """
#     doc = minidom.parse(xml) # returns an xml.dom.minidom.Document object
#     node = doc.documentElement # returns the root tag (catalog)
#     books = doc.getElementsByTagName('book') # returns a list of DOM Element books
#
#     titles = []
#     for book in books:
#         titleObj = book.getElementsByTagName('title')[0] # returns a
#             # one-item list of <DOM Element: 'title'>
#         titles.append(titleObj)
#
#     for title in titles:
#         nodes = title.childNodes
#         for node in nodes:
#             if node.nodeType == node.TEXT_NODE: # node.TEXT_NODE == 3, an integer
#                 # representing the node type
#                 print(node.data)
#
# if __name__ == '__main__':
#     document = 'example.xml'
#     getTitles(document)

# # Creating XML with ElementTree
# import xml.etree.ElementTree as xml
#
# def createXML(filename):
#     """
#     Create an example XML file
#     """
#     root = xml.Element('zAppointments')
#     appt = xml.Element('appointment')
#     root.append(appt)
#
#     # add appointment children
#     begin = xml.SubElement(appt, 'begin')
#     begin.text = '1181251680'
#
#     uid = xml.SubElement(appt, 'uid')
#     uid.text = '040000008200E000'
#
#     alarmTime = xml.SubElement(appt, 'alarmTime')
#     alarmTime.text = '1191582063'
#
#     state = xml.SubElement(appt, 'state')
#
#     location = xml.SubElement(appt, 'location')
#
#     duration = xml.SubElement(appt, 'duration')
#     duration.text = '1800'
#
#     subject = xml.SubElement(appt, 'subject')
#
#     tree = xml.ElementTree(root)
#     with open(filename, 'wb') as fh:
#         tree.write(fh)
#
# if __name__ == '__main__':
#     createXML('appt.xml')

# # debug_test
# def doubler(a):
#     """Doubler"""
#     result = a * 2
#     print(result)
#     return(result)
#
# def main():
#     """
#     main
#     """
#     for i in range(1, 10):
#         doubler(i)
#
# if __name__ == '__main__':
#     main()
#
# # python -m pdb python101.py
# # if a function is called, "step" will go into the function
# # if a function is called, "next" will execute the function without entering it
# # "args" or 'a' will print the current argument list
# # "jump" or 'j' will jump to a line
# # "break 942" creates a breakpoint at line 942

# def another_function(function):
#     """A function that accepts and returns another function"""
#
#     def other_func():
#         val = 'The result of {} is {}'.format(function(), eval(function()))
#         return val
#     return other_func
#
# # another_function needs to be defined before this decorator
# # this means a_function = another_function(a_function)
# # a_function() now returns 'The result of 1+1 is 2'
# @another_function
# def a_function():
#     """A pretty useless function"""
#     return '1+1'
#
# if __name__ == '__main__':
#     value = a_function()
#     print(value)
#     # pass in 'a_function' WITHOUT CALLING IT
#     decorated_function = another_function(a_function)
#     print(decorated_function())

# # creating a logging decorator
# import logging
#
# def log(func):
#     """
#     Log what function is called
#     """
#     def wrap_log(*args, **kwargs):
#         name = func.__name__
#         # logging.getLogger returns a logger with the specified name
#         logger = logging.getLogger(name)
#         logger.setLevel(logging.INFO)
#
#         # add file handler
#         fh = logging.FileHandler('{}.log'.format(name))
#         # can't use .format with this, format is defined by the logging module
#         fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#         formatter = logging.Formatter(fmt)
#         fh.setFormatter(formatter)
#         logger.addHandler(fh)
#
#         logger.info('Running function: {}'.format(name))
#         result = func(*args, **kwargs)
#         logger.info('Result: {}'.format(result))
#         return func
#     return wrap_log
#
# # this will now create a double_function.log file when double_function is called
# @log
# def double_function(a):
#     """
#     Double the input parameter
#     """
#     return a * 2
#
# if __name__ == '__main__':
#     value = double_function(2)

# #An "instance method" uses the information contained in the instance
# #    to figure out what value to return (or which side-effect to do).
# #    These are very common.
# #A "class method" uses information about the class (and not an
# #    instance of that class) to affect what it does (they're typically
# #    used to create new instances as alternative constructors, and
# #    thus aren't incredibly common).
# #A "static method" doesn't use any information about the class or
# #    instance to calculate what it does. It is usually just in the class
# #    for convenience. (As such, these aren't very common either.)

# class DecoratorTest(object):
#     """
#     Test regular method vs @classmethod vs @staticmethod
#     """
#     def __init__(self):
#         """Constructor"""
#         pass
#
#     def doubler(self, x):
#         """"""
#         print('running doubler')
#         return x * 2
#
#     # This can be called by the class itself, and doesn't need an instance
#     # This doesn't know which instance called it
#     @classmethod
#     def class_tripler(klass, x):
#         """"""
#         print('running tripler: {}'.format(klass))
#         return x * 3
#
#     # This can be called by class or instance also.
#     # can't be called without the class or instance though.
#     @staticmethod
#     def static_quad(x):
#         """"""
#         print('running quad')
#         return x * 4
#
# if __name__ == '__main__':
#     DecoratorTest_instance = DecoratorTest()
#     print(DecoratorTest_instance.doubler(5))
#
#     print(DecoratorTest_instance.class_tripler(3))
#     print(DecoratorTest.class_tripler(3))
#
#     print(DecoratorTest_instance.static_quad(2))
#     print(DecoratorTest.static_quad(3))
#
#     print(DecoratorTest_instance.doubler)
#     print(DecoratorTest_instance.class_tripler)
#     print(DecoratorTest_instance.static_quad)

# class Person(object):
#     """"""
#     def __init__(self, first_name, last_name):
#         """Constructor"""
#         self.first_name = first_name
#         self.last_name = last_name
#
#     # converts Person.full_name into a read-only attribute
#     @property
#     def full_name(self):
#         """
#         Return the full name
#         """
#         return '{} {}'.format(self.first_name, self.last_name)

# #classmethods can be used to create instances of a class in a different way to __init__,
# #    e.g. from a file. They can also keep track of things outside the instance.
# #    So they can increment the number of each instance automatically when created using
# #    the @classmethod.

# from decimal import Decimal
#
# class Fees(object):
#     """"""
#
#     def __init__(self):
#         """Constructor"""
#         self._fee = None
#
#     def get_fee(self):
#         """
#         Return the current fee
#         """
#         return self._fee
#
#     def set_fee(self, value):
#         """
#         Set the fee
#         """
#         if isinstance(value, str):
#             self._fee = Decimal(value)
#         elif isinstance(value, Decimal):
#             self._fee = value
#
#     # This allows us to acces Fees._fee by using Fees.fee
#     fee = property(get_fee, set_fee)

# # custom decorators
# from decimal import Decimal
#
# class Fees(object):
#     """"""
#
#     def __init__(self):
#         """Constructor"""
#         self._fee = None
#
#     @property
#     def fee(self):
#         """
#         The fee property - the getter
#         """
#         return self._fee
#
#     @fee.setter
#     def fee(self, value):
#         """
#         The setter of the fee property
#         """
#         if isinstance(value, str):
#             self._fee = Decimal(value)
#         elif isinstance(value, Decimal):
#             self._fee = value
#
# if __name__ == '__main__':
#     f = Fees()

# # the lambda function
# import math
#
# # normal style
# def sqroot(x):
#     return math.sqrt(x)
#
# # lambda style
# lambda_sqroot = lambda x: math.sqrt(x)

# import tkinter as tk
#
# class App:
#     """"""
#
#     def __init__(self, parent):
#         """Constructor"""
#         frame = tk.Frame(parent)
#         frame.pack()
#
#         btn22 = tk.Button(frame, text='22', command=lambda: self.printNum(22))
#         btn22.pack(side=tk.LEFT)
#         btn44 = tk.Button(frame, text='44', command=lambda: self.printNum(44))
#         btn44.pack(side=tk.LEFT)
#
#     def printNum(self, num):
#         """"""
#         print('You pressed the {} button'.format(num))
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()

# # code profiling
# import hashlib
# import cProfile
#
# print(cProfile.run("hashlib.md5(b'abcdefghijkl').digest()"))

# import time
#
# def fast():
#     """"""
#     print('I run fast!')
#
# def slow():
#     """"""
#     time.sleep(3)
#     print('I run slow!')
#
# def medium():
#     """"""
#     time.sleep(0.5)
#     print('I run medium!')
#
# def main():
#     """"""
#     fast()
#     slow()
#     medium()
#
# if __name__ == '__main__':
#     main()
#
# # python -m cProfile -o output.txt python101.py

# import pstats
#
# p = pstats.Stats('output.txt')
# p.strip_dirs().sort_stats(-1).print_stats()

# # Testing with doctest
# def double(a):
#     """
#     >>> double(4)
#     8
#     >>> double(9)
#     18
#     """
#     return a * 2
# # to check: (-v for verbose output)
# # python -m doctest -v python101.py

# # sharing files with python
# # cd into the directory
# python -m SimpleHTTPServer 8000 # can use pretty much any port, like 8080
# # To access the shared files go to http://your_ip_address:8000.

# # running tests with "python python101.py"
# def double(a):
#     """
#     >>> double(4)
#     8
#     >>> double(9)
#     18
#     """
#     return a * 2
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)

# # running doctest from separate file
# python -m doctest -v tests.txt

# # TDD with unittest
# import unittest
#
# class TestBowling(unittest.TestCase):
#     """Docstring"""
#     def test_all_ones(self):
#         """Constructor"""
#         game = Game()
#         # 11 rolls with 1 pin each time
#         game.roll(11, 1)
#         self.assertEqual(game.score, 11)
#
# class Game:
#     """Docstring"""
#
#     def __init__(self):
#         """Constructor"""
#         self.score = 0
#
#     def roll(self, numOfRolls, pins):
#         """"""
#         for roll in numOfRolls:
#             self.score += pins
#
# if __name__ == '__main__':
#     unittest.main()

# # Fixing first test
# import unittest
#
# class TestBowling(unittest.TestCase):
#     """Docstring"""
#     def test_all_ones(self):
#         """Constructor"""
#         game = Game()
#         # 11 rolls with 1 pin each time
#         game.roll(11, 1)
#         self.assertEqual(game.score, 11)
#
# class Game:
#     """Docstring"""
#
#     def __init__(self):
#         """Constructor"""
#         self.score = 0
#
#     def roll(self, numOfRolls, pins):
#         """"""
#         for roll in range(numOfRolls):
#             self.score += pins
#
# if __name__ == '__main__':
#     unittest.main()

# # second test
# import unittest
#
# class TestBowling(unittest.TestCase):
#     """Docstring"""
#
#     def test_all_ones(self):
#         """Constructor"""
#         game = Game()
#         pins = [1 for i in range(11)]
#         game.roll(11, pins)
#         self.assertEqual(game.score, 11)
#
#     def test_strike(self):
#         """Strike is 10 + the value of the next two rolls."""
#         game = Game()
#         game.roll(11, [10, 5, 4])
#         self.assertEqual(game.score, 28)
#
# class Game:
#     """Docstring"""
#
#     def __init__(self):
#         """Constructor"""
#         self.score = 0
#         self.pins = [0 for i in range(11)]
#
#     def roll(self, numOfRolls, pins):
#         """"""
#         x = 0
#         for pin in pins:
#             self.pins[x] = pin
#             x += 1
#         x = 0
#         for roll in range(numOfRolls):
#             if self.pins[x] == 10:
#                 self.score = self.pins[x] + self.pins[x+1] + self.pins[x+2]
#             else:
#                 self.score += self.pins[x]
#             x += 1
#         print(self.score)
#
# if __name__ == '__main__':
#     unittest.main()

# # Third test, for spares
# # 2 tests actually broken lol
# import unittest
#
# class TestBowling(unittest.TestCase):
#     """Docstring"""
#
#     def setUp(self):
#         """"""
#         self.game = Game()
#
#     def test_all_ones(self):
#         """Constructor"""
#         game = Game()
#         pins = [1 for i in range(11)]
#         game.roll(11, pins)
#         self.assertEqual(self.game.score, 11)
#
#     def test_spare(self):
#         """
#         Spare is worth 10 + value of next roll.
#         """
#         self.game.roll(11, [5, 5, 5, 4])
#         self.assertEqual(self.game.score, 24)
#
#     def test_strike(self):
#         """Strike is 10 + the value of the next two rolls."""
#         game = Game()
#         game.roll(11, [10, 5, 4])
#         self.assertEqual(game.score, 28)
#
# class Game:
#     """Docstring"""
#
#     def __init__(self):
#         """Constructor"""
#         self.score = 0
#         self.pins = [0 for i in range(11)]
#
#     def roll(self, numOfRolls, pins):
#         """"""
#         x = 0
#         for pin in pins:
#             self.pins[x] = pin
#             x += 1
#         x = 0
#         spare_begin = 0
#         spare_end = 2
#         for roll in range(numOfRolls):
#             spare = sum(self.pins[spare_begin:spare_end])
#             if self.pins == 10:
#                 self.score = self.pins[x] + self.pins[x + 1] + self.pins[x + 2]
#             elif spare == 10:
#                 self.score = spare + self.pins[x + 2]
#                 x += 1
#             else:
#                 self.score += self.pins[x]
#             x += 1
#             if x == 11:
#                 break
#             spare_begin += 2
#             spare_end += 2
#             print(self.score)
#
# if __name__ == '__main__':
#     unittest.main()

# # upgrde a package
# pip install -U package_name
# # only pip can install wheels
# # only easy_install can install eggs

# import configobj
#
# def createConfig(path):
#     config = configobj.ConfigObj()
#     config.filename = path
#     config['Sony'] = {}
#     config["Sony"]["product"] = "Sony PS3"
#     config["Sony"]["accessories"] = ['controller', 'eye', 'memory stick']
#     config["Sony"]["retail price"] = "$400"
#     config.write()
#
# if __name__ == "__main__":
#     createConfig("config.ini")

# # Turning xml into a dictionary
# # A more realistic example would turn the extracted data into a "Book" class.
# # Can also do this with JSON feeds.
# from lxml import etree
#
# def parseBookXML(xmlFile):
#     with open(xmlFile) as fobj:
#         xml = fobj.read()
#
#     root = etree.fromstring(xml)
#     book_dict = {}
#     books = []
#     for book in root.getchildren():
#         for elem in book.getchildren():
#             if not elem.text:
#                 text = "None"
#             else:
#                 text = elem.text
#             print(elem.tag + " => " + text)
#             book_dict[elem.tag] = text
#         if book.tag == "book":
#             books.append(book_dict)
#             book_dict = {}
#     return books
#
# if __name__ == "__main__":
#     parseBookXML("example.xml")

# from lxml import etree, objectify
#
# def parseXML(xmlFile):
#     """Parse the XML file"""
#     with open(xmlFile) as f:
#         xml = f.read()
#
#     root = objectify.fromstring(xml)
#
#     # returns attributes in element node as dict
#     attrib = root.attrib
#
#     # how to extract element data
#     begin = root.appointment.begin
#     uid = root.appointment.uid
#
#     # loop over lements and print their tags and text
#     for appt in root.getchildren():
#         for e in appt.getchildren():
#             print('%s => %s' % (e.tag, e.text))
#         print()
#
#     # how to change an element's text
#     root.appointment.begin = 'something else'
#     print(root.appointment.begin)
#
#     # how to add a new element
#     root.appointment.new_element = 'new data'
#
#     # remove the py:pytype stuff
#     objectify.deannotate(root)
#     etree.cleanup_namespaces(root)
#     obj_xml = etree.tostring(root, pretty_print=True)
#     print(obj_xml)
#
#     # save your xml
#     with open('new.xml', 'wb') as f:
#         f.write(obj_xml)
#
# if __name__ == '__main__':
#     f = r'sample.xml'
#     parseXML(f)

# # code analysis with pylint
# import sys
#
# class CarClass:
#     """"""
#
#     def __init__(self, color, make, model, year):
#         """Constructor"""
#         self.color = color
#         self.make = make
#         self.model = model
#         self.year = year
#
#         if 'Windows' in platform.platform():
#             print("You're using Windows!")
#
#         self.weight = self.getWeight(1,2,3)
#
#     def getWeight(this):
#         """"""
#         return '2000 lbs'


# # crummy_code_fixed.py
# import platform
# class CarClass:
#     """"""
#     def __init__(self, color, make, model, year):
#         """Constructor"""
#         self.color = color
#         self.make = make
#         self.model = model
#         self.year = year
#
#         if "Windows" in platform.platform():
#             print("You're using Windows!")
#
#         self.weight = self.get_weight(3)
#
#     def get_weight(self, this):
#         """"""
#         return "2000 lbs"

# # The requests package
# import urllib.request
# import urllib.parse
# import webbrowser
#
# data = urllib.parse.urlencode({'q': 'Python'})
# url = 'http://duckduckgo.com/html/'
# full_url = url + '?' + data
# response = urllib.request.urlopen(full_url)
# with open('results.html', 'wb') as f:
#     f.write(response.read())
#
# webbrowser.open('results.html')

# # requests equivalent
# import requests
#
# url = 'https://duckduckgo.com/html/'
# payload = {'q':'python'}
# r = requests.get(url, params=payload)
# with open('requests_results.html', 'wb') as f:
#     f.write(r.content)

# # creating tables with SQLAlchemy
# from sqlalchemy import create_engine, ForeignKey
# from sqlalchemy import Column, Date, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, backref
#
# # connection string
# engine = create_engine('sqlite:///mymusic.db', echo=True)
# Base = declarative_base()
#
# # classes based on Base
# class Artist(Base):
#     """"""
#     __tablename__ = 'artists'
#
#     id = Column(Integer, primary_key=True) # will auto-increment
#     name = Column(String)
#
# class Album(Base):
#     """"""
#     __tablename__ = 'albums'
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     release_date = Column(Date)
#     published = Column(String)
#     media_type = Column(String)
#
#     artist_id = Column(Integer, ForeignKey('artists.id')) # uniqely indentifies a row
#         # in the 'Artist' table. Lots of different albums can have the same ForignKey,
#         # so this is a many-to-one relationship
#     artist = relationship('Artist', backref=backref('albums', order_by=id))
#
# # create tables
# Base.metadata.create_all(engine)

# # data insertion
# import datetime
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from table_def import Album, Artist
#
# engine = create_engine('sqlite:///mymusic.db', echo=True)
#
# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # create an Artist
# new_artist = Artist(name='Newsboys')
#
# new_artist.albums = [Album(title='Read All About It',
#     release_date=datetime.date(1988,12,1),
#     publisher='Refuge',
#     media_type='CD')]
#
# # add more albums
# more_albums = [Album(title="Hell Is for Wimps",
#         release_date=datetime.date(1990,7,31),
#         publisher="Star Song", media_type="CD"),
#     Album(title="Love Liberty Disco",
#         release_date=datetime.date(1999,11,16),
#         publisher="Sparrow", media_type="CD"),
#     Album(title="Thrive",
#         release_date=datetime.date(2002,3,26),
#         publisher="Sparrow", media_type="CD")]
# new_artist.albums.extend(more_albums)
#
# # Add record to session object
# session.add(new_artist)
# # commit the record
# session.commit()
#
# # add several artists
# session.add_all([
#     Artist(name="MXPX"),
#     Artist(name="Kutless"),
#     Artist(name="Thousand Foot Krutch")
#     ])
# session.commit()

# # data modification
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from table_def import Album, Artist
#
# engine = create_engine('sqlite:///mymusic.db', echo=True)
#
# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # querying for a record in the Artist table
# res = session.query(Artist).filter(Artist.name=='Kutless').first()
# print(res.name)
#
# # changing the name
# res.name = 'Beach Boys'
# session.commit()
#
# # editing Album data
# artist, album = session.query(Artist, Album).filter(
#     Artist.id==Album.artist_id).filter(Album.title=='Thrive').first()
# album.title = 'Step Up to the Microphone'
# session.commit()

# # data deletion
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from table_def import Album, Artist
#
# engine = create_engine('sqlite:///mymusic.db', echo=True)
#
# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
#
# res = session.query(Artist).filter(Artist.name=='MXPX').first()
#
# session.delete(res)
# session.commit()

# # sample queries
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from table_def import Album, Artist
#
# engine = create_engine('sqlite:///mymusic.db', echo=True)
#
# # create a Session
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # how to do a SELECT *
# res = session.query(Artist).all()
# for artist in res:
#     print(artist.name)
#
# # how to SELECT the first result
# res = session.query(Artist).filter(Artist.name=='Newsboys').first()
#
# # how to sort the results (ORDER BY)
# res = session.query(Album).order_by(Album.title).all()
# for album in res:
#     print(album.title)
#
# # how to do a JOINed query
# qry = session.query(Artist, Album)
# qry = qry.filter(Artist.id==Album.artist_id)
# artist, album = qry.filter(Album.title=='Step Up to the Microphone').first()
#
# # how to use LIKE in a query
# # starts with capital 'S', some character, an 'a', then anything else.
# res = session.query(Album).filter(Album.publisher.like('S%a%')).all()
# for item in res:
#     print(item.publisher)

# # virtualenv
# # The virtualenv package does not work with Anaconda.
# # From the terminal prompt you should create a new virtual
# # environment using the conda statement conda -n new_env_name.
# conda search "^python$" # find which versions of python are available
# conda create -n yourenvname python=x.x anaconda
# source activate yourenvname # modify PATH and shell variables to point to the new env
# conda info -e # list all environments
# conda install -n yourenvname [package] # install packages only to venv
# source deactivate # end session in current venv
# conda remove -n yourenvname -all # delete a conda env

######################
