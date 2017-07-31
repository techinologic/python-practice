# #
# # Example file for helloworld
# #
# import sys
#
#
# def main():
#     print "hello world"
#
#
# if __name__ == "__main__":
#     main()
#
# print "me too"
#
# # declare variables
#
# f = 0;
# print f
#
# f = "abc"
# print f
#
# print "String type " + str(123)
#
#
# def someFunction():
#     global f
#     f = "def"
#     print f
#
#
# someFunction()
# print f
#
# ##del f
# print f
#
#
# def func1():
#     print "Im a function"
#
#
# func1()
#
# print func1()
#
# print func1
#
#
# # func with arguments
#
# def func2(arg1, arg2):
#     print arg1, " ", arg2
#
#
# def cube(x):
#     return x * x * x
#
#
# print cube(3)
#
#
# def power(num, x=1):
#     result = 1;
#     for i in range(x):
#         result = result * num
#     return result
#
#
# print power(2, 8)
#
#
# def multi_add(*args):
#     result = 0;
#     for x in args:
#         result = result + x
#     return result
#
#
# print multi_add(2, 3, 5, 7, 4, 2)
#
#
# def main():
#     x, y = 1000, 1000
#     if x < y:
#         st = "x is less than y"
#     elif x == y:
#         st = "x is same as y"
#     else:
#         st = "y is less than x"
#     print st
#
#     st = "x is less than y" if (x < y) else "x is greater than or equal to y"
#     print st
#
#
# def test():
#     x = 0
#     while (x < 5):
#         print x
#         x = x + 1
#
#
# for y in range(5, 10):
#     print "for loop", y
#
#     days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#     for d in days:
#         print d
#
#     for x in range(5, 10):
#         if x % 2: continue
#         print x
#
#
#     days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#     for i, d in enumerate(days):
#         print i, d
#
# class myClass():
#     def method1(self):
#         print "myClass method1"
#
#     def method2(self, someString):
#         print "myclass method2" + someString
#
# def classTest():
#     c = myClass()
#     c.method1()
#     c.method2(" This is a string")
#
# if __name__ == '__main__':
#     classTest()
#
#
# if __name__ == '__main__':
#     n = int(raw_input())
#     if (n % 2 == 1):
#         print "Not Weird"
#     elif (n < 6):
#         print "Weird"
#     elif (n < 20):
#         print "Not Weird"
#     else:
#         print "Not Weird"
#
# if __name__ == '__main__':
#     g = int(raw_input())
#
#     for g in range(5, 0):
#         print g
#
# if __name__ == '__main__':
#     n = int(raw_input())
#
#     x = 1
#     while x != n + 1:
#         sys.stdout.write(str(x))
#         x = x + 1
#

# Dates, time, and datetime classes

from datetime import date
from datetime import time
from datetime import datetime


def main():
    # Get today's date from the simple today() method from date class
    today = date.today()
    print "Today's date is", today

    # print out date's individual components
    print "Date components: ", today.day, today.month, today.year

    # todays weekday 0=mon -> 6=sun
    print "Today's weekday: ", today.weekday()

    # Date time objects
    today = datetime.now()
    print "The current date and time is: ", today

    t = datetime.time(datetime.now())
    print "Today's date time: ", t

    wd = date.weekday(today)

    days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

    print "today is: ",
if __name__ == "__main__":
    main();
    
    
    