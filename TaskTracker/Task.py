'''
@author: Thomas
'''
import random
import time


class Task(object):
    taskIds = []

    def __init__(self, subject, dueDate, assignmentTitle, description=''):
        self.subject = subject
        self.assignmentTitle = assignmentTitle
        self.description = description
        self.ID = ''
        self.randomID()
        self.created = ''
        self.createdDOY = 0
        self.timeStamp()
        self.dueDate = self.createdDOY + dueDate

    def updateAttribute(self, attributeNumber, update):
        if attributeNumber == 0:
            self.subject = update
        elif attributeNumber == 1:
            self.dueDate = self.createdDOY + update
        elif attributeNumber == 2:
            self.assignmentTitle = update
        elif attributeNumber == 3:
            self.description = update
        return self

    def randomID(self):
        while True:
            id = ''
            id += str(random.randint(10, 100))
            id += random.choice('abcdefghijklmnopqrstuv'
                                'ABCDEFGHIJKLMNOPQRSTUV')
            id += random.choice('abcdefghijklmnopqrstuv'
                                'ABCDEFGHIJKLMNOPQRSTUV')
            id += str(random.randint(10, 100))
            if not id in self.taskIds:
                self.ID = id
                break
            else:
                continue

    def timeStamp(self):
        self.created = time.strftime('%m/%d/%Y')
        self.createdDOY = time.localtime().tm_yday

if __name__ == '__name__':
    print 'Please run this program from TaskTracker.py'