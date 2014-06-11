'''
@author: Thomas
'''
import Task
import pickle
import os
import sys
import time

uncompletedTasks = {}


def newTask():
    subject = raw_input('What subject is this task for? ')
    dueDate = int(raw_input('How many days do you have to do this? '))
    title = raw_input('What is the title? ')
    option = raw_input('Would you like to add a description? (y/n) ')
    if option.lower() == 'y':
        description = raw_input('Add a description: ')
        addToTaskDic(Task.Task(subject, dueDate, title, description))
    else:
        addToTaskDic(Task.Task(subject, dueDate, title))


def addToTaskDic(task):
    uncompletedTasks[task.ID] = task


def listTasks():
    tasksByDueDate = {}
    for task in uncompletedTasks.keys():
        if not str(uncompletedTasks[task].dueDate - time.localtime().tm_yday) in tasksByDueDate.keys():
            tasksByDueDate[str(uncompletedTasks[task].dueDate - time.localtime().tm_yday)] = [uncompletedTasks[task]]
        else:
            tasksByDueDate[task].append(uncompletedTasks[task])
    for taskList in sorted(tasksByDueDate):
        print 'These assignments are due in ' + str(tasksByDueDate[taskList][0].dueDate - time.localtime().tm_yday),\
            'days:'
        for sortedTask in tasksByDueDate[taskList]:
            print '    ' + sortedTask.assignmentTitle + ' for ' + sortedTask.subject + '. (id: ' + sortedTask.ID + ')'


def removeTask(taskID):
    del uncompletedTasks[taskID]


def saveTasks(uncompletedTasks):
    pickle.dump(uncompletedTasks, open(os.getcwd()+'\\tasks.p', 'w'))


def translateUpdateStrToInt(task, command):
    if command[14:21] == 'subject':
        update = command[22:]
        uncompletedTasks[task].updateAttribute(0, update)
    elif command[14:18] == 'date':
        update = int(command[19:])
        uncompletedTasks[task].updateAttribute(1, update)
    elif command[14:19] == 'title':
        update = command[20:]
        uncompletedTasks[task].updateAttribute(2, update)
    elif command[14:25] == 'description':
        update = command[26:]
        uncompletedTasks[task].updateAttribute(3, update)

if __name__ == '__main__':
    try:
        uncompletedTasks = pickle.load(open(os.getcwd() + '\\tasks.p'))
    except IOError:
        pass
    while True:
        command = raw_input('Enter a command. ')
        if command == 'add':
            newTask()
        elif command == 'list':
            listTasks()
        elif command[:6] == 'remove':
            removeTask(command.strip()[7:])
        elif command == 'save':
            try:
                saveTasks(uncompletedTasks)
                print 'Saved task list'
            except Exception as e:
                print e
                continue
        elif command[:6] == 'update':
            translateUpdateStrToInt(command[7:13], command)
        elif command[:8] == 'describe':
            print uncompletedTasks[command.strip()[9:]].description
        elif command[:7] == 'created':
            print uncompletedTasks[command.strip()[8:]].created
        elif command == 'exit':
            option = raw_input('Would you like to save before exiting? (y/n) ')
            if option.lower() != 'n':
                saveTasks(uncompletedTasks)
            sys.exit()
        else:
            print 'Invalid command.\nCommands are: add, list, remove <ID>, describe <ID>, created <ID>\n' \
                  'save, update <ID> <Subject> <data>, exit'