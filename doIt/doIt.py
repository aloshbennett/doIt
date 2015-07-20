'''
Created on Jul 19, 2015

@author: msoundar
'''
import logging;
from utils import filePersistor;

logger = logging.getLogger("doIt");
do_keywords = set(['do']);
done_keywords = set(['done','finished','completed']);
schedule_keywords = set(['prepone','postpone']);
display_keywords = set(['list','display','show']);
fileName = "todo.txt";

def do(task):
    ''' adds a task '''
    fhandle = open(fileName,'a');
    filePersistor.persist(task, fhandle);
    fhandle.close();
    
def done(task):
    ''' removes a task '''
    
def schedule(task):
    ''' schedule a task '''
    
def display(from_date_time=None, to_date_time=None):
    ''' lists tasks within a range '''
    tasks = filePersistor.getTasks(fileName);
    # handle filtering
    logger.info(tasks);
