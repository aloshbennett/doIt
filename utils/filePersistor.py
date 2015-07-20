'''
Created on Jul 18, 2015

@author: msoundar
'''
import sys;

def persist(task, fhandle=None):
    if not fhandle:
        fhandle = sys.stdout;
    for task_part in task.keys():
        fhandle.write(task_part + ':' + str(task[task_part]) + ' ');
    fhandle.write(";\n");

def persistAll(tasks,fileName="todo.txt"):
    fhandle = open(fileName, 'w');
    for task in tasks:
        persist(task,fhandle);
    fhandle.close();
    
def getTasks(fileName="todo.txt"):
    tasks = [];
    fhandle = open(fileName,'r');
    for line in fhandle:
        task = {};
        for cmd_value in line.split():
            parts = cmd_value.split(':');
            if len(parts)!=2:
                continue;
            task[parts[0]] = parts[1];
        tasks.append(task);
    return tasks;
