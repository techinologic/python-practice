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
# def main():
#     # Get today's date from the simple today() method from date class
#     today = date.today()
#     print "Today's date is", today
#
#     # print out date's individual components
#     print "Date components: ", today.day, today.month, today.year
#
#     # todays weekday 0=mon -> 6=sun
#     print "Today's weekday: ", today.weekday()
#
#     # Date time objects
#     today = datetime.now()
#     print "The current date and time is: ", today
#
#     t = datetime.time(datetime.now())
#     print "Today's date time: ", t
#
#     wd = date.weekday(today)
#
#     days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
#
#     print "today is day number: %d" % wd
#     print "Which is a " + days[wd]
# if __name__ == "__main__":
#     main();
#
#
#

# from datetime import date
# from datetime import time
# from datetime import datetime
# from datetime import timedelta
#
#
# # construct a basic timedelta and print it
# print timedelta(days=365, hours=5, minutes=1)
#
# # print today's date
# print "Today's date is: " + str(datetime.now())
#
# # print date one year from now
# print "one year from now it will be: " + str(datetime.now() + timedelta(days=365))
#
# print "in two weeks and 3 days, it will be: " + str(datetime.now() + timedelta(weeks=2, days=3))
#
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("%A %B %d, %Y")
#
# print "1 week ago, it was: " + s
#
#
# ## calculate how many days until April Fool's day ##
#
# # get today's date
# today = datetime.now()
# afd = date(today.year, 4, 1)
#
# if afd < today:
#     print "April fools day already went by by %d days ago" % ((today-afd).days)
#     afd = afd.replace(year=today.year + 1)
#
# time_to_afd = abs(afd-today)
# print time_to_afd.days, "days until next april fools day!"

###### WORKING WITH CALENDAR #######

# import calendar
#
# # create plain text calendar
# c = calendar.TextCalendar(calendar.MONDAY)
# str = c.formatmonth(2017, 8, 0, 0)
# print str
#
# hc = calendar.HTMLCalendar(calendar.MONDAY)
# str = hc.formatmonth(2017, 1)
# print str
#
# # print each day of the calendar
# for i in c.itermonthdays(2017, 8):
#     print i
#
# # locales
#
# for name in calendar.month_name:
#     print name
#
# for day in calendar.day_name:
#     print day
#
# # display the date of every friday every month
# for m in range(1, 13): # represents months
#     cal = calendar.monthcalendar(2017, m)
#     weekone = cal[0]
#     weektwo = cal[1]
#
#     if weekone[calendar.FRIDAY] != 0:
#         meetday = weekone[calendar.FRIDAY]
#     else:
#         meetday = weektwo[calendar.FRIDAY]
#     print "%10s %2d" % (calendar.month_name[m], meetday)


############# READING AND WRITING FILES ###################

# create a file and write something inside it
def main():
# WRITE ACCESS
    # f = open("textfile.txt","w+") # write access/ will overwrite if done again
    #
    # for i in range(10):
    #     f.write("This is line %d\r\n" % (i+1))
    #
    # f.close()

# APPEND ACCESS
    # f = open("textfile.txt","a+") # append / will append to previously written data in file
    #
    # for i in range(10):
    #     f.write("This is line %d\r\n" % (i+1))
    #
    # f.close()

# READ ACCESS / OPEN FILE INTO CONSOLE

    # f = open("textfile.txt","r") # append / will append to previously written data in file
    #
    # if f.mode == 'r':
    #     contents = f.read()
    # print contents
    # f.close()

# READLINES FUNCTINO WILL READ EACH LINE INTO A LIST and print EACH LINE

    f = open("textfile.txt","r") # append / will append to previously written data in file

    if f.mode == 'r':
        fl = f.readlines()
    for x in fl:
        print x




if __name__ == '__main__':
    main()