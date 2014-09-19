__author__ = 'santhosh'
class Day:
    def __init__(self):
        print "date: Day is 19"

class Month(Day):
    def __init__(self):
        print "Month is September"

class Year(Month):
    def __init__(self):
        print "Year is 2014"

 p1 = Year()
